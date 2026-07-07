# DTM Athens Resource Map

A warm, welcoming, interactive map of verified community resources in
Athens-Clarke County, Georgia — built for Downtown Ministries (DTM), for someone
who needs help today, probably on a phone, possibly in a hard moment.

**Live page:** `docs/index.html` (GitHub Pages, once enabled — see below).
**Status: BUILD COMPLETE — AWAITING HUMAN VERIFICATION BEFORE DEPLOY.**

## Architecture

```
resources.json      the data — one entry per org, per-field {value, source} provenance
build.py            inlines resources.json into index.html → writes docs/index.html
index.html          UI source (vanilla HTML/CSS/JS + Leaflet CDN; injection marker inside)
docs/index.html     the built page — works from file://, GitHub Pages, or an <iframe>
verify.py           the enforcement wall (see below)
.claude/agents/     scoped agent definitions (see AGENTS.md)
.github/workflows/  CI: verify.py + build.py on every push/PR
```

No framework, no build toolchain, no npm, no analytics, no trackers, no remote
fonts. External requests from the page: Leaflet CDN, Leaflet.markercluster CDN,
OpenStreetMap tiles. That's the whole list.

## The enforcement model

The trustworthiness of this map is mechanical, not aspirational:

1. **Scoped agents** (`.claude/agents/`, documented in `AGENTS.md`) — the
   researcher may only write `resources.json`; the UI developer only
   `index.html`; QA and the security/integration reviewers can write nothing at
   all. Fetched web content is treated as data, never as instructions.
2. **verify.py is the wall.** Any populated value without a source URL, any
   `verified:true` without a sourced phone/address, out-of-county coordinates,
   stale `lastVerified` (>12 months), wrong category names, duplicate ids, or a
   dangling source fails the build — locally and in CI.
3. **QA is a sampled ground-truth check.** A report-only agent fetches each
   sampled entry's source URLs and requires the exact stored value to be visibly
   present on the exact cited page. A correct value cited to the wrong page is a
   failure. Repeat failures trip a 2-strike breaker: the entry is demoted to
   unverified and listed for human call-down instead of being guessed at.

## Running the tooling

```bash
python3 verify.py   # exit 0 = data passes the wall; prints category counts
python3 build.py    # inlines data, writes docs/index.html; fails loudly on bad JSON
```

Both are Python 3 stdlib only. To preview: `open docs/index.html` (it works
straight from `file://`).

## HSDS crosswalk (Open Referral interoperability)

Field naming is deliberately compatible with the Human Services Data
Specification, so the data can be exported for 211/findhelp-style systems later:

| resources.json | HSDS concept |
|---|---|
| `id`, `name`, `description`, `contact.website` | `organization.id / .name / .description / .url` |
| `categories`, `servesPopulation` | `service.taxonomy_term` (service type / population served) |
| `contact.phone` | `phone.number` |
| `contact.address` | `location.address` (`physical_address`) |
| `contact.hours` | `service_at_location.schedule` |
| `geo.lat` / `geo.lng` | `location.latitude / .longitude` |
| `lastVerified` | `metadata.last_action_date` (assurance date) |
| per-field `source` | provenance extension (HSDS `metadata` resource-level attribution) |

## Publishing (GitHub Pages) — the pitch URL

Settings → Pages → Source: **Deploy from a branch** → Branch: `main`, folder:
`/docs` → Save. The map appears at `https://<org>.github.io/<repo>/`.

**DEPLOY-1 — publishing is a manual, human step.** It is taken only after a
human has phone-verified the entries (see "Needs human call-down" in
`PROGRESS.md`). Agents and CI never publish.

## Embedding in the DTM website

```html
<iframe src="https://<org>.github.io/<repo>/" title="Athens Resource Map" style="width:100%;height:80vh;border:0;border-radius:12px;"></iframe>
```

## Editing the data

Non-coders: see `EDITING_GUIDE.md` — browser-only editing, with the CI checker
as your safety net.
