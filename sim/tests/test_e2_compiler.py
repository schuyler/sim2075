"""E2 gate: compiles the migrated events (FIX-C ground truth) and rejects each broken variant by event ID."""
from pathlib import Path

import numpy as np
import pytest

from sim.catalog import (CatalogError, compile_catalog, load_omega, load_state_catalog)
from sim.catalog.compile import compile_event_records
from sim.catalog.expr import ExprContext, compile_expression
from sim.catalog.extract import event_id_from_filename, extract_all, extract_record
from sim.catalog.types import (DUR_DECAY, DUR_PERMANENT, DUR_UNTIL_RESOLVED, ENTITY_GLOBAL,
                               ONSET_GRADUAL, ONSET_IMMEDIATE)
from sim.tests.fixtures import fix_c

REPO = fix_c.REPO
BROKEN = Path(__file__).parent / "fixtures" / "broken"


@pytest.fixture(scope="module")
def world():
    sc = load_state_catalog()
    _, omega = load_omega(factors=sc.factors)
    _, known, _ = extract_all(REPO / "events")
    return sc, omega, known


# ---------------------------------------------------------------- FIX-C ----
def test_fix_c_compiles_to_hand_built_structure(world):
    sc, omega, known = world
    cat = compile_catalog([fix_c.TAIWAN, fix_c.AMOC], omega, sc, known_event_ids=known, strict_cascades=False)
    assert cat.event_ids == ["TAIWAN_CONFLICT", "AMOC_WEAKENING"]
    assert cat.causal_type.tolist() == [3, 2]
    assert np.isnan(cat.p_annual).all()
    fi = cat.index.factor
    for f, v in fix_c.TAIWAN_LOADINGS.items():
        assert cat.lam[0, fi[f]] == v
    for f, v in fix_c.AMOC_LOADINGS.items():
        assert cat.lam[1, fi[f]] == v
    assert np.count_nonzero(cat.lam[0]) == 4 and np.count_nonzero(cat.lam[1]) == 5
    np.testing.assert_allclose(cat.meta["achieved_variance"], [fix_c.TAIWAN_VARIANCE, fix_c.AMOC_VARIANCE], atol=5e-5)
    np.testing.assert_allclose(cat.sigma_idio, np.sqrt(1 - np.array([fix_c.TAIWAN_VARIANCE, fix_c.AMOC_VARIANCE])), atol=5e-5)

    t3 = cat.type3[0]
    assert len(t3.preconditions) == 4 and len(t3.sustained) == 1 and t3.sustained[0][1] == 2
    assert (t3.window, t3.resolution) == (0.03, 0.65)
    t2 = cat.type2[1]
    assert (t2.threshold, t2.threshold_std, t2.sharpness, t2.floor) == (65, 15, 0.15, 0.002)
    ns = {"_shape": (1,), **{k: np.array([v]) for k, v in fix_c.AMOC_BASELINE_NS.items()}}
    assert t2.pressure(ns)[0] == pytest.approx(fix_c.AMOC_PRESSURE_AT_BASELINE)
    # the compiler's own pressure-scale check evaluated the same thing from state_catalog.yaml's baselines
    assert cat.meta["pressure_at_baseline"]["AMOC_WEAKENING"] == pytest.approx(fix_c.AMOC_PRESSURE_AT_BASELINE)
    assert sc.baseline_2025["global_temp_anomaly"] == 1.3

    tree = cat.resolution_tree[0]
    r_ids, r_p, b_ids, b_p = fix_c.TAIWAN_TREE
    assert tree.resolution_ids == r_ids and tree.resolution_p.tolist() == r_p
    assert tree.branch_ids == b_ids and [x.tolist() for x in tree.branch_p] == b_p
    assert cat.resolution_tree[1].resolution_ids == ["default"] and cat.resolution_tree[1].branch_ids == [["default"]]

    tab = cat.impact_table
    assert len(tab) == fix_c.N_ROWS_TAIWAN + fix_c.N_ROWS_AMOC
    assert (tab["event"] == 0).sum() == fix_c.N_ROWS_TAIWAN
    gv, cv, en = cat.index.global_var, cat.index.country_var, cat.index.entity
    lim = tab[(tab["event"] == 0) & (tab["res_code"] == 0) & (tab["branch_code"] == 0)]
    semi = lim[lim["var_idx"] == gv["semiconductor_supply"]]
    assert len(semi) == 1 and semi["entity_idx"][0] == ENTITY_GLOBAL
    assert (semi["mean"][0], semi["std"][0], semi["onset_kind"][0], semi["dur_kind"][0], semi["dur_param"][0]) == (-0.70, 0.15, ONSET_IMMEDIATE, DUR_DECAY, 2)
    inv = tab[(tab["event"] == 0) & (tab["res_code"] == 0) & (tab["branch_code"] == 1)]
    semi_inv = inv[inv["var_idx"] == gv["semiconductor_supply"]]
    assert semi_inv["mean"][0] == pytest.approx(-0.70 * 1.5) and semi_inv["std"][0] == pytest.approx(0.15 * 1.5)
    nuc = tab[(tab["event"] == 0) & (tab["res_code"] == 0) & (tab["branch_code"] == 2)]
    assert nuc[nuc["var_idx"] == gv["semiconductor_supply"]]["mean"][0] == pytest.approx(-0.70 * 3.0)
    twn_conf = lim[(lim["entity_idx"] == en["twn"]) & (lim["var_idx"] == cv["external_conflict_involvement"])]
    assert twn_conf["dur_kind"][0] == DUR_UNTIL_RESOLVED and twn_conf["mean"][0] == 4
    sanc = lim[(lim["entity_idx"] == en["chn"]) & (lim["var_idx"] == cv["sanctions_level"])]
    assert sanc["dur_kind"][0] == DUR_PERMANENT
    unst = tab[(tab["event"] == 0) & (tab["res_code"] == 1) & (tab["branch_code"] == 1)]
    assert len(unst) == 3 and unst[unst["var_idx"] == gv["global_credit_spread"]]["mean"][0] == pytest.approx(-25.0)
    amoc = tab[(tab["event"] == 1) & (tab["var_idx"] == gv["amoc_strength"]) & (tab["entity_idx"] == ENTITY_GLOBAL)]
    assert (amoc["onset_kind"][0], amoc["onset_years"][0], amoc["dur_kind"][0]) == (ONSET_GRADUAL, 5, DUR_PERMANENT)
    gbr = tab[(tab["event"] == 1) & (tab["entity_idx"] == en["gbr"]) & (tab["var_idx"] == cv["gdp_real"])]
    assert (gbr["onset_years"][0], gbr["dur_kind"][0], gbr["dur_param"][0]) == (15, DUR_DECAY, 25)
    # units (schema §Impact Fields): gdp_real rows are fractions of current value, everything else additive
    assert tab["multiplicative"].sum() == fix_c.N_MULTIPLICATIVE_ROWS
    assert (tab["multiplicative"] == (tab["var_idx"] == cv["gdp_real"]) & (tab["entity_idx"] != ENTITY_GLOBAL)).all()
    # Taiwan's nuclear branch scales twn.gdp_real -0.40 by 3.0 to -1.2: compiles, with a loud note (README §4)
    assert any("WARNING" in n and "twn.gdp_real mean -1.2" in n for n in cat.meta["notes"])

    assert cat.resolves_after.tolist() == fix_c.RESOLVES_AFTER and cat.resolves_after.dtype == np.int64

    assert cat.cascade_edges == []
    assert len(cat.meta["warnings"]) == fix_c.N_DROPPED_EDGES
    assert all("not compiled (unmigrated)" in w for w in cat.meta["warnings"])


def test_pressure_scale_check_is_skipped_loudly_without_baselines(world):
    """Country variables carry no baseline_2025 in the state catalog, so a pressure reading them cannot be
    checked; the compiler records the skip in meta['notes'] rather than passing silently."""
    from sim.catalog.compile import check_pressure_scale
    from sim.catalog.types import Type2Spec
    sc, _, _ = world
    ctx = ExprContext(sc, "T2_SKIP")
    spec = Type2Spec(compile_expression("100 * (pak.water_stress / 100)", ctx, "pressure", "numeric"), 70, 10, 0.2, 0.003)
    value, note = check_pressure_scale(spec, sc, "T2_SKIP")
    assert value is None and "skipped" in note and "pak.water_stress" in note
    spec = Type2Spec(compile_expression("100 * (global_temp_anomaly / 2.0)", ctx, "pressure", "numeric"), 65, 15, 0.15, 0.002)
    assert check_pressure_scale(spec, sc, "T2_OK")[0] == pytest.approx(65.0)
    spec = Type2Spec(compile_expression("global_temp_anomaly / 2.0", ctx, "pressure", "numeric"), 65, 15, 0.15, 0.002)
    with pytest.raises(CatalogError, match="T2_BAD: Type 2 pressure at the 2025 baselines is 0.65"):
        check_pressure_scale(spec, sc, "T2_BAD")


def test_strict_cascades_rejects_unmigrated_targets(world):
    sc, omega, known = world
    with pytest.raises(CatalogError, match="TAIWAN_CONFLICT: cascade target 'KOREAN_PENINSULA_CRISIS'"):
        compile_catalog([fix_c.TAIWAN, fix_c.AMOC], omega, sc, known_event_ids=known, strict_cascades=True)


# ------------------------------------------------------- broken variants ----
@pytest.mark.parametrize("name,needle", [
    ("unknown_variable", "unknown country variable 'not_a_variable'"),
    ("bad_enum", "domain must be one of"),
    ("branch_psum", "probabilities sum to 0.900000"),
    ("banned_ast", "disallowed construct IfExp"),
    ("undeclared_resolution", "undeclared resolution name 'nope'"),
    ("pressure_scale", "pressure at the 2025 baselines is 0.325, outside [5, 125]"),
    ("missing_resolves_after", "has an 'until: resolved' impact row but no probability.resolves_after"),
])
def test_broken_variant_rejected_with_event_id(world, name, needle):
    sc, omega, known = world
    path = BROKEN / f"{name}.md"
    eid = event_id_from_filename(path).replace("_", "_")
    with pytest.raises(CatalogError) as ei:
        compile_catalog([path], omega, sc, known_event_ids=known, strict_cascades=False)
    msg = str(ei.value)
    assert f"BROKEN_{name.upper()}" in msg, msg
    assert needle in msg, msg


# ------------------------------------------ catalog-wide migration status ----
def test_known_event_ids_cover_the_catalog(world):
    _, _, known = world
    assert len(known) == 29
    assert "OIL_SUPPLY_SHOCK" in known and "US_CHINA_ECONOMIC_RUPTURE" in known


@pytest.mark.parametrize("stem", [
    "geopolitical/taiwan-conflict", "climate/amoc-weakening",
    # data-track step D1 (2026-10-12) remediated the three Task 4.2 "needs remediation" events
    "geopolitical/pakistan-state-failure", "health/severe-pandemic", "breakthrough/fusion-commercialization",
])
def test_completed_migrations_compile(world, stem):
    sc, omega, known = world
    compile_catalog([REPO / "events" / f"{stem}.md"], omega, sc, known_event_ids=known, strict_cascades=False)


def test_every_migrated_event_compiles(world):
    """The data-track gate (guide §2): every file under events/ with an id block compiles. Unmigrated files are
    listed, not failed. Mirrors `python -m sim.catalog.cli events`, which CI runs as a blocking step."""
    from sim.catalog import compile_events_dir
    sc, omega, _ = world
    cat = compile_events_dir(REPO / "events", omega, sc, strict_cascades=False)
    assert len(cat.event_ids) + len(cat.meta["unmigrated"]) == 29


# ------------------------------------------------------- expression unit ----
@pytest.fixture(scope="module")
def ctx(world):
    sc, _, _ = world
    return ExprContext(sc, "EXPR_TEST", {"war": 0, "peace": 1}, {"limited": 0, "stable": 1}, set())


def _ns(**kw):
    return {"_shape": (3,), **{k: np.asarray(v, dtype=np.float64) for k, v in kw.items()}}


def test_boolean_rewrite_and_chained_compare(ctx):
    f = compile_expression("F_GPT > 1.0 and not (0 < chn.gdp_real < 2) or oil_brent == 75", ctx, "t", "boolean")
    assert set(f.names) == {"F_GPT", "chn.gdp_real", "oil_brent"}
    out = f(_ns(F_GPT=[2, 2, 0], **{"chn.gdp_real": [1, 5, 1]}, oil_brent=[0, 0, 75]))
    assert out.tolist() == [False, True, True]


def test_numeric_functions_and_where(ctx):
    f = compile_expression("where(F_GPT > 0, min(F_GPT, 1.0), max(F_GPT, -1.0)) + abs(oil_brent) ** 2 / 4", ctx, "t", "numeric")
    out = f(_ns(F_GPT=[0.5, 3, -4], oil_brent=[2, 2, 2]))
    np.testing.assert_allclose(out, [1.5, 2.0, 0.0])


def test_constant_expression_broadcasts(ctx):
    assert compile_expression("1.5", ctx, "t", "numeric")({"_shape": (4,)}).shape == (4,)


def test_categorical_equality(ctx):
    f = compile_expression("resolution == 'peace' or branch != 'limited'", ctx, "t", "boolean")
    assert f(_ns(resolution=[1, 0, 0], branch=[0, 0, 1])).tolist() == [True, False, True]


@pytest.mark.parametrize("src,needle", [
    ("F_GPT if True else 0", "IfExp"),
    ("lambda: 1", "Lambda"),
    ("[x for x in (1,)]", "ListComp"),
    ("F_GPT[0]", "Subscript"),
    ("chn.gdp_real.foo", "attribute access beyond"),
    ("len(F_GPT)", "non-whitelisted function 'len'"),
    ("'abc'", "string literal outside categorical"),
    ("resolution > 'war'", "must be == or !="),
    ("resolution == 'nope'", "undeclared resolution name"),
    ("F_NOPE > 1", "unknown name 'F_NOPE'"),
    ("gdp_real > 1", "is a country variable; write entity.gdp_real"),
    ("zzz.gdp_real > 1", "unknown entity 'zzz'"),
    ("chn.nope > 1", "unknown country variable 'nope'"),
    ("F_GPT and F_FIN", "non-boolean operand"),
    ("(F_GPT > 1) + 1", "arithmetic '+' on boolean"),
    ("min(F_GPT)", "takes exactly 2"),
    ("1 +", "does not parse"),
])
def test_rejections(ctx, src, needle):
    with pytest.raises(CatalogError, match="EXPR_TEST") as ei:
        compile_expression(src, ctx, "slot", "boolean" if ">" in src or "==" in src or "and" in src else "numeric")
    assert needle in str(ei.value), str(ei.value)


def test_result_type_is_checked(ctx):
    with pytest.raises(CatalogError, match="must be boolean but is numeric"):
        compile_expression("F_GPT + 1", ctx, "preconditions", "boolean")
    with pytest.raises(CatalogError, match="must be numeric but is boolean"):
        compile_expression("F_GPT > 1", ctx, "pressure", "numeric")
