"""Expression compiler — the normative contract is methodology/reference/expression-language.md.

Each event-embedded expression is parsed with ``ast``, checked against the §4
allow-list, name-resolved against the state catalog and the owning event's
declared resolutions/branches, rewritten to elementwise NumPy (``and``/``or``/
``not`` -> ``&``/``|``/``~``; chained comparisons -> conjunctions; whitelisted
functions -> ``np.*``), and compiled once into ``fn(ns) -> (R,) ndarray``.

The namespace ``ns`` maps every name the expression reads to an ``(R,)`` view:
factor IDs (``F_GPT``), global variables (``oil_brent``), dotted country
variables (``chn.gdp_real``), and the owning event's own state (``resolution``,
``branch`` as integer codes, ``years_since`` as int). ``ns["_shape"]`` must hold
``(R,)`` so constant-only expressions broadcast correctly.
"""
from __future__ import annotations

import ast
from dataclasses import dataclass, field

import numpy as np

from .types import CatalogError, ExprFn, StateCatalog

EVENT_STATE_NUMERIC = ("years_since",)
EVENT_STATE_CATEGORICAL = ("resolution", "branch")

# whitelisted function name -> (numpy expression template, arity, result kind)
_FUNCS = {
    "min": ("np.minimum({0}, {1})", 2, "numeric"),
    "max": ("np.maximum({0}, {1})", 2, "numeric"),
    "abs": ("np.abs({0})", 1, "numeric"),
    "clip": ("np.clip({0}, {1}, {2})", 3, "numeric"),
    "exp": ("np.exp({0})", 1, "numeric"),
    "log": ("np.log({0})", 1, "numeric"),
    "sqrt": ("np.sqrt({0})", 1, "numeric"),
    "where": ("np.where({0}, {1}, {2})", 3, "numeric"),
}
_BINOPS = {ast.Add: "+", ast.Sub: "-", ast.Mult: "*", ast.Div: "/", ast.Pow: "**"}
_CMPOPS = {ast.Lt: "<", ast.LtE: "<=", ast.Gt: ">", ast.GtE: ">=", ast.Eq: "==", ast.NotEq: "!="}


@dataclass
class ExprContext:
    """What names an expression may resolve against."""
    state: StateCatalog
    event_id: str
    resolution_codes: dict[str, int] = field(default_factory=dict)
    branch_codes: dict[str, int] = field(default_factory=dict)     # unique branch names only
    ambiguous_branches: set[str] = field(default_factory=set)      # names declared under >1 resolution
    allow_event_state: bool = True


class _Compiler:
    def __init__(self, ctx: ExprContext, source: str, slot: str):
        self.ctx = ctx
        self.source = source
        self.slot = slot
        self.names: list[str] = []

    # -- error helper -------------------------------------------------------
    def fail(self, why: str) -> CatalogError:
        return CatalogError(f"{self.ctx.event_id}: expression in {self.slot} rejected — {why}: {self.source.strip()!r}")

    # -- entry --------------------------------------------------------------
    def compile(self) -> ExprFn:
        try:
            # Parenthesize so multi-line YAML block scalars (schema §Type 2 examples) parse as one expression.
            tree = ast.parse("(" + self.source + "\n)", mode="eval")
        except SyntaxError as e:
            raise self.fail(f"does not parse ({e.msg})") from None
        code, kind = self.visit(tree.body)
        return ExprFn(self.source, tuple(dict.fromkeys(self.names)), self._build(code, kind), kind)

    def _build(self, code: str, kind: str):
        dtype = "np.bool_" if kind == "boolean" else "np.float64"
        src = f"lambda ns: np.broadcast_to(np.asarray({code}, dtype={dtype}), ns['_shape'])"
        return eval(compile(src, f"<expr {self.ctx.event_id} {self.slot}>", "eval"), {"np": np, "__builtins__": {}})

    # -- visitors: return (python_code, kind) ------------------------------
    def visit(self, node: ast.AST) -> tuple[str, str]:
        m = getattr(self, "v_" + type(node).__name__, None)
        if m is None:
            raise self.fail(f"disallowed construct {type(node).__name__}")
        return m(node)

    def v_Constant(self, node: ast.Constant):
        if isinstance(node.value, bool) or not isinstance(node.value, (int, float)):
            if isinstance(node.value, str):
                raise self.fail("string literal outside categorical equality")
            raise self.fail(f"literal of type {type(node.value).__name__}")
        return repr(float(node.value)), "numeric"

    def _bind(self, key: str) -> str:
        self.names.append(key)
        return f"ns[{key!r}]"

    def v_Name(self, node: ast.Name):
        st = self.ctx.state
        n = node.id
        if n in st.factors or n in st.global_vars:
            return self._bind(n), "numeric"
        if n in EVENT_STATE_NUMERIC and self.ctx.allow_event_state:
            return self._bind(n), "numeric"
        if n in EVENT_STATE_CATEGORICAL:
            raise self.fail(f"categorical name {n!r} may only be compared with == or != to a string literal")
        if n in st.country_vars:
            raise self.fail(f"{n!r} is a country variable; write entity.{n}")
        if n in st.entities:
            raise self.fail(f"{n!r} is an entity; write {n}.variable")
        raise self.fail(f"unknown name {n!r}")

    def v_Attribute(self, node: ast.Attribute):
        if not isinstance(node.value, ast.Name):
            raise self.fail("attribute access beyond entity.variable")
        ent, var = node.value.id, node.attr
        st = self.ctx.state
        if ent not in st.entities:
            raise self.fail(f"unknown entity {ent!r} in {ent}.{var}")
        if var not in st.country_vars:
            raise self.fail(f"unknown country variable {var!r} in {ent}.{var}")
        return self._bind(f"{ent}.{var}"), "numeric"

    def v_UnaryOp(self, node: ast.UnaryOp):
        code, kind = self.visit(node.operand)
        if isinstance(node.op, ast.Not):
            if kind != "boolean":
                raise self.fail("'not' applied to a non-boolean operand")
            return f"(~{code})", "boolean"
        if isinstance(node.op, (ast.USub, ast.UAdd)):
            if kind != "numeric":
                raise self.fail("unary sign applied to a boolean operand")
            return f"({'-' if isinstance(node.op, ast.USub) else '+'}{code})", "numeric"
        raise self.fail(f"disallowed unary operator {type(node.op).__name__}")

    def v_BinOp(self, node: ast.BinOp):
        op = _BINOPS.get(type(node.op))
        if op is None:
            raise self.fail(f"disallowed operator {type(node.op).__name__}")
        a, ka = self.visit(node.left)
        b, kb = self.visit(node.right)
        if ka != "numeric" or kb != "numeric":
            raise self.fail(f"arithmetic '{op}' on boolean operands")
        return f"({a} {op} {b})", "numeric"

    def v_BoolOp(self, node: ast.BoolOp):
        sym = "&" if isinstance(node.op, ast.And) else "|"
        parts = []
        for v in node.values:
            c, k = self.visit(v)
            if k != "boolean":
                raise self.fail("'and'/'or' on a non-boolean operand")
            parts.append(c)
        return "(" + f" {sym} ".join(parts) + ")", "boolean"

    def _categorical(self, node: ast.AST) -> str | None:
        if isinstance(node, ast.Name) and node.id in EVENT_STATE_CATEGORICAL:
            return node.id
        return None

    def v_Compare(self, node: ast.Compare):
        operands = [node.left] + list(node.comparators)
        terms = []
        for i, op in enumerate(node.ops):
            sym = _CMPOPS.get(type(op))
            if sym is None:
                raise self.fail(f"disallowed comparison {type(op).__name__}")
            l, r = operands[i], operands[i + 1]
            cat_l, cat_r = self._categorical(l), self._categorical(r)
            if cat_l or cat_r:
                if not self.ctx.allow_event_state:
                    raise self.fail("event state names are not available in this slot")
                if sym not in ("==", "!="):
                    raise self.fail("categorical comparison must be == or !=")
                name_node, lit = (l, r) if cat_l else (r, l)
                if not (isinstance(lit, ast.Constant) and isinstance(lit.value, str)):
                    raise self.fail("categorical name must be compared with a string literal")
                table = self.ctx.resolution_codes if name_node.id == "resolution" else self.ctx.branch_codes
                if name_node.id == "branch" and lit.value in self.ctx.ambiguous_branches:
                    raise self.fail(f"branch name {lit.value!r} is declared under more than one resolution")
                if lit.value not in table:
                    raise self.fail(f"undeclared {name_node.id} name {lit.value!r}")
                terms.append(f"({self._bind(name_node.id)} {sym} {table[lit.value]})")
                continue
            a, ka = self.visit(l)
            b, kb = self.visit(r)
            if ka != "numeric" or kb != "numeric":
                raise self.fail("comparison of boolean operands")
            terms.append(f"({a} {sym} {b})")
        return "(" + " & ".join(terms) + ")", "boolean"

    def v_Call(self, node: ast.Call):
        if not isinstance(node.func, ast.Name) or node.func.id not in _FUNCS:
            fn = getattr(node.func, "id", type(node.func).__name__)
            raise self.fail(f"call to non-whitelisted function {fn!r}")
        if node.keywords:
            raise self.fail("keyword arguments are not permitted")
        template, arity, kind = _FUNCS[node.func.id]
        if len(node.args) != arity:
            raise self.fail(f"{node.func.id}() takes exactly {arity} argument(s)")
        args = []
        for i, a in enumerate(node.args):
            c, k = self.visit(a)
            want = "boolean" if (node.func.id == "where" and i == 0) else "numeric"
            if k != want:
                raise self.fail(f"argument {i + 1} of {node.func.id}() must be {want}")
            args.append(c)
        return template.format(*args), kind


def compile_expression(source: str, ctx: ExprContext, slot: str, expect: str) -> ExprFn:
    """Compile one expression; ``expect`` is "numeric" or "boolean" (§4 type checking)."""
    if not isinstance(source, str) or not source.strip():
        raise CatalogError(f"{ctx.event_id}: expression in {slot} is missing or not a string")
    fn = _Compiler(ctx, source, slot).compile()
    if fn.result != expect:
        raise CatalogError(
            f"{ctx.event_id}: expression in {slot} must be {expect} but is {fn.result}: {source.strip()!r}")
    return fn
