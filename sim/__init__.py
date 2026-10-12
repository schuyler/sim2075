"""sim2075 — compile layer, reference engine, and (later stages) the vectorized engine.

Layout follows methodology/reference/simulator-architecture.md §2:

    sim/catalog/    compile layer: markdown YAML -> CompiledCatalog
    sim/reference/  scalar reference implementation (ADR-1 oracle + narrator)
    sim/engine/     vectorized runtime (stages E3+; not yet built)
    sim/analysis/   output analysis (stage E9; not yet built)
    sim/data/       state catalog, Ω, and (data track) initial conditions
    sim/tests/      fixtures and gates per implementation-guide §5
"""
