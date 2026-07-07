#!/usr/bin/env python3
"""build.py — inline resources.json into index.html at the marked injection point.

Reads the source `index.html` (which must contain the marker
`/*==INJECT_RESOURCES==*/null`), replaces the marker with the parsed-and-re-serialized
contents of `resources.json`, and writes the built page to `docs/index.html`.

Exits non-zero with a clear message on malformed JSON or a missing marker.
Stdlib only. Usage: python3 build.py [--json PATH] [--html PATH] [--out PATH]
"""

import argparse
import json
import sys
from pathlib import Path

HERE = Path(__file__).parent
MARKER = "/*==INJECT_RESOURCES==*/null"


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--json", default=str(HERE / "resources.json"))
    ap.add_argument("--html", default=str(HERE / "index.html"))
    ap.add_argument("--out", default=str(HERE / "docs" / "index.html"))
    args = ap.parse_args()

    json_path, html_path, out_path = Path(args.json), Path(args.html), Path(args.out)

    try:
        raw = json_path.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"build.py: FAIL — cannot read {json_path}: {exc}")
        return 1

    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        print(f"build.py: FAIL — {json_path} is malformed JSON: "
              f"line {exc.lineno}, column {exc.colno}: {exc.msg}")
        return 1

    if not isinstance(data, list):
        print(f"build.py: FAIL — {json_path} must be a JSON array of entries")
        return 1

    try:
        html = html_path.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"build.py: FAIL — cannot read {html_path}: {exc}")
        return 1

    if MARKER not in html:
        print(f"build.py: FAIL — injection marker {MARKER!r} not found in {html_path}. "
              f"The source index.html must keep the marker intact.")
        return 1

    # </script>-safe serialization so inlined data can never close the script tag.
    payload = json.dumps(data, ensure_ascii=False).replace("</", "<\\/")
    built = html.replace(MARKER, payload)

    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(built, encoding="utf-8")
    print(f"build.py: OK — inlined {len(data)} entries into {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
