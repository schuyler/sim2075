"""RNG discipline (ADR-8; implementation guide §4.6) — contract code shared by both engines.

One ``SeedSequence(master_seed)``; one child per run-block of ``block_size``
runs (so results are invariant to how runs are chunked across processes, as
long as ``block_size`` is held fixed). Within a block, draws happen in this
fixed order with fixed, outcome-independent shapes (``Rb`` = rows in block):

    at init:      t2_offset   [Rb, E_type2]      Type 2 per-run threshold offsets
    each year:    factor      [Rb, K]            standard normals (pre-Cholesky)
                  idio        [Rb, E]            idiosyncratic standard normals
                  res_u       [Rb, E]            resolution uniforms
                  branch_u    [Rb, E]            branch uniforms
                  impact_z    [Rb, n_impact_rows] impact magnitude standard normals
                  dyn_z       [Rb, n_noisy_vars] dynamics noise standard normals

``res_u``/``branch_u`` are drawn for every event (E_resolving == E: every event
resolves to at least the implicit ``default`` outcome), which keeps the shape
outcome-independent. The scalar reference implementation replays a specific
run by generating the full-width block arrays and consuming its own row (§5.2).

``ScriptedDraws`` provides the same interface from hand-written arrays so that
fixture expectations can be computed by hand.
"""
from __future__ import annotations

from dataclasses import dataclass
from typing import Iterator

import numpy as np

YEAR_KEYS = ("factor", "idio", "res_u", "branch_u", "impact_z", "dyn_z")
INIT_KEYS = ("t2_offset",)


@dataclass(frozen=True)
class DrawShapes:
    K: int
    E: int
    E_type2: int
    n_impact_rows: int
    n_noisy_vars: int

    @staticmethod
    def for_catalog(catalog, n_noisy_vars: int) -> "DrawShapes":
        return DrawShapes(K=catalog.n_factors, E=catalog.n_events, E_type2=len(catalog.type2),
                          n_impact_rows=len(catalog.impact_table), n_noisy_vars=n_noisy_vars)

    def init_shape(self, rb: int) -> dict[str, tuple[int, ...]]:
        return {"t2_offset": (rb, self.E_type2)}

    def year_shape(self, rb: int) -> dict[str, tuple[int, ...]]:
        return {"factor": (rb, self.K), "idio": (rb, self.E), "res_u": (rb, self.E),
                "branch_u": (rb, self.E), "impact_z": (rb, self.n_impact_rows), "dyn_z": (rb, self.n_noisy_vars)}


class BlockStream:
    """Draws for one block, delivered strictly in order: ``init`` once, then ``year(0)``, ``year(1)``, ..."""

    def __init__(self, init: dict[str, np.ndarray], years: Iterator[dict[str, np.ndarray]]):
        self.init = init
        self._years = years
        self._next = 0

    def year(self, t: int) -> dict[str, np.ndarray]:
        if t != self._next:
            raise RuntimeError(f"draws must be consumed in order: asked for year {t}, next is {self._next}")
        self._next += 1
        return next(self._years)


class SeededDraws:
    """Production draw source (§4.6)."""

    def __init__(self, master_seed: int, R: int, shapes: DrawShapes, block_size: int = 1024, years: int = 50):
        if R < 1 or block_size < 1:
            raise ValueError("R and block_size must be >= 1")
        self.master_seed = int(master_seed)
        self.R = int(R)
        self.shapes = shapes
        self.block_size = int(block_size)
        self.years = int(years)
        self._ss = np.random.SeedSequence(self.master_seed)
        self._children = self._ss.spawn(self.n_blocks)

    @property
    def n_blocks(self) -> int:
        return (self.R + self.block_size - 1) // self.block_size

    def block_rows(self, b: int) -> tuple[int, int]:
        start = b * self.block_size
        return start, min(start + self.block_size, self.R)

    def block_of(self, r: int) -> tuple[int, int]:
        """(block index, row within block) for global run index ``r``."""
        if not 0 <= r < self.R:
            raise IndexError(r)
        return r // self.block_size, r % self.block_size

    def stream(self, b: int) -> BlockStream:
        start, stop = self.block_rows(b)
        rb = stop - start
        gen = np.random.Generator(np.random.PCG64(self._children[b]))
        init = {k: gen.standard_normal(s) for k, s in self.shapes.init_shape(rb).items()}

        def years():
            for _ in range(self.years):
                ys = self.shapes.year_shape(rb)
                out = {}
                out["factor"] = gen.standard_normal(ys["factor"])
                out["idio"] = gen.standard_normal(ys["idio"])
                out["res_u"] = gen.random(ys["res_u"])
                out["branch_u"] = gen.random(ys["branch_u"])
                out["impact_z"] = gen.standard_normal(ys["impact_z"])
                out["dyn_z"] = gen.standard_normal(ys["dyn_z"])
                yield out

        return BlockStream(init, years())


class ScriptedDraws:
    """Hand-written draws for fixtures: one block holding all ``R`` rows."""

    def __init__(self, init: dict[str, np.ndarray], years: list[dict[str, np.ndarray]], shapes: DrawShapes):
        self.shapes = shapes
        self.init = {k: np.asarray(v, dtype=np.float64) for k, v in init.items()}
        self.years_list = [{k: np.asarray(v, dtype=np.float64) for k, v in y.items()} for y in years]
        self.R = int(self.init["t2_offset"].shape[0])
        self.block_size = self.R
        self.years = len(self.years_list)
        self._check()

    def _check(self):
        for k, s in self.shapes.init_shape(self.R).items():
            if self.init[k].shape != s:
                raise ValueError(f"scripted init draw {k} has shape {self.init[k].shape}, expected {s}")
        for t, y in enumerate(self.years_list):
            for k, s in self.shapes.year_shape(self.R).items():
                if k not in y or y[k].shape != s:
                    raise ValueError(f"scripted year-{t} draw {k} has shape {y.get(k, np.zeros(0)).shape}, expected {s}")

    @property
    def n_blocks(self) -> int:
        return 1

    def block_rows(self, b: int) -> tuple[int, int]:
        return 0, self.R

    def block_of(self, r: int) -> tuple[int, int]:
        return 0, r

    def stream(self, b: int) -> BlockStream:
        return BlockStream(dict(self.init), iter(self.years_list))
