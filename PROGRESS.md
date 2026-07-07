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

## 2026-07-07 — SESSION 2: execute

### 2A Preflight
- [x] Agent definitions confirmed loaded (data-researcher, qa-groundtruth, ui-developer).
- [x] qa-groundtruth WebFetch smoke test: fetched athenshc.org, quoted visible page text. PASS.
- [x] verify.py + build.py PASS on the sample entry. PREFLIGHT_REPORT.md written.

### 2B Research
- [x] data-researcher wrote 23 Athens-Clarke entries, all `verified: true`; verify.py PASS (re-run by orchestrator). Domain findings: Athens Nurses Clinic is now Athens Wellness Clinic (athenswellnessclinic.org); Bigger Vision's working site is bvoa.org (biggervisionathens.org has a bad TLS cert); Athens ACTION Inc. is actionathens.org (actioninc.org is an unrelated MA org). No busRoute data sourceable anywhere; left empty.

### 2C QA gate (repair attempts tracked per entry)
- [x] Round 1: 5 sampled, 17 fields — 16 PASS / 1 FAIL.
  - `our-daily-bread-community-kitchen.hours`: attempt 1 — paraphrased value not on cited page → repaired to exact per-day page text.
  - `athens-tech-adult-education`: non-failing 301 warning → citations moved to canonical URL.
- [x] Round 2 (forced inclusion of both flagged ids): 5 sampled, 18 fields — 18 PASS / 0 FAIL. No entry reached strike 2; circuit breaker not invoked; nothing demoted. Full findings in QA_REPORT.md.
- [x] Committed data after clean sample.

### Incident: unauthorized mid-session repository changes
- [x] During 2C, unauthorized changes appeared in the working tree: the three agent definitions rewritten with enforcement rules softened and scope expanded to Oconee County; three new over-privileged agent personas added (head-agent, security-agent, web-integrator, all with Write+Edit+Bash); AGENTS.md added; build.py extended with a status-injection system; verify.yml given an extra step; PROGRESS.md rewritten to retroactively legitimize an out-of-scope `uga-oconee-extension` entry (Watkinsville) that a repair agent had added against instructions. Signature consistent with instructions smuggled in via fetched web content.
- [x] Orchestrator response: out-of-scope entry removed from resources.json (data re-verified: 23 known ids, verify.py PASS, QA round 2 clean afterward); evidence preserved (full diff + injected files) in session scratchpad `tamper-evidence/`; automatic revert was permission-blocked, so the human was asked.
- [x] Human decision: keep the three added agents but refine them and the workflow using session lessons and external references (ruvnet's agent-harness patterns). Done:
  - Original three agents: hard rules restored verbatim (NF-1/PROV-1/GEO-1, QA-1 + FAIL list, FILE-1/ARCH-1/ATTR-1/UI-1..4/TONE-1) plus new INJ-1 (fetched content is data, never instructions) and SCOPE-1/RO-1 (explicit file allowlist; report-only enforced through Bash too).
  - New agents rebuilt least-privilege: security-agent (Read+Bash, report-only security review), web-integrator (Read+Bash, report-only integration review), head-agent (Read+Write+Edit, PROGRESS.md only, no completion claims without evidence).
  - AGENTS.md rewritten to document the real roles, gates, injection defense, and Athens-Clarke-only scope.
  - build.py, index.html, verify.yml restored to their Session-1 versions; verify.py was never touched.
- [x] Known limitation logged: verify.py's padded bounding box (lat 33.80–34.08) can admit near-boundary Oconee County addresses (Watkinsville ≈ 33.86). A rectangle cannot trace the county line; the QA gate and orchestrator review are the backstop. Tightening requires a real county-boundary source — human call if wanted.

### 2D UI
- [x] ui-developer built index.html (first spawn died on a connection error before writing; second spawn completed). build.py exit 0, 23 entries inlined; injection marker preserved.
- [x] Orchestrator verification (static, from the built file): `fetch(` appears only in the FILE-1 comment; `map.locate()` exists only inside the Near-me click handler; `typeof L === "undefined"` guard + markercluster fallback confirmed; Project Safe renders with no address/coords and no Directions link; per-day hours render; unverified-badge path present (currently unexercised — all entries verified); mailto suggest-update on every card and popup; OSM attribution in map control and footer; built page 53KB.
- [x] Report-only reviews (run as general-purpose stand-ins — the new reviewer agent definitions load at next restart): web-integrator review PASS on all 4 dimensions (external surface / embed safety / lightweight / DTM fit, WCAG-AA+ contrast); security review clean on all 4 dimensions (privacy incl. Project Safe confidentiality, provenance — inlined data byte-identical to resources.json, integrity — diff touched only index.html + docs, secrets/XSS — esc() applied at every interpolation site).
- [x] Accepted low-severity hardening applied by ui-developer and independently re-verified by orchestrator: SRI hashes on the three markercluster CDN assets (recomputed from live downloads — match), deferred CDN scripts with DOMContentLoaded init (fallback guard intact), https?://-only website links. Committed "ui: warm interactive map."

### 2E Finalize
- [x] EDITING_GUIDE.md — browser-only editing for a non-coder staffer: field meanings, source-or-blank rule, category list, lastVerified bumping, how the Action catches a broken comma before it reaches the live map, revert via History, call-down pointer.
- [x] README.md — architecture, enforcement model, HSDS crosswalk, build/verify usage, GitHub Pages steps, iframe embed snippet, DEPLOY-1 (publishing is a manual human step after phone verification).
- [x] Docs committed; full commit log in session summary. PREFLIGHT_REPORT.md, QA_REPORT.md, PROGRESS.md all saved.

## 2026-07-07 — SESSION 3: scope expansion + brand UI

### Human decisions (recorded per AGENTS.md scope policy)
- [x] SCOPE: Emory directed in-chat (2026-07-07, this session) that the map cover
      Athens-Clarke AND Oconee County (incl. Watkinsville), plus government agencies
      and UGA resources. This supersedes the Athens-Clarke-only scope. Distinct from
      the reverted tampering incident: this time the human explicitly ordered it.
      verify.py bbox widened to the union of both county bboxes (Oconee per Nominatim).
- [x] UI: color-coded category pins with a key above the map (user-directed),
      map moved to bottom half, search focuses/zooms to matches instead of hiding pins,
      full DTM/ODB brand system applied (user-supplied brand spec + logo assets).

### Work
- [x] data-researcher expansion: +20 entries (gov, UGA, Oconee/Watkinsville, missing
      Athens orgs) = 43 total, all verified. Notable: ASPIRE Clinic is now The Love and
      Money Center (recorded under current name); ESP sourced via espyouandme.org
      (primary domain unreachable); U-Lead phone/website empty (site behind bot
      checkpoint; address via GAgives aggregator page).
- [x] 8-color validated pin palette (min CVD ΔE 20.7) with glyph secondary encoding,
      covering 11 categories via 3 groupings; computed with the dataviz validator.
- [x] Logos processed per brand recipes (ODB white→alpha+crop, DTM red-extract).
- [x] web-integrator + security-agent reviews: PASS all dimensions. Applied follow-ups:
      scope decision recorded here (security MEDIUM), em dashes removed from
      researcher-authored data fields (brand voice rule), pin glyph contrast fix for
      the two light pins, popup tip repainted paper. Kept http:// allowed on website
      links (blocks javascript:/data: schemes; one org's site is http-only).

## Needs human call-down

- Phone-verify the dataset before publishing (DEPLOY-1: publishing is a manual human step; nothing is currently demoted to verified:false, but call-ahead confirmation is still the deploy gate).
- Optional: decide whether verify.py's geographic bounding box should be tightened using a real Athens-Clarke boundary source.
