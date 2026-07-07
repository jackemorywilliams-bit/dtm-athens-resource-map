# PROGRESS — DTM Athens Resource Map

## 2026-07-07 — SESSION 1: scaffold

- [x] `.claude/agents/data-researcher.md` — Read, Write, Bash, WebFetch, WebSearch. NF-1 (no facts from memory), PROV-1 (source URL must visibly display the value), real-lookup-only geocoding, warm voice rules, verify.py-before-finish, summary-only reporting.
- [x] `.claude/agents/qa-groundtruth.md` — Read, Bash, WebFetch only (no Write/Edit by construction). QA-1 sampled ground-truth check; sourcing failure IS failure; report-only.
- [x] `.claude/agents/ui-developer.md` — Read, Write, Edit, Bash. FILE-1 (inlined data, no runtime fetch), ARCH-1 (vanilla + Leaflet CDN only), ATTR-1 (OSM attribution), UI-1..4, TONE-1.
- [x] `resources.json` — schema in place (HSDS-compatible naming, per-field `{value, source}` provenance, `categories` array), one `SAMPLE_DELETE_ME` entry.
- [x] `verify.py` — enforcement wall. Proven to catch: sourceless values, out-of-county geo, stale/invalid `lastVerified`, non-approved categories, `verified:true` without sourced phone/address, duplicate ids/names, missing fields, dangling sources. Exit 1 on any hard fail; prints category + verified counts.
- [x] `build.py` — inlines resources.json into index.html at `/*==INJECT_RESOURCES==*/null`, writes `docs/index.html`. Proven to exit non-zero with a clear message on malformed JSON and on a missing marker.
- [x] `index.html` — placeholder with injection marker (ui-developer replaces in Session 2; marker must be preserved).
- [x] `.github/workflows/verify.yml` — runs verify.py + build.py on push/PR; `permissions: contents: read`; no secrets.
- [x] Proof runs: verify.py PASS + build.py OK on sample; both negative proofs recorded above.

**Next:** restart Claude Code so agent definitions load, then run SESSION 2 of the DTM brief.

## Needs human call-down

(none yet)
