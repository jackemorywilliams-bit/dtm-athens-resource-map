#!/usr/bin/env python3
"""verify.py — the enforcement wall for the DTM Athens Resource Map.

Exits non-zero on any hard fail. Stdlib only. Rules enforced:

  1. Any populated value (contact fields, geo coordinates) with an empty `source`.
  2. `verified: true` on an entry lacking a populated phone OR address.
  3. Missing required fields or wrong field types.
  4. Duplicate ids or duplicate org names.
  5. geo coordinates outside the Athens-Clarke County bounding box.
  6. `lastVerified` older than 12 months (or unparseable).
  7. Categories not from the approved set (or empty).

Prints counts by category and verified-vs-unverified, then PASS/FAIL.
"""

import json
import sys
from datetime import date, datetime
from pathlib import Path

RESOURCES_PATH = Path(__file__).parent / "resources.json"

APPROVED_CATEGORIES = {
    "Food",
    "Housing & Shelter",
    "Counseling & Mental Health",
    "Jobs & Workforce",
    "GED & Adult Education",
    "Addiction Recovery",
    "Healthcare (free/low-cost)",
    "Transportation",
    "Legal Aid",
    "Churches & Volunteer Groups",
    "Youth & Family",
}

# Athens-Clarke County, GA bounding box (slightly padded).
LAT_MIN, LAT_MAX = 33.80, 34.08
LNG_MIN, LNG_MAX = -83.62, -83.18

REQUIRED_FIELDS = [
    "id", "name", "categories", "description", "whatToBring", "warmNextStep",
    "busRoute", "contact", "servesPopulation", "geo", "lastVerified", "verified",
]
CONTACT_FIELDS = ["phone", "address", "hours", "website"]

MAX_AGE_DAYS = 366  # 12 months


def fail_msgs(entries):
    """Yield (entry_label, message) for every hard fail."""
    seen_ids = {}
    seen_names = {}

    for i, e in enumerate(entries):
        label = e.get("id") if isinstance(e, dict) and e.get("id") else f"entry #{i}"

        if not isinstance(e, dict):
            yield label, "entry is not an object"
            continue

        # 3. Required fields present
        for f in REQUIRED_FIELDS:
            if f not in e:
                yield label, f"missing required field '{f}'"

        # 4. Duplicates
        eid = e.get("id")
        if eid:
            if eid in seen_ids:
                yield label, f"duplicate id (also entry #{seen_ids[eid]})"
            seen_ids[eid] = i
        name = (e.get("name") or "").strip().lower()
        if name:
            if name in seen_names:
                yield label, f"duplicate org name (also entry #{seen_names[name]})"
            seen_names[name] = i

        # 7. Categories from approved set, non-empty array
        cats = e.get("categories")
        if not isinstance(cats, list) or not cats:
            yield label, "categories must be a non-empty array"
        else:
            for c in cats:
                if c not in APPROVED_CATEGORIES:
                    yield label, f"category not in approved set: {c!r}"

        # 1. Populated contact values require a source
        contact = e.get("contact")
        phone_ok = addr_ok = False
        if not isinstance(contact, dict):
            yield label, "contact must be an object"
        else:
            for cf in CONTACT_FIELDS:
                pair = contact.get(cf)
                if not isinstance(pair, dict) or "value" not in pair or "source" not in pair:
                    yield label, f"contact.{cf} must be an object with 'value' and 'source'"
                    continue
                value = (pair.get("value") or "").strip()
                source = (pair.get("source") or "").strip()
                if value and not source:
                    yield label, f"contact.{cf} has a value but no source (PROV-1)"
                if source and not value:
                    yield label, f"contact.{cf} has a dangling source but no value"
                if cf == "phone" and value and source:
                    phone_ok = True
                if cf == "address" and value and source:
                    addr_ok = True

        # 1. Populated geo requires a source; 5. bounding box
        geo = e.get("geo")
        if not isinstance(geo, dict):
            yield label, "geo must be an object"
        else:
            lat, lng = geo.get("lat"), geo.get("lng")
            gsource = (geo.get("source") or "").strip()
            if (lat is None) != (lng is None):
                yield label, "geo has only one of lat/lng"
            if lat is not None and lng is not None:
                if not gsource:
                    yield label, "geo has coordinates but no source (PROV-1)"
                if not (isinstance(lat, (int, float)) and isinstance(lng, (int, float))):
                    yield label, "geo lat/lng must be numbers"
                elif not (LAT_MIN <= lat <= LAT_MAX and LNG_MIN <= lng <= LNG_MAX):
                    yield label, (
                        f"geo ({lat}, {lng}) outside Athens-Clarke County bounding box"
                    )
            if lat is None and lng is None and gsource:
                yield label, "geo has a dangling source but no coordinates"

        # 2. verified:true requires sourced phone OR address
        if e.get("verified") is True and not (phone_ok or addr_ok):
            yield label, "verified:true but no sourced phone or address"
        if not isinstance(e.get("verified"), bool):
            yield label, "verified must be true or false"

        # 6. lastVerified parseable and fresh
        lv = e.get("lastVerified")
        try:
            lv_date = datetime.strptime(lv, "%Y-%m-%d").date()
        except (TypeError, ValueError):
            yield label, f"lastVerified is not a YYYY-MM-DD date: {lv!r}"
        else:
            age = (date.today() - lv_date).days
            if age > MAX_AGE_DAYS:
                yield label, f"lastVerified is {age} days old (>12 months)"
            if age < 0:
                yield label, f"lastVerified is in the future: {lv}"


def main():
    try:
        raw = RESOURCES_PATH.read_text(encoding="utf-8")
    except OSError as exc:
        print(f"FAIL: cannot read {RESOURCES_PATH}: {exc}")
        return 1
    try:
        entries = json.loads(raw)
    except json.JSONDecodeError as exc:
        print(f"FAIL: resources.json is not valid JSON: {exc}")
        return 1
    if not isinstance(entries, list):
        print("FAIL: resources.json must be a JSON array of entries")
        return 1

    failures = list(fail_msgs(entries))

    # Counts
    cat_counts = {}
    verified = unverified = 0
    for e in entries:
        if isinstance(e, dict):
            for c in e.get("categories") or []:
                cat_counts[c] = cat_counts.get(c, 0) + 1
            if e.get("verified") is True:
                verified += 1
            else:
                unverified += 1

    print(f"Entries: {len(entries)}")
    print(f"Verified: {verified}  |  Unverified: {unverified}")
    print("By category:")
    for c in sorted(cat_counts):
        print(f"  {c}: {cat_counts[c]}")
    print()

    if failures:
        print(f"HARD FAILS ({len(failures)}):")
        for label, msg in failures:
            print(f"  [{label}] {msg}")
        print("\nverify.py: FAIL")
        return 1

    print("verify.py: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
