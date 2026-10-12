"""Pull ```yaml blocks out of events/**/*.md and merge them into one record per file (ADR-7 step 1)."""
from __future__ import annotations

import re
from pathlib import Path

import yaml

from .types import CatalogError

_FENCE = re.compile(r"^```yaml[ \t]*\n(.*?)^```[ \t]*$", re.M | re.S)


def event_id_from_filename(path: str | Path) -> str:
    """``korean-peninsula-crisis.md`` -> ``KOREAN_PENINSULA_CRISIS``; ``Oil Supply Shock.md`` -> ``OIL_SUPPLY_SHOCK``."""
    stem = Path(path).stem
    return re.sub(r"[^A-Za-z0-9]+", "_", stem).strip("_").upper()


def list_event_files(events_dir: str | Path) -> list[Path]:
    """Every event markdown file under the domain subdirectories (planning docs at the top level excluded)."""
    root = Path(events_dir)
    return sorted(p for p in root.glob("*/*.md"))


def extract_record(path: str | Path) -> dict | None:
    """Merge the file's YAML blocks into one dict. Returns None when the file has no ``id`` block (unmigrated)."""
    path = Path(path)
    text = path.read_text(encoding="utf-8")
    record: dict = {}
    problems: list[str] = []
    for m in _FENCE.finditer(text):
        try:
            block = yaml.safe_load(m.group(1))
        except yaml.YAMLError as e:
            problems.append(f"YAML block does not parse: {e}")
            continue
        if block is None:
            continue
        if not isinstance(block, dict):
            problems.append("YAML block is not a mapping")
            continue
        for k, v in block.items():
            if k in record:
                problems.append(f"key {k!r} appears in more than one YAML block")
            record[k] = v
    if "id" not in record:
        # Unmigrated file (legacy partial blocks are common); nothing to compile.
        return None
    if problems:
        raise CatalogError(f"{path}: " + "; ".join(problems))
    record["_source"] = str(path)
    return record


def extract_all(events_dir: str | Path) -> tuple[list[dict], list[str], list[Path]]:
    """Returns (migrated records, all known event IDs by filename, unmigrated paths)."""
    records, known, unmigrated = [], [], []
    for p in list_event_files(events_dir):
        known.append(event_id_from_filename(p))
        r = extract_record(p)
        if r is None:
            unmigrated.append(p)
        else:
            records.append(r)
    return records, known, unmigrated
