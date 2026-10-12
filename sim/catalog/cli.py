"""``python -m sim.catalog.cli <events_dir>`` — compile every migrated event and report.

Exit status is non-zero when any migrated event fails to compile. Unmigrated
files (no ``id`` block) are listed, not failed: the data track owns them.
"""
from __future__ import annotations

import sys
from pathlib import Path

from .compile import compile_event_records
from .extract import extract_all
from .omega import load_omega
from .state_catalog import load_state_catalog
from .types import CatalogError


def main(argv: list[str] | None = None) -> int:
    argv = sys.argv[1:] if argv is None else argv
    events_dir = Path(argv[0]) if argv else Path("events")
    sc = load_state_catalog()
    _, omega = load_omega(factors=sc.factors)
    records, known, unmigrated = extract_all(events_dir)
    failed = 0
    print(f"{len(known)} event files; {len(records)} migrated; {len(unmigrated)} unmigrated")
    for rec in records:
        try:
            cat = compile_event_records([rec], omega, sc, known_event_ids=known, strict_cascades=False)
            dropped = len(cat.meta["warnings"])
            print(f"  OK    {rec['id']:<32} {len(cat.impact_table):>4} impact rows, achieved variance "
                  f"{cat.meta['achieved_variance'][0]:.4f} (declared {cat.meta['declared_variance'][0]:.2f}), "
                  f"{dropped} cascade edge(s) to unmigrated events")
            for note in cat.meta["notes"]:
                print(f"        {note}")
        except CatalogError as e:
            failed += 1
            print(f"  FAIL  {rec['id']:<32} {e}")
    for p in unmigrated:
        print(f"  --    {p} (unmigrated)")
    print(f"{len(records) - failed}/{len(records)} migrated events compile")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
