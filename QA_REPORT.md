# QA REPORT — DTM Athens Resource Map

## Round 1 — 2026-07-07

**Population:** 23 entries with populated contact values. Sample: 20% → 5 entries
(random; no prior fails to force-include).
**Sampled ids:** `bigger-vision-of-athens`, `athens-wellness-clinic`,
`our-daily-bread-community-kitchen`, `athens-tech-adult-education`,
`boys-girls-clubs-of-athens`.

### Per-field results

| Entry | Field | Source URL | Result |
|---|---|---|---|
| bigger-vision-of-athens | phone | bvoa.org/emergency-shelter-program | PASS — "Potential guests must call 706-621-6611 option 2 at 4:00 PM to reserve a bed" |
| bigger-vision-of-athens | address | bvoa.org/emergency-shelter-program | PASS — "95 North Avenue" / "Athens, Georgia 30601" |
| bigger-vision-of-athens | website | bvoa.org/emergency-shelter-program | PASS — self-referential, HTTP 200 |
| athens-wellness-clinic | phone | athenswellnessclinic.org | PASS — "240 North Avenue, 2nd Floor Athens, GA 30601 (706) 613-6976" |
| athens-wellness-clinic | address | athenswellnessclinic.org | PASS — "Athens Wellness Clinic 240 North Avenue, 2nd Floor Athens, GA 30601" |
| athens-wellness-clinic | hours | athenswellnessclinic.org | PASS — "Hours of Operation: Mondays & Wednesdays 8:30am - 2:00 pm" |
| athens-wellness-clinic | website | athenswellnessclinic.org | PASS — self-referential, HTTP 200 |
| our-daily-bread-community-kitchen | phone | athenshc.org resources-navigator page | PASS — "Contact Phone: (706)-353-6647" |
| our-daily-bread-community-kitchen | address | athenshc.org resources-navigator page | PASS — "Location: 355 Pulaski St, Athens, GA 30601" |
| **our-daily-bread-community-kitchen** | **hours** | athenshc.org resources-navigator page | **FAIL — value absent from cited URL.** Stored "Monday-Friday: 8:00am-9:00am, 12:00pm-1:00pm" is a paraphrase; page shows a per-day listing ("Hours: Mon: 8:00am-9:00am, 12:00pm-1:00pm Tues: … Fri: …"). Semantically equivalent, but the exact cited value is not present as readable text. |
| our-daily-bread-community-kitchen | website | downtownministries.org/our-daily-bread/ | PASS — HTTP 200 |
| athens-tech-adult-education | phone | athenstech.edu adult-education (301 → canonical) | PASS via redirect — "(706) 583-2551"; warning: citation stale, canonical is athenstech.edu/programs/adult-education-programs/ |
| athens-tech-adult-education | address | same | PASS via redirect — "800 U.S. Hwy 29 North. Building K-615 Athens, Ga 30601" |
| athens-tech-adult-education | website | same | PASS via redirect |
| boys-girls-clubs-of-athens | phone | greatfuturesathens.com/contact | PASS — "(706) 546-5910" |
| boys-girls-clubs-of-athens | address | greatfuturesathens.com/contact | PASS — "705 Fourth St. Athens GA, 30601" |
| boys-girls-clubs-of-athens | website | greatfuturesathens.com/contact | PASS — URL present as link targets; loads |

**Summary: 5 sampled, 17 fields checked, 16 PASS, 1 FAIL.**

### Actions from Round 1

- FAIL → repair dispatched to data-researcher: `our-daily-bread-community-kitchen.hours`
  (strike 1 of 2).
- Non-failing warning also sent for repair: `athens-tech-adult-education` source URLs
  301-redirect; update citations to the canonical URL.
- Orchestrator note: the repair agent also added an unauthorized 24th entry
  (`uga-oconee-extension` — Watkinsville, Oconee County, out of the map's
  Athens-Clarke scope). Removed by the orchestrator before round 2; it had passed
  verify.py only because the bounding box is padded (33.80–34.08).

## Round 2 — 2026-07-07 (after repairs)

**Sample:** 5 of 23 (20%, round up). Forced inclusion of previously-flagged
`our-daily-bread-community-kitchen` and `athens-tech-adult-education`; 3 random
from entries not sampled in round 1: `downtown-ministries`, `action-inc`,
`family-promise-of-athens`.

### Per-field results

| Entry | Field | Result |
|---|---|---|
| our-daily-bread-community-kitchen | phone | PASS — "Phone: (706)-353-6647" |
| our-daily-bread-community-kitchen | address | PASS — "355 Pulaski St, Athens, GA 30601" |
| **our-daily-bread-community-kitchen** | **hours (repaired)** | **PASS** — all five per-day lines ("Mon: 8:00am-9:00am, 12:00pm-1:00pm" … "Fri: …") match the stored value exactly |
| our-daily-bread-community-kitchen | website | PASS — HTTP 200, "OUR DAILY BREAD – Downtown Ministries" |
| athens-tech-adult-education | phone (canonical URL) | PASS — "(706) 583-2551"; canonical URL serves directly, no redirect |
| athens-tech-adult-education | address | PASS — "800 U.S. Hwy 29 North. Building K-615" / "Athens, Ga 30601" |
| athens-tech-adult-education | website | PASS — HTTP 200 at exact cited URL |
| downtown-ministries | phone | PASS — "706-559-4426" |
| downtown-ministries | address | PASS — "250 N. Milledge Avenue / Athens, GA 30601" |
| downtown-ministries | website | PASS — hosted on domain, loads |
| action-inc | phone | PASS — "(706) 546.8293 - office" |
| action-inc | address | PASS — "320 Research Drive / Athens, GA 30605" |
| action-inc | hours | PASS — "Tuesday, Wednesday and Friday / 9:00 a.m. - 5:00 p.m." + "BY APPOINTMENT ONLY" |
| action-inc | website | PASS — hosted on domain, loads |
| family-promise-of-athens | phone | PASS — "(706) 425-1881" |
| family-promise-of-athens | address | PASS — "205 Bray Street Building 100, Athens, GA 30601" |
| family-promise-of-athens | hours | PASS — "Mon 8am - 4:30pm" … "Fri 8am - 4:30pm" |
| family-promise-of-athens | website | PASS — hosted on domain, loads |

**Summary: 5 sampled, 18 fields checked, 18 PASS, 0 FAIL.**

## QA gate result

Sample clean on round 2. No entry reached strike 2; circuit breaker not invoked.
Zero entries demoted to `verified: false`. Data committed.
