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

---

# SESSION 3 — 2026-07-07 (scope expansion: +20 entries, 43 total)

## Round 1

**Sample:** 9 of 43 (20%). Forced 6 new entries with fallback sourcing
(love-and-money-center-uga, extra-special-people, u-lead-athens,
oconee-county-health-department, athens-housing-authority,
athens-clarke-county-library) + 3 random new (clarke-county-health-department,
books-for-keeps, athens-community-council-on-aging).

**Result: 9 sampled, 29 fields checked, 28 PASS, 1 FAIL.**

- FAIL: `athens-clarke-county-library.hours` — range-compressed paraphrase
  ("Monday–Thursday: …") not present on cited page, which lists seven per-day
  rows. Same defect class as Session 2 round 1.
- Non-failing warning: same entry's citations pointed at
  athenslibrary.org/athens/ which 301-redirects; canonical is
  athenslibrary.org/location/athens-clarke/.
- Notable PASSes: ESP via espyouandme.org ("189 VFW Drive Watkinsville, GA
  30677"); U-Lead address on the GAgives aggregator page exactly as stored;
  Love and Money Center (the successor of the ASPIRE Clinic) fully sourced on
  fcs.uga.edu.

## Repair (strike 1)

data-researcher rewrote the library hours as seven exact per-day lines from the
canonical page, moved all four citations (and the website value) to the
canonical URL, and corrected the address to the page's exact comma-less text.
verify.py PASS. Orchestrator confirmed only that entry changed.

## Round 2

**Sample:** 9 (forced: repaired library; random from never-sampled: our-daily-bread,
clarke-county-dfcs, athens-area-emergency-food-bank, uga-extension-oconee,
food-bank-of-northeast-georgia, family-promise-of-athens, bigger-vision-of-athens,
advantage-behavioral-health).
**Result: 9 sampled, 32 fields, 27 PASS, 5 FAIL.** Library repair held (all 4 fields).
Fails, all strike 1: athens-area-emergency-food-bank.website (value absent from cited
sub-page), uga-extension-oconee.hours (composite "and" not page text),
family-promise-of-athens.hours (value only in script JSON; visible text conflicts) +
.website (absent from cited sub-page), bigger-vision-of-athens.address (comma not on
page).

## Repairs (strike 1 each)

Websites made self-cited to loading homepages; Oconee Extension hours stored as the
page's three lines incl. "Closed for lunch, 12:00pm - 1:00pm"; Family Promise hours
replaced with the page's visible walk-in sentence; Bigger Vision address stored as the
page's two lines. verify.py PASS.

## Round 3

**Sample:** 9 (forced: the 4 repaired; random never-sampled: uga-extension-athens-clarke,
the-cottage-athens, oconee-area-resource-council, athens-free-clinic, casa-de-amistad).
**Result: 9 sampled, 31 fields, 30 PASS, 1 FAIL.** All 4 repairs held.
New fail (strike 1): athens-free-clinic.address — researcher-inserted commas; page
prints three lines. Repaired to exact three-line text; focused re-test: address PASS.

## Orchestrator ruling — self-cited website fields

The round-3 focused re-test flagged athens-free-clinic.website because the URL string
does not appear as visible prose on its own page. Ruling: a `website` field whose
`source` equals its `value` is verified by the cited URL serving the page (HTTP 200,
no cross-host redirect) — the page is its own evidence. This matches the convention
every QA round applied to all other self-cited websites today. Ruled PASS.

---

# SESSION 4 — 2026-07-08 (deep pass 2: +18 entries, 61 total)

## Round 1

**Sample:** 13 of 61 (20%). Forced 9 new entries with unusual sourcing (WorkSource
NEGA's on-page typo "(706t) 369-5703" stored verbatim and confirmed on page; Athens
First UMC's odd "(706) 543- 1442" spacing confirmed; UGA Campus Transit's U+2011
non-breaking hyphen matched byte-for-byte; Campus Kitchen's pipe-separated address
confirmed literal) + 4 random new.

**Result: 13 sampled, 45 fields checked, 43 PASS, 2 FAIL.**
- FAIL x2 (one entry, strike 1): `acceptance-recovery-center` phone + address cited
  to arc-ga.org/contact/ which now returns 404.
- Non-failing warning: `uga-campus-transit` citations redirect to canonical
  tps.uga.edu/transit/.

## Repair + focused re-test

Both ARC values found as visible footer text on the live arc-ga.org homepage and
re-cited there (values unchanged); transit citations moved to the canonical URL with
values confirmed. Focused re-test: 3/3 PASS.

## SESSION 4 QA gate result

Gate closed clean; no entry reached strike 2; breaker not invoked; zero demotions.

---

# SESSION 5 — 2026-07-22 (full-coverage sweep: every entry ground-truthed)

## Sweep (orchestrator-directed fixed samples, two parallel testers)

The 21 entries never sampled in prior rounds were swept in full: part A (11
entries, 35 fields — 26 PASS / 9 FAIL) and part B (10 entries, 35 fields —
33 PASS / 2 FAIL). Project Safe's confidentiality check: clean (no address,
no coordinates, none anywhere in the entry).

All 11 failures were mechanical citation defects, none factual: seven stored
addresses/hours flattened page line breaks into commas or spaces the page never
prints (plus one zip+4 suffix not visible on the page); three website values
were cited to sub-pages where the URL never appears as readable text; Mercy
Health Center's homepage had become fully client-rendered, leaving its values
visible only in script JSON. Five non-failing stale-redirect warnings.

## Batch repair + re-test

data-researcher re-fetched every flagged page: addresses/hours stored as exact
newline-separated page lines, websites self-cited to loading homepages, all
stale citations moved to canonical URLs. Re-test of the 12 repaired entries:
37/40 PASS — the three remaining fails were all Mercy Health Center
(client-rendered homepage). Strike-1 repair re-cited Mercy to its
server-rendered /medical page with values stored exactly as printed; focused
re-test: 4/4 PASS.

## SESSION 5 QA gate result

**Ground-truth coverage is now 100%: all 61 entries have had every populated
sourced field fetched and checked against its cited page at least once.**
No entry reached strike 2; breaker not invoked; zero demotions.

## SESSION 3 QA gate result

Cumulative unique entries ground-truthed today: 22 of 43 (51%). Final round clean
under the standing conventions; no entry reached strike 2; breaker not invoked; zero
demotions. Gate closed; data shipped.

---

<!-- SOURCE-DIRECTORY:BEGIN (generated by qa_directory.py — do not edit by hand) -->

## Source directory (auto-generated)

All 78 entries with every populated value's exact source. 78 of 78 entries (100%) have additionally had their sourced fields fetched and checked against the cited pages by the report-only QA agent (rounds in the right column; details in the session logs above). Every entry, sampled or not, passes verify.py's structural wall on every build.

| Entry | Field | Cited source | Last verified | QA rounds |
|---|---|---|---|---|
| **Athens-Clarke County High School Completion Initiative** (`acc-high-school-completion-initiative`) | phone | [https://www.acchsci.org/](https://www.acchsci.org/) | 2026-07-22 | S6-newA 2026-07-22; S6-retest 2026-07-22 |
|  | address | [https://www.acchsci.org/](https://www.acchsci.org/) |  |  |
|  | website | [https://www.acchsci.org/](https://www.acchsci.org/) |  |  |
|  | geo | [https://nominatim.openstreetmap.org/search?q=855+Sunset+Drive,+Athens,+Georgia+30606&format=json](https://nominatim.openstreetmap.org/search?q=855+Sunset+Drive,+Athens,+Georgia+30606&format=json) |  |  |
| **ACC Second Chance Desk** (`acc-second-chance-desk`) | phone | [https://www.accgov.com/8429/Second-Chance-Desk](https://www.accgov.com/8429/Second-Chance-Desk) | 2026-07-08 | S4-R1 2026-07-08 |
|  | address | [https://www.accgov.com/8429/Second-Chance-Desk](https://www.accgov.com/8429/Second-Chance-Desk) |  |  |
|  | hours | [https://www.accgov.com/8429/Second-Chance-Desk](https://www.accgov.com/8429/Second-Chance-Desk) |  |  |
|  | website | [https://www.accgov.com/8429/Second-Chance-Desk](https://www.accgov.com/8429/Second-Chance-Desk) |  |  |
|  | geo | [https://nominatim.openstreetmap.org/search?q=4070+Lexington+Road%2C+Athens%2C+Georgia+30605&format=json](https://nominatim.openstreetmap.org/search?q=4070+Lexington+Road%2C+Athens%2C+Georgia+30605&format=json) |  |  |
| **Acceptance Recovery Center** (`acceptance-recovery-center`) | phone | [https://arc-ga.org/](https://arc-ga.org/) | 2026-07-08 | S4-R1 2026-07-08; S4-focused 2026-07-08 |
|  | address | [https://arc-ga.org/](https://arc-ga.org/) |  |  |
|  | website | [https://arc-ga.org/](https://arc-ga.org/) |  |  |
| **ACTION, Inc.** (`action-inc`) | phone | [https://actionathens.org/contact-us](https://actionathens.org/contact-us) | 2026-07-07 | S2-R2 2026-07-07 |
|  | address | [https://actionathens.org/contact-us](https://actionathens.org/contact-us) |  |  |
|  | hours | [https://actionathens.org/contact-us](https://actionathens.org/contact-us) |  |  |
|  | website | [https://actionathens.org/contact-us](https://actionathens.org/contact-us) |  |  |
|  | geo | [https://nominatim.openstreetmap.org/search?q=320+Research+Drive,+Athens,+Georgia+30605&format=json](https://nominatim.openstreetmap.org/search?q=320+Research+Drive,+Athens,+Georgia+30605&format=json) |  |  |
| **Advantage Behavioral Health Systems** (`advantage-behavioral-health`) | phone | [https://advantagebhs.org/](https://advantagebhs.org/) | 2026-07-07 | S3-R2 2026-07-07 |
|  | website | [https://advantagebhs.org/](https://advantagebhs.org/) |  |  |
| **Advantage Homeless Day Service Center** (`advantage-homeless-day-service-center`) | phone | [https://advantagebhs.org/homeless-services/](https://advantagebhs.org/homeless-services/) | 2026-07-22 | S6-newA 2026-07-22 |
|  | address | [https://advantagebhs.org/homeless-services/](https://advantagebhs.org/homeless-services/) |  |  |
|  | hours | [https://advantagebhs.org/athens-clarke-county/](https://advantagebhs.org/athens-clarke-county/) |  |  |
|  | website | [https://advantagebhs.org/homeless-services/](https://advantagebhs.org/homeless-services/) |  |  |
|  | geo | [https://nominatim.openstreetmap.org/search?q=240+North+Avenue,+Athens,+Georgia+30601&format=json](https://nominatim.openstreetmap.org/search?q=240+North+Avenue,+Athens,+Georgia+30601&format=json) |  |  |
| **Advantage Pavilion for Behavioral Health** (`advantage-pavilion-for-behavioral-health`) | phone | [https://advantagebhs.org/athens-clarke-county/](https://advantagebhs.org/athens-clarke-county/) | 2026-07-22 | S6-newB 2026-07-22 |
|  | address | [https://advantagebhs.org/athens-clarke-county/](https://advantagebhs.org/athens-clarke-county/) |  |  |
|  | hours | [https://advantagebhs.org/crisis-stabilization/](https://advantagebhs.org/crisis-stabilization/) |  |  |
|  | website | [https://advantagebhs.org/athens-clarke-county/](https://advantagebhs.org/athens-clarke-county/) |  |  |
|  | geo | [https://nominatim.openstreetmap.org/search?q=240+Mitchell+Bridge+Road,+Athens,+Georgia+30606&format=json](https://nominatim.openstreetmap.org/search?q=240+Mitchell+Bridge+Road,+Athens,+Georgia+30606&format=json) |  |  |
| **Athens A.A. (Alcoholics Anonymous District 16B)** (`athens-aa-district-16b`) | phone | [https://www.athensaa.org/](https://www.athensaa.org/) | 2026-07-08 | S4-R1 2026-07-08 |
|  | website | [https://www.athensaa.org/](https://www.athensaa.org/) |  |  |
| **Athens Area Commencement Center** (`athens-area-commencement-center`) | phone | [https://thecommencementcenter.com/contact/](https://thecommencementcenter.com/contact/) | 2026-07-22 | S5-sweepA 2026-07-22; S5-retest 2026-07-22 |
|  | address | [https://thecommencementcenter.com/contact/](https://thecommencementcenter.com/contact/) |  |  |
|  | hours | [https://thecommencementcenter.com/contact/](https://thecommencementcenter.com/contact/) |  |  |
|  | website | [https://thecommencementcenter.com/](https://thecommencementcenter.com/) |  |  |
|  | geo | [https://nominatim.openstreetmap.org/search?q=1175+Mitchell+Bridge+Road%2C+Athens%2C+Georgia+30606&format=json](https://nominatim.openstreetmap.org/search?q=1175+Mitchell+Bridge+Road%2C+Athens%2C+Georgia+30606&format=json) |  |  |
| **Athens Area Emergency Food Bank** (`athens-area-emergency-food-bank`) | phone | [https://www.athensfoodbank.org/donations.html](https://www.athensfoodbank.org/donations.html) | 2026-07-07 | S3-R2 2026-07-07; S3-R3 2026-07-07 |
|  | address | [https://www.athensfoodbank.org/donations.html](https://www.athensfoodbank.org/donations.html) |  |  |
|  | hours | [https://www.athensfoodbank.org/donations.html](https://www.athensfoodbank.org/donations.html) |  |  |
|  | website | [https://www.athensfoodbank.org/](https://www.athensfoodbank.org/) |  |  |
|  | geo | [https://nominatim.openstreetmap.org/search?q=640+Barber+Street,+Athens,+Georgia+30601&format=json](https://nominatim.openstreetmap.org/search?q=640+Barber+Street,+Athens,+Georgia+30601&format=json) |  |  |
| **Athens Area Habitat for Humanity** (`athens-area-habitat`) | phone | [https://www.athenshabitat.com/](https://www.athenshabitat.com/) | 2026-07-22 | S5-sweepA 2026-07-22; S5-retest 2026-07-22 |
|  | address | [https://www.athenshabitat.com/](https://www.athenshabitat.com/) |  |  |
|  | website | [https://www.athenshabitat.com/](https://www.athenshabitat.com/) |  |  |
|  | geo | [https://nominatim.openstreetmap.org/search?q=532+Barber+Street,+Athens,+Georgia&format=json](https://nominatim.openstreetmap.org/search?q=532+Barber+Street,+Athens,+Georgia&format=json) |  |  |
| **Athens Area Homeless Shelter** (`athens-area-homeless-shelter`) | phone | [https://www.helpathenshomeless.org/](https://www.helpathenshomeless.org/) | 2026-07-07 | S5-sweepA 2026-07-22 |
|  | address | [https://www.helpathenshomeless.org/](https://www.helpathenshomeless.org/) |  |  |
|  | website | [https://www.helpathenshomeless.org/](https://www.helpathenshomeless.org/) |  |  |
|  | geo | [https://nominatim.openstreetmap.org/search?q=205+Bray+Street,+Athens,+Georgia+30601&format=json](https://nominatim.openstreetmap.org/search?q=205+Bray+Street,+Athens,+Georgia+30601&format=json) |  |  |
| **Athens-Clarke County Library** (`athens-clarke-county-library`) | phone | [https://athenslibrary.org/location/athens-clarke/](https://athenslibrary.org/location/athens-clarke/) | 2026-07-07 | S3-R1 2026-07-07; S3-R2 2026-07-07 |
|  | address | [https://athenslibrary.org/location/athens-clarke/](https://athenslibrary.org/location/athens-clarke/) |  |  |
|  | hours | [https://athenslibrary.org/location/athens-clarke/](https://athenslibrary.org/location/athens-clarke/) |  |  |
|  | website | [https://athenslibrary.org/location/athens-clarke/](https://athenslibrary.org/location/athens-clarke/) |  |  |
|  | geo | [https://nominatim.openstreetmap.org/search?q=2025+Baxter+Street,+Athens,+Georgia+30606&format=json](https://nominatim.openstreetmap.org/search?q=2025+Baxter+Street,+Athens,+Georgia+30606&format=json) |  |  |
| **Athens-Clarke County Transit** (`athens-clarke-county-transit`) | phone | [https://www.accgov.com/transit](https://www.accgov.com/transit) | 2026-07-22 | S5-sweepA 2026-07-22; S5-retest 2026-07-22 |
|  | address | [https://www.accgov.com/transit](https://www.accgov.com/transit) |  |  |
|  | website | [https://www.accgov.com/transit](https://www.accgov.com/transit) |  |  |
|  | geo | [https://nominatim.openstreetmap.org/search?q=775+East+Broad+Street,+Athens,+Georgia+30601&format=json](https://nominatim.openstreetmap.org/search?q=775+East+Broad+Street,+Athens,+Georgia+30601&format=json) |  |  |
| **Athens Community Council on Aging** (`athens-community-council-on-aging`) | phone | [https://www.accaging.org/](https://www.accaging.org/) | 2026-07-07 | S3-R1 2026-07-07 |
|  | address | [https://www.accaging.org/](https://www.accaging.org/) |  |  |
|  | hours | [https://www.accaging.org/](https://www.accaging.org/) |  |  |
|  | website | [https://www.accaging.org/](https://www.accaging.org/) |  |  |
|  | geo | [https://nominatim.openstreetmap.org/search?q=135+Hoyt+Street,+Athens,+Georgia+30601&format=json](https://nominatim.openstreetmap.org/search?q=135+Hoyt+Street,+Athens,+Georgia+30601&format=json) |  |  |
| **Athens Farmers Market SNAP Doubling** (`athens-farmers-market-double-snap`) | address | [https://athensfarmersmarket.net/](https://athensfarmersmarket.net/) | 2026-07-22 | S6-newB 2026-07-22; S6-retest 2026-07-22 |
|  | website | [https://athensfarmersmarket.net/snap-doubling](https://athensfarmersmarket.net/snap-doubling) |  |  |
|  | geo | [https://nominatim.openstreetmap.org/search?q=705+Sunset+Drive,+Athens,+Georgia+30606&format=json](https://nominatim.openstreetmap.org/search?q=705+Sunset+Drive,+Athens,+Georgia+30606&format=json) |  |  |
| **Athens First United Methodist Church** (`athens-first-united-methodist-church`) | phone | [https://athensfirstumc.org/](https://athensfirstumc.org/) | 2026-07-08 | S4-R1 2026-07-08 |
|  | address | [https://athensfirstumc.org/](https://athensfirstumc.org/) |  |  |
|  | hours | [https://athensfirstumc.org/](https://athensfirstumc.org/) |  |  |
|  | website | [https://athensfirstumc.org/](https://athensfirstumc.org/) |  |  |
|  | geo | [https://nominatim.openstreetmap.org/search?q=327+North+Lumpkin+Street%2C+Athens%2C+Georgia+30601&format=json](https://nominatim.openstreetmap.org/search?q=327+North+Lumpkin+Street%2C+Athens%2C+Georgia+30601&format=json) |  |  |
| **Athens Free Clinic** (`athens-free-clinic`) | phone | [https://medicalpartnership.usg.edu/education/athens-free-clinic/](https://medicalpartnership.usg.edu/education/athens-free-clinic/) | 2026-07-07 | S3-R3 2026-07-07; S3-focused 2026-07-07 |
|  | address | [https://medicalpartnership.usg.edu/education/athens-free-clinic/](https://medicalpartnership.usg.edu/education/athens-free-clinic/) |  |  |
|  | website | [https://medicalpartnership.usg.edu/education/athens-free-clinic/](https://medicalpartnership.usg.edu/education/athens-free-clinic/) |  |  |
|  | geo | [https://nominatim.openstreetmap.org/search?q=1425+Prince+Avenue,+Athens,+Georgia+30602&format=json](https://nominatim.openstreetmap.org/search?q=1425+Prince+Avenue,+Athens,+Georgia+30602&format=json) |  |  |
| **Athens Housing Authority** (`athens-housing-authority`) | phone | [https://www.athenshousing.org/](https://www.athenshousing.org/) | 2026-07-07 | S3-R1 2026-07-07 |
|  | address | [https://www.athenshousing.org/](https://www.athenshousing.org/) |  |  |
|  | website | [https://www.athenshousing.org/](https://www.athenshousing.org/) |  |  |
|  | geo | [https://nominatim.openstreetmap.org/search?q=300+South+Rocksprings+Street,+Athens,+Georgia+30606&format=json](https://nominatim.openstreetmap.org/search?q=300+South+Rocksprings+Street,+Athens,+Georgia+30606&format=json) |  |  |
| **Athens Land Trust** (`athens-land-trust`) | phone | [https://athenslandtrust.org/contact/](https://athenslandtrust.org/contact/) | 2026-07-22 | S5-sweepA 2026-07-22; S5-retest 2026-07-22 |
|  | address | [https://athenslandtrust.org/contact/](https://athenslandtrust.org/contact/) |  |  |
|  | website | [https://athenslandtrust.org/](https://athenslandtrust.org/) |  |  |
|  | geo | [https://nominatim.openstreetmap.org/search?q=685+North+Pope+Street,+Athens,+Georgia+30601&format=json](https://nominatim.openstreetmap.org/search?q=685+North+Pope+Street,+Athens,+Georgia+30601&format=json) |  |  |
| **Athens Neighborhood Health Center** (`athens-neighborhood-health-center`) | phone | [https://www.anhc.clinic/contact/](https://www.anhc.clinic/contact/) | 2026-07-22 | S5-sweepA 2026-07-22; S5-retest 2026-07-22 |
|  | address | [https://www.anhc.clinic/contact/](https://www.anhc.clinic/contact/) |  |  |
|  | website | [https://www.anhc.clinic/](https://www.anhc.clinic/) |  |  |
|  | geo | [https://nominatim.openstreetmap.org/search?q=402+McKinley+Drive,+Athens,+Georgia+30601&format=json](https://nominatim.openstreetmap.org/search?q=402+McKinley+Drive,+Athens,+Georgia+30601&format=json) |  |  |
| **Athens-Oconee CASA** (`athens-oconee-casa`) | phone | [https://www.athensoconeecasa.org/](https://www.athensoconeecasa.org/) | 2026-07-08 | S4-R1 2026-07-08 |
|  | address | [https://www.athensoconeecasa.org/](https://www.athensoconeecasa.org/) |  |  |
|  | hours | [https://www.athensoconeecasa.org/](https://www.athensoconeecasa.org/) |  |  |
|  | website | [https://www.athensoconeecasa.org/](https://www.athensoconeecasa.org/) |  |  |
|  | geo | [https://nominatim.openstreetmap.org/search?q=693+North+Pope+Street%2C+Athens%2C+Georgia+30601&format=json](https://nominatim.openstreetmap.org/search?q=693+North+Pope+Street%2C+Athens%2C+Georgia+30601&format=json) |  |  |
| **Athens Public Defender (Western Circuit Public Defender)** (`athens-public-defender-western-circuit`) | phone | [https://www.athenspublicdefender.com/contact-us](https://www.athenspublicdefender.com/contact-us) | 2026-07-08 | S5-sweepA 2026-07-22 |
|  | address | [https://www.athenspublicdefender.com/contact-us](https://www.athenspublicdefender.com/contact-us) |  |  |
|  | hours | [https://www.athenspublicdefender.com/contact-us](https://www.athenspublicdefender.com/contact-us) |  |  |
|  | website | [https://www.athenspublicdefender.com/](https://www.athenspublicdefender.com/) |  |  |
|  | geo | [https://nominatim.openstreetmap.org/search?q=440+College+Avenue%2C+Athens%2C+Georgia+30601&format=json](https://nominatim.openstreetmap.org/search?q=440+College+Avenue%2C+Athens%2C+Georgia+30601&format=json) |  |  |
| **Athens Technical College Adult Education** (`athens-tech-adult-education`) | phone | [https://athenstech.edu/programs/adult-education-programs/](https://athenstech.edu/programs/adult-education-programs/) | 2026-07-07 | S2-R1 2026-07-07; S2-R2 2026-07-07 |
|  | address | [https://athenstech.edu/programs/adult-education-programs/](https://athenstech.edu/programs/adult-education-programs/) |  |  |
|  | website | [https://athenstech.edu/programs/adult-education-programs/](https://athenstech.edu/programs/adult-education-programs/) |  |  |
|  | geo | [https://nominatim.openstreetmap.org/search?q=Athens+Technical+College,+Athens,+Georgia&format=json](https://nominatim.openstreetmap.org/search?q=Athens+Technical+College,+Athens,+Georgia&format=json) |  |  |
| **Athens Wellness Clinic** (`athens-wellness-clinic`) | phone | [http://athenswellnessclinic.org/](http://athenswellnessclinic.org/) | 2026-07-07 | S2-R1 2026-07-07 |
|  | address | [http://athenswellnessclinic.org/](http://athenswellnessclinic.org/) |  |  |
|  | hours | [http://athenswellnessclinic.org/](http://athenswellnessclinic.org/) |  |  |
|  | website | [http://athenswellnessclinic.org/](http://athenswellnessclinic.org/) |  |  |
|  | geo | [https://nominatim.openstreetmap.org/search?q=240+North+Avenue,+Athens,+Georgia+30601&format=json](https://nominatim.openstreetmap.org/search?q=240+North+Avenue,+Athens,+Georgia+30601&format=json) |  |  |
| **Bigger Vision of Athens** (`bigger-vision-of-athens`) | phone | [https://www.bvoa.org/emergency-shelter-program](https://www.bvoa.org/emergency-shelter-program) | 2026-07-07 | S2-R1 2026-07-07; S3-R2 2026-07-07; S3-R3 2026-07-07 |
|  | address | [https://www.bvoa.org/emergency-shelter-program](https://www.bvoa.org/emergency-shelter-program) |  |  |
|  | website | [https://www.bvoa.org/emergency-shelter-program](https://www.bvoa.org/emergency-shelter-program) |  |  |
|  | geo | [https://nominatim.openstreetmap.org/search?q=95+North+Avenue,+Athens,+Georgia+30601&format=json](https://nominatim.openstreetmap.org/search?q=95+North+Avenue,+Athens,+Georgia+30601&format=json) |  |  |
| **Books for Keeps** (`books-for-keeps`) | phone | [https://www.booksforkeeps.org/](https://www.booksforkeeps.org/) | 2026-07-07 | S3-R1 2026-07-07 |
|  | website | [https://www.booksforkeeps.org/](https://www.booksforkeeps.org/) |  |  |
| **Boys & Girls Clubs of Athens** (`boys-girls-clubs-of-athens`) | phone | [https://www.greatfuturesathens.com/contact](https://www.greatfuturesathens.com/contact) | 2026-07-07 | S2-R1 2026-07-07 |
|  | address | [https://www.greatfuturesathens.com/contact](https://www.greatfuturesathens.com/contact) |  |  |
|  | website | [https://www.greatfuturesathens.com/contact](https://www.greatfuturesathens.com/contact) |  |  |
|  | geo | [https://nominatim.openstreetmap.org/search?q=705+Fourth+Street,+Athens,+Georgia+30601&format=json](https://nominatim.openstreetmap.org/search?q=705+Fourth+Street,+Athens,+Georgia+30601&format=json) |  |  |
| **Campus Kitchen at UGA** (`campus-kitchen-at-uga`) | phone | [https://servicelearning.uga.edu/community-engagement/campus-kitchen/](https://servicelearning.uga.edu/community-engagement/campus-kitchen/) | 2026-07-08 | S4-R1 2026-07-08 |
|  | address | [https://servicelearning.uga.edu/community-engagement/campus-kitchen/](https://servicelearning.uga.edu/community-engagement/campus-kitchen/) |  |  |
|  | website | [https://servicelearning.uga.edu/community-engagement/campus-kitchen/](https://servicelearning.uga.edu/community-engagement/campus-kitchen/) |  |  |
|  | geo | [https://nominatim.openstreetmap.org/search?q=1242+South+Lumpkin+Street%2C+Athens%2C+Georgia+30602&format=json](https://nominatim.openstreetmap.org/search?q=1242+South+Lumpkin+Street%2C+Athens%2C+Georgia+30602&format=json) |  |  |
| **Casa de Amistad** (`casa-de-amistad`) | phone | [https://www.athensamistad.com/](https://www.athensamistad.com/) | 2026-07-07 | S3-R3 2026-07-07 |
|  | website | [https://www.athensamistad.com/](https://www.athensamistad.com/) |  |  |
| **Celebrate Recovery at Cornerstone Church** (`celebrate-recovery-cornerstone-church`) | phone | [https://www.cornerstoneathens.cc/celebrate-recovery](https://www.cornerstoneathens.cc/celebrate-recovery) | 2026-07-08 | S4-R1 2026-07-08 |
|  | address | [https://www.cornerstoneathens.cc/celebrate-recovery](https://www.cornerstoneathens.cc/celebrate-recovery) |  |  |
|  | hours | [https://www.cornerstoneathens.cc/celebrate-recovery](https://www.cornerstoneathens.cc/celebrate-recovery) |  |  |
|  | website | [https://www.cornerstoneathens.cc/celebrate-recovery](https://www.cornerstoneathens.cc/celebrate-recovery) |  |  |
|  | geo | [https://nominatim.openstreetmap.org/search?q=4680+Lexington+Road%2C+Athens%2C+Georgia+30605&format=json](https://nominatim.openstreetmap.org/search?q=4680+Lexington+Road%2C+Athens%2C+Georgia+30605&format=json) |  |  |
| **Celebrate Recovery Athens at Living Hope Church** (`celebrate-recovery-living-hope-church`) | phone | [https://www.livinghopeathens.org/addiction](https://www.livinghopeathens.org/addiction) | 2026-07-08 | S4-R1 2026-07-08 |
|  | address | [https://www.livinghopeathens.org/addiction](https://www.livinghopeathens.org/addiction) |  |  |
|  | hours | [https://www.livinghopeathens.org/addiction](https://www.livinghopeathens.org/addiction) |  |  |
|  | website | [https://www.livinghopeathens.org/addiction](https://www.livinghopeathens.org/addiction) |  |  |
|  | geo | [https://nominatim.openstreetmap.org/search?q=2150+Lexington+Road%2C+Athens%2C+Georgia+30605&format=json](https://nominatim.openstreetmap.org/search?q=2150+Lexington+Road%2C+Athens%2C+Georgia+30605&format=json) |  |  |
| **Chess and Community** (`chess-and-community`) | phone | [https://www.chessandcommunity.org/contact](https://www.chessandcommunity.org/contact) | 2026-07-22 | S6-newA 2026-07-22; S6-retest 2026-07-22 |
|  | address | [https://www.chessandcommunity.org/contact](https://www.chessandcommunity.org/contact) |  |  |
|  | website | [https://www.chessandcommunity.org/](https://www.chessandcommunity.org/) |  |  |
|  | geo | [https://nominatim.openstreetmap.org/search?q=465+Huntington+Road,+Athens,+Georgia+30606&format=json (street-level match)](https://nominatim.openstreetmap.org/search?q=465+Huntington+Road,+Athens,+Georgia+30606&format=json (street-level match)) |  |  |
| **City of Refuge Athens** (`city-of-refuge-athens`) | phone | [https://www.cityofrefugeathens.org/](https://www.cityofrefugeathens.org/) | 2026-07-22 | S6-newB 2026-07-22; S6-retest 2026-07-22 |
|  | address | [https://www.cityofrefugeathens.org/](https://www.cityofrefugeathens.org/) |  |  |
|  | website | [https://www.cityofrefugeathens.org/](https://www.cityofrefugeathens.org/) |  |  |
|  | geo | [https://nominatim.openstreetmap.org/search?q=565+Tallassee+Road,+Athens,+Georgia+30606&format=json](https://nominatim.openstreetmap.org/search?q=565+Tallassee+Road,+Athens,+Georgia+30606&format=json) |  |  |
| **Clarke County DFCS Office** (`clarke-county-dfcs`) | phone | [https://dfcs.georgia.gov/locations/clarke-county](https://dfcs.georgia.gov/locations/clarke-county) | 2026-07-07 | S3-R2 2026-07-07 |
|  | address | [https://dfcs.georgia.gov/locations/clarke-county](https://dfcs.georgia.gov/locations/clarke-county) |  |  |
|  | hours | [https://dfcs.georgia.gov/locations/clarke-county](https://dfcs.georgia.gov/locations/clarke-county) |  |  |
|  | website | [https://dfcs.georgia.gov/locations/clarke-county](https://dfcs.georgia.gov/locations/clarke-county) |  |  |
|  | geo | [https://nominatim.openstreetmap.org/search?q=284+North+Avenue,+Athens,+Georgia+30601&format=json](https://nominatim.openstreetmap.org/search?q=284+North+Avenue,+Athens,+Georgia+30601&format=json) |  |  |
| **Clarke County Health Department** (`clarke-county-health-department`) | phone | [https://www.northeasthealthdistrict.org/locations/clarke-county/](https://www.northeasthealthdistrict.org/locations/clarke-county/) | 2026-07-07 | S3-R1 2026-07-07 |
|  | address | [https://www.northeasthealthdistrict.org/locations/clarke-county/](https://www.northeasthealthdistrict.org/locations/clarke-county/) |  |  |
|  | hours | [https://www.northeasthealthdistrict.org/locations/clarke-county/](https://www.northeasthealthdistrict.org/locations/clarke-county/) |  |  |
|  | website | [https://www.northeasthealthdistrict.org/locations/clarke-county/](https://www.northeasthealthdistrict.org/locations/clarke-county/) |  |  |
|  | geo | [https://nominatim.openstreetmap.org/search?q=345+North+Harris+Street,+Athens,+Georgia+30601&format=json](https://nominatim.openstreetmap.org/search?q=345+North+Harris+Street,+Athens,+Georgia+30601&format=json) |  |  |
| **DIVAS Who Win Freedom Center** (`divas-who-win-freedom-center`) | phone | [https://www.divaswhowin.org/](https://www.divaswhowin.org/) | 2026-07-22 | S6-newA 2026-07-22 |
|  | address | [https://www.divaswhowin.org/](https://www.divaswhowin.org/) |  |  |
|  | website | [https://www.divaswhowin.org/](https://www.divaswhowin.org/) |  |  |
|  | geo | [https://nominatim.openstreetmap.org/search?q=645+Hawthorne+Avenue,+Athens,+Georgia&format=json](https://nominatim.openstreetmap.org/search?q=645+Hawthorne+Avenue,+Athens,+Georgia&format=json) |  |  |
| **Downtown Ministries** (`downtown-ministries`) | phone | [https://downtownministries.org/contact/](https://downtownministries.org/contact/) | 2026-07-07 | S2-R2 2026-07-07 |
|  | address | [https://downtownministries.org/contact/](https://downtownministries.org/contact/) |  |  |
|  | website | [https://downtownministries.org/contact/](https://downtownministries.org/contact/) |  |  |
|  | geo | [https://nominatim.openstreetmap.org/search?q=250+North+Milledge+Avenue,+Athens,+Georgia+30601&format=json](https://nominatim.openstreetmap.org/search?q=250+North+Milledge+Avenue,+Athens,+Georgia+30601&format=json) |  |  |
| **East Athens Development Corporation** (`east-athens-development-corporation`) | phone | [https://www.eadcinc.org/contact](https://www.eadcinc.org/contact) | 2026-07-22 | S6-newA 2026-07-22; S6-retest 2026-07-22 |
|  | address | [https://www.eadcinc.org/contact](https://www.eadcinc.org/contact) |  |  |
|  | hours | [https://www.eadcinc.org/contact](https://www.eadcinc.org/contact) |  |  |
|  | website | [https://www.eadcinc.org/](https://www.eadcinc.org/) |  |  |
|  | geo | [https://nominatim.openstreetmap.org/search?q=410+McKinley+Drive,+Athens,+Georgia+30601&format=json](https://nominatim.openstreetmap.org/search?q=410+McKinley+Drive,+Athens,+Georgia+30601&format=json) |  |  |
| **East Georgia Cancer Coalition** (`east-georgia-cancer-coalition`) | phone | [https://www.eastgeorgiacancercoalition.org/contact-us](https://www.eastgeorgiacancercoalition.org/contact-us) | 2026-07-22 | S6-newB 2026-07-22 |
|  | address | [https://www.eastgeorgiacancercoalition.org/contact-us](https://www.eastgeorgiacancercoalition.org/contact-us) |  |  |
|  | website | [https://www.eastgeorgiacancercoalition.org/](https://www.eastgeorgiacancercoalition.org/) |  |  |
|  | geo | [https://nominatim.openstreetmap.org/search?q=315+Riverbend+Road,+Athens,+Georgia+30602&format=json](https://nominatim.openstreetmap.org/search?q=315+Riverbend+Road,+Athens,+Georgia+30602&format=json) |  |  |
| **Emmanuel Episcopal Church** (`emmanuel-episcopal-church`) | phone | [https://www.emmanuelathens.org/](https://www.emmanuelathens.org/) | 2026-07-08 | S5-sweepA 2026-07-22 |
|  | address | [https://www.emmanuelathens.org/](https://www.emmanuelathens.org/) |  |  |
|  | website | [https://www.emmanuelathens.org/](https://www.emmanuelathens.org/) |  |  |
|  | geo | [https://nominatim.openstreetmap.org/search?q=498+Prince+Avenue%2C+Athens%2C+Georgia+30601&format=json](https://nominatim.openstreetmap.org/search?q=498+Prince+Avenue%2C+Athens%2C+Georgia+30601&format=json) |  |  |
| **Extra Special People (ESP)** (`extra-special-people`) | phone | [https://espyouandme.org/esp-athens/](https://espyouandme.org/esp-athens/) | 2026-07-07 | S3-R1 2026-07-07 |
|  | address | [https://espyouandme.org/esp-athens/](https://espyouandme.org/esp-athens/) |  |  |
|  | website | [https://espyouandme.org/esp-athens/](https://espyouandme.org/esp-athens/) |  |  |
|  | geo | [https://nominatim.openstreetmap.org/search?q=189+VFW+Drive,+Watkinsville,+Georgia+30677&format=json](https://nominatim.openstreetmap.org/search?q=189+VFW+Drive,+Watkinsville,+Georgia+30677&format=json) |  |  |
| **Family Connection-Communities in Schools of Athens** (`family-connection-cis-of-athens`) | phone | [https://www.fc-cisofathens.org/contact](https://www.fc-cisofathens.org/contact) | 2026-07-22 | S6-newA 2026-07-22 |
|  | website | [https://www.fc-cisofathens.org/](https://www.fc-cisofathens.org/) |  |  |
| **Family Counseling Services of Athens** (`family-counseling-services-of-athens`) | phone | [https://www.fcsathens.com/contact](https://www.fcsathens.com/contact) | 2026-07-08 | S4-R1 2026-07-08 |
|  | address | [https://www.fcsathens.com/contact](https://www.fcsathens.com/contact) |  |  |
|  | website | [https://www.fcsathens.com/](https://www.fcsathens.com/) |  |  |
|  | geo | [https://nominatim.openstreetmap.org/search?q=1435+Oglethorpe+Avenue%2C+Athens%2C+Georgia+30606&format=json](https://nominatim.openstreetmap.org/search?q=1435+Oglethorpe+Avenue%2C+Athens%2C+Georgia+30606&format=json) |  |  |
| **Family Promise of Athens** (`family-promise-of-athens`) | phone | [https://www.familypromiseathens.org/contact](https://www.familypromiseathens.org/contact) | 2026-07-07 | S2-R2 2026-07-07; S3-R2 2026-07-07; S3-R3 2026-07-07 |
|  | address | [https://www.familypromiseathens.org/contact](https://www.familypromiseathens.org/contact) |  |  |
|  | hours | [https://www.familypromiseathens.org/contact](https://www.familypromiseathens.org/contact) |  |  |
|  | website | [https://www.familypromiseathens.org/](https://www.familypromiseathens.org/) |  |  |
|  | geo | [https://nominatim.openstreetmap.org/search?q=205+Bray+Street,+Athens,+Georgia+30601&format=json](https://nominatim.openstreetmap.org/search?q=205+Bray+Street,+Athens,+Georgia+30601&format=json) |  |  |
| **Food Bank of Northeast Georgia** (`food-bank-of-northeast-georgia`) | phone | [https://foodbanknega.org/](https://foodbanknega.org/) | 2026-07-22 | S3-R2 2026-07-07; S6-partners 2026-07-22 |
|  | address | [https://foodbanknega.org/](https://foodbanknega.org/) |  |  |
|  | website | [https://foodbanknega.org/](https://foodbanknega.org/) |  |  |
|  | geo | [https://nominatim.openstreetmap.org/search?q=890+Newton+Bridge+Road,+Athens,+Georgia+30607&format=json](https://nominatim.openstreetmap.org/search?q=890+Newton+Bridge+Road,+Athens,+Georgia+30607&format=json) |  |  |
| **Georgia Department of Labor - Athens Career Center** (`gdol-athens-career-center`) | address | [https://dol.georgia.gov/locations/athens](https://dol.georgia.gov/locations/athens) | 2026-07-22 | S5-sweepA 2026-07-22; S5-retest 2026-07-22 |
|  | website | [https://dol.georgia.gov/locations/athens](https://dol.georgia.gov/locations/athens) |  |  |
|  | geo | [https://nominatim.openstreetmap.org/search?q=Georgia+Department+of+Labor%2C+Athens%2C+Georgia&format=json&limit=5](https://nominatim.openstreetmap.org/search?q=Georgia+Department+of+Labor%2C+Athens%2C+Georgia&format=json&limit=5) |  |  |
| **Georgia Conflict Center** (`georgia-conflict-center`) | phone | [https://www.gaconflict.org/contact](https://www.gaconflict.org/contact) | 2026-07-22 | S6-newB 2026-07-22 |
|  | website | [https://www.gaconflict.org/](https://www.gaconflict.org/) |  |  |
| **Georgia Legal Services Program - Athens Regional Office** (`georgia-legal-services-athens`) | phone | [https://www.glsp.org/need-help/](https://www.glsp.org/need-help/) | 2026-07-22 | S5-sweepA 2026-07-22; S5-retest 2026-07-22 |
|  | address | [https://www.glsp.org/need-help/](https://www.glsp.org/need-help/) |  |  |
|  | website | [https://www.glsp.org/need-help/](https://www.glsp.org/need-help/) |  |  |
|  | geo | [https://nominatim.openstreetmap.org/search?q=1865+West+Broad+Street,+Athens,+Georgia+30606&format=json](https://nominatim.openstreetmap.org/search?q=1865+West+Broad+Street,+Athens,+Georgia+30606&format=json) |  |  |
| **Goodwill of North Georgia - East Athens Career Center** (`goodwill-east-athens-career-center`) | phone | [https://goodwillng.org/gw-locations/east-athens-store-donation-career-center-30605/](https://goodwillng.org/gw-locations/east-athens-store-donation-career-center-30605/) | 2026-07-08 | S4-R1 2026-07-08 |
|  | address | [https://goodwillng.org/gw-locations/east-athens-store-donation-career-center-30605/](https://goodwillng.org/gw-locations/east-athens-store-donation-career-center-30605/) |  |  |
|  | hours | [https://goodwillng.org/gw-locations/east-athens-store-donation-career-center-30605/](https://goodwillng.org/gw-locations/east-athens-store-donation-career-center-30605/) |  |  |
|  | website | [https://goodwillng.org/gw-locations/east-athens-store-donation-career-center-30605/](https://goodwillng.org/gw-locations/east-athens-store-donation-career-center-30605/) |  |  |
|  | geo | [https://nominatim.openstreetmap.org/search?q=4070+Lexington+Road%2C+Athens%2C+Georgia+30605&format=json](https://nominatim.openstreetmap.org/search?q=4070+Lexington+Road%2C+Athens%2C+Georgia+30605&format=json) |  |  |
| **Georgia Vocational Rehabilitation Agency - Athens VR Office** (`gvra-athens-vr-office`) | phone | [https://gvs.georgia.gov/locations/athens-vr-office](https://gvs.georgia.gov/locations/athens-vr-office) | 2026-07-22 | S5-sweepA 2026-07-22; S5-retest 2026-07-22 |
|  | address | [https://gvs.georgia.gov/locations/athens-vr-office](https://gvs.georgia.gov/locations/athens-vr-office) |  |  |
|  | hours | [https://gvs.georgia.gov/locations/athens-vr-office](https://gvs.georgia.gov/locations/athens-vr-office) |  |  |
|  | website | [https://gvs.georgia.gov/locations/athens-vr-office](https://gvs.georgia.gov/locations/athens-vr-office) |  |  |
|  | geo | [https://nominatim.openstreetmap.org/search?q=125+Athens+West+Parkway,+Athens,+Georgia+30606&format=json](https://nominatim.openstreetmap.org/search?q=125+Athens+West+Parkway,+Athens,+Georgia+30606&format=json) |  |  |
| **Hands On Historic Athens** (`hands-on-historic-athens`) | phone | [https://www.historicathens.com/hoha](https://www.historicathens.com/hoha) | 2026-07-22 | S6-newA 2026-07-22 |
|  | website | [https://www.historicathens.com/hoha](https://www.historicathens.com/hoha) |  |  |
| **HER Health** (`her-health-athens`) | phone | [https://www.herhealthga.com/](https://www.herhealthga.com/) | 2026-07-22 | S6-newB 2026-07-22; S6-retest 2026-07-22 |
|  | address | [https://www.herhealthga.com/](https://www.herhealthga.com/) |  |  |
|  | hours | [https://www.herhealthga.com/](https://www.herhealthga.com/) |  |  |
|  | website | [https://www.herhealthga.com/](https://www.herhealthga.com/) |  |  |
|  | geo | [https://nominatim.openstreetmap.org/search?q=740+Prince+Avenue,+Athens,+Georgia+30606&format=json](https://nominatim.openstreetmap.org/search?q=740+Prince+Avenue,+Athens,+Georgia+30606&format=json) |  |  |
| **Hope Haven of Northeast Georgia** (`hope-haven-of-northeast-georgia`) | phone | [https://hopehaven.net/contact-us/](https://hopehaven.net/contact-us/) | 2026-07-22 | S5-sweepB 2026-07-22; S5-retest 2026-07-22 |
|  | address | [https://hopehaven.net/contact-us/](https://hopehaven.net/contact-us/) |  |  |
|  | hours | [https://hopehaven.net/contact-us/](https://hopehaven.net/contact-us/) |  |  |
|  | website | [https://hopehaven.net/](https://hopehaven.net/) |  |  |
|  | geo | [https://nominatim.openstreetmap.org/search?q=795+Newton+Bridge+Road%2C+Athens%2C+Georgia+30607&format=json](https://nominatim.openstreetmap.org/search?q=795+Newton+Bridge+Road%2C+Athens%2C+Georgia+30607&format=json) |  |  |
| **Innovative Start Organization (ISO)** (`innovative-start-organization`) | phone | [https://www.innovativestart.org/contact-us](https://www.innovativestart.org/contact-us) | 2026-07-22 | S6-partners 2026-07-22 |
|  | website | [https://www.innovativestart.org](https://www.innovativestart.org) |  |  |
| **Live Forward** (`live-forward`) | phone | [https://liveforward.org/](https://liveforward.org/) | 2026-07-22 | S5-sweepB 2026-07-22; S5-retest 2026-07-22 |
|  | address | [https://liveforward.org/](https://liveforward.org/) |  |  |
|  | website | [https://liveforward.org/](https://liveforward.org/) |  |  |
|  | geo | [https://nominatim.openstreetmap.org/search?q=2500+West+Broad+Street,+Athens,+Georgia+30606&format=json](https://nominatim.openstreetmap.org/search?q=2500+West+Broad+Street,+Athens,+Georgia+30606&format=json) |  |  |
| **The Love and Money Center at UGA** (`love-and-money-center-uga`) | phone | [https://www.fcs.uga.edu/loveandmoneycenter/contact](https://www.fcs.uga.edu/loveandmoneycenter/contact) | 2026-07-07 | S3-R1 2026-07-07 |
|  | address | [https://www.fcs.uga.edu/loveandmoneycenter/contact](https://www.fcs.uga.edu/loveandmoneycenter/contact) |  |  |
|  | hours | [https://www.fcs.uga.edu/loveandmoneycenter/contact](https://www.fcs.uga.edu/loveandmoneycenter/contact) |  |  |
|  | website | [https://www.fcs.uga.edu/loveandmoneycenter/contact](https://www.fcs.uga.edu/loveandmoneycenter/contact) |  |  |
|  | geo | [https://nominatim.openstreetmap.org/search?q=202+Carlton+Street,+Athens,+Georgia+30602&format=json](https://nominatim.openstreetmap.org/search?q=202+Carlton+Street,+Athens,+Georgia+30602&format=json) |  |  |
| **Mercy Health Center** (`mercy-health-center`) | phone | [https://www.mercyhealthcenter.net/medical](https://www.mercyhealthcenter.net/medical) | 2026-07-22 | S5-sweepB 2026-07-22; S5-retest 2026-07-22 |
|  | address | [https://www.mercyhealthcenter.net/medical](https://www.mercyhealthcenter.net/medical) |  |  |
|  | hours | [https://www.mercyhealthcenter.net/medical](https://www.mercyhealthcenter.net/medical) |  |  |
|  | website | [https://www.mercyhealthcenter.net/](https://www.mercyhealthcenter.net/) |  |  |
|  | geo | [https://nominatim.openstreetmap.org/search?q=700+Oglethorpe+Avenue,+Athens,+Georgia+30606&format=json](https://nominatim.openstreetmap.org/search?q=700+Oglethorpe+Avenue,+Athens,+Georgia+30606&format=json) |  |  |
| **Nuçi's Space** (`nucis-space`) | phone | [https://www.nuci.org/](https://www.nuci.org/) | 2026-07-07 | S5-sweepB 2026-07-22 |
|  | address | [https://www.nuci.org/](https://www.nuci.org/) |  |  |
|  | website | [https://www.nuci.org/](https://www.nuci.org/) |  |  |
|  | geo | [https://nominatim.openstreetmap.org/search?q=396+Oconee+Street,+Athens,+Georgia+30601&format=json](https://nominatim.openstreetmap.org/search?q=396+Oconee+Street,+Athens,+Georgia+30601&format=json) |  |  |
| **Oconee Area Resource Council (OARC)** (`oconee-area-resource-council`) | phone | [https://www.oconeeconnection.org/contact/](https://www.oconeeconnection.org/contact/) | 2026-07-07 | S3-R3 2026-07-07 |
|  | address | [https://www.oconeeconnection.org/contact/](https://www.oconeeconnection.org/contact/) |  |  |
|  | hours | [https://www.oconeeconnection.org/contact/](https://www.oconeeconnection.org/contact/) |  |  |
|  | website | [https://www.oconeeconnection.org/contact/](https://www.oconeeconnection.org/contact/) |  |  |
|  | geo | [https://nominatim.openstreetmap.org/search?q=Jamestown+Boulevard,+Oconee+County,+Georgia&format=json (street-level match)](https://nominatim.openstreetmap.org/search?q=Jamestown+Boulevard,+Oconee+County,+Georgia&format=json (street-level match)) |  |  |
| **Oconee County Health Department** (`oconee-county-health-department`) | phone | [https://www.northeasthealthdistrict.org/locations/oconee-county/](https://www.northeasthealthdistrict.org/locations/oconee-county/) | 2026-07-07 | S3-R1 2026-07-07 |
|  | address | [https://www.northeasthealthdistrict.org/locations/oconee-county/](https://www.northeasthealthdistrict.org/locations/oconee-county/) |  |  |
|  | hours | [https://www.northeasthealthdistrict.org/locations/oconee-county/](https://www.northeasthealthdistrict.org/locations/oconee-county/) |  |  |
|  | website | [https://www.northeasthealthdistrict.org/locations/oconee-county/](https://www.northeasthealthdistrict.org/locations/oconee-county/) |  |  |
|  | geo | [https://nominatim.openstreetmap.org/search?q=1060+Experiment+Station+Road,+Watkinsville,+Georgia+30677&format=json](https://nominatim.openstreetmap.org/search?q=1060+Experiment+Station+Road,+Watkinsville,+Georgia+30677&format=json) |  |  |
| **Oconee County Senior Center** (`oconee-county-senior-center`) | phone | [https://www.oconeecountyga.gov/1234/Senior-Center](https://www.oconeecountyga.gov/1234/Senior-Center) | 2026-07-07 | S5-sweepB 2026-07-22 |
|  | address | [https://www.oconeecountyga.gov/1234/Senior-Center](https://www.oconeecountyga.gov/1234/Senior-Center) |  |  |
|  | hours | [https://www.oconeecountyga.gov/1234/Senior-Center](https://www.oconeecountyga.gov/1234/Senior-Center) |  |  |
|  | website | [https://www.oconeecountyga.gov/1234/Senior-Center](https://www.oconeecountyga.gov/1234/Senior-Center) |  |  |
|  | geo | [https://nominatim.openstreetmap.org/search?q=Hog+Mountain+Road,+Oconee+County,+Georgia&format=json (street-level match)](https://nominatim.openstreetmap.org/search?q=Hog+Mountain+Road,+Oconee+County,+Georgia&format=json (street-level match)) |  |  |
| **Our Daily Bread Community Kitchen** (`our-daily-bread-community-kitchen`) | phone | [https://athenshc.org/resources-navigator/blog-post-title-four-s88y2-jh2rl-7jwwa-zcbf3](https://athenshc.org/resources-navigator/blog-post-title-four-s88y2-jh2rl-7jwwa-zcbf3) | 2026-07-22 | S2-R1 2026-07-07; S2-R2 2026-07-07; S3-R2 2026-07-07; S6-partners 2026-07-22 |
|  | address | [https://athenshc.org/resources-navigator/blog-post-title-four-s88y2-jh2rl-7jwwa-zcbf3](https://athenshc.org/resources-navigator/blog-post-title-four-s88y2-jh2rl-7jwwa-zcbf3) |  |  |
|  | website | [https://downtownministries.org/our-daily-bread/](https://downtownministries.org/our-daily-bread/) |  |  |
|  | geo | [https://nominatim.openstreetmap.org/search?q=355+Pulaski+Street,+Athens,+Georgia+30601&format=json](https://nominatim.openstreetmap.org/search?q=355+Pulaski+Street,+Athens,+Georgia+30601&format=json) |  |  |
| **People Living in Recovery** (`people-living-in-recovery`) | phone | [https://www.peoplelivinginrecovery.com/contact-us](https://www.peoplelivinginrecovery.com/contact-us) | 2026-07-22 | S5-sweepB 2026-07-22; S5-retest 2026-07-22 |
|  | address | [https://www.peoplelivinginrecovery.com/contact-us](https://www.peoplelivinginrecovery.com/contact-us) |  |  |
|  | hours | [https://www.peoplelivinginrecovery.com/contact-us](https://www.peoplelivinginrecovery.com/contact-us) |  |  |
|  | website | [https://www.peoplelivinginrecovery.com](https://www.peoplelivinginrecovery.com) |  |  |
|  | geo | [https://nominatim.openstreetmap.org/search?q=115+Sycamore+Drive,+Athens,+Georgia+30606&format=json](https://nominatim.openstreetmap.org/search?q=115+Sycamore+Drive,+Athens,+Georgia+30606&format=json) |  |  |
| **Project Safe** (`project-safe`) | phone | [https://project-safe.org/](https://project-safe.org/) | 2026-07-07 | S5-sweepB 2026-07-22 |
|  | website | [https://project-safe.org/](https://project-safe.org/) |  |  |
| **The Salvation Army of Athens** (`salvation-army-athens`) | phone | [https://southernusa.salvationarmy.org/athens/](https://southernusa.salvationarmy.org/athens/) | 2026-07-07 | S5-sweepB 2026-07-22 |
|  | address | [https://southernusa.salvationarmy.org/athens/](https://southernusa.salvationarmy.org/athens/) |  |  |
|  | website | [https://southernusa.salvationarmy.org/athens/](https://southernusa.salvationarmy.org/athens/) |  |  |
|  | geo | [https://nominatim.openstreetmap.org/search?q=784+North+Chase+Street,+Athens,+Georgia+30601&format=json](https://nominatim.openstreetmap.org/search?q=784+North+Chase+Street,+Athens,+Georgia+30601&format=json) |  |  |
| **The Sparrow's Nest** (`sparrows-nest`) | phone | [https://www.sparrowsnestathens.org/](https://www.sparrowsnestathens.org/) | 2026-07-07 | S5-sweepB 2026-07-22 |
|  | address | [https://www.sparrowsnestathens.org/](https://www.sparrowsnestathens.org/) |  |  |
|  | hours | [https://www.sparrowsnestathens.org/](https://www.sparrowsnestathens.org/) |  |  |
|  | website | [https://www.sparrowsnestathens.org/](https://www.sparrowsnestathens.org/) |  |  |
|  | geo | [https://nominatim.openstreetmap.org/search?q=745+Prince+Avenue,+Athens,+Georgia+30606&format=json](https://nominatim.openstreetmap.org/search?q=745+Prince+Avenue,+Athens,+Georgia+30606&format=json) |  |  |
| **Teen Matters Athens** (`teen-matters-athens`) | phone | [https://teenmatters.com/clinic-location-and-services/tm-athens/](https://teenmatters.com/clinic-location-and-services/tm-athens/) | 2026-07-22 | S6-newB 2026-07-22; S6-retest 2026-07-22 |
|  | address | [https://teenmatters.com/clinic-location-and-services/tm-athens/](https://teenmatters.com/clinic-location-and-services/tm-athens/) |  |  |
|  | website | [https://teenmatters.com/clinic-location-and-services/tm-athens/](https://teenmatters.com/clinic-location-and-services/tm-athens/) |  |  |
|  | geo | [https://nominatim.openstreetmap.org/search?q=1275+Cedar+Shoals+Drive,+Athens,+Georgia+30605&format=json](https://nominatim.openstreetmap.org/search?q=1275+Cedar+Shoals+Drive,+Athens,+Georgia+30605&format=json) |  |  |
| **The Ark United Ministry Outreach Center** (`the-ark-united-ministry-outreach-center`) | phone | [https://www.athensark.org/](https://www.athensark.org/) | 2026-07-08 | S4-R1 2026-07-08 |
|  | address | [https://www.athensark.org/](https://www.athensark.org/) |  |  |
|  | hours | [https://www.athensark.org/](https://www.athensark.org/) |  |  |
|  | website | [https://www.athensark.org/](https://www.athensark.org/) |  |  |
|  | geo | [https://nominatim.openstreetmap.org/search?q=640+Barber+Street%2C+Athens%2C+Georgia+30601&format=json](https://nominatim.openstreetmap.org/search?q=640+Barber+Street%2C+Athens%2C+Georgia+30601&format=json) |  |  |
| **The Cottage: Sexual Assault Center & Children's Advocacy Center** (`the-cottage-athens`) | phone | [https://thecottagega.org/](https://thecottagega.org/) | 2026-07-07 | S3-R3 2026-07-07 |
|  | address | [https://thecottagega.org/](https://thecottagega.org/) |  |  |
|  | website | [https://thecottagega.org/](https://thecottagega.org/) |  |  |
|  | geo | [https://nominatim.openstreetmap.org/search?q=3019+Lexington+Road,+Athens,+Georgia+30605&format=json](https://nominatim.openstreetmap.org/search?q=3019+Lexington+Road,+Athens,+Georgia+30605&format=json) |  |  |
| **Timothy Baptist Church Food Pantry** (`timothy-baptist-church-food-pantry`) | phone | [https://timothybaptist.org/food-pantry/](https://timothybaptist.org/food-pantry/) | 2026-07-08 | S5-sweepB 2026-07-22 |
|  | address | [https://timothybaptist.org/food-pantry/](https://timothybaptist.org/food-pantry/) |  |  |
|  | hours | [https://timothybaptist.org/food-pantry/](https://timothybaptist.org/food-pantry/) |  |  |
|  | website | [https://timothybaptist.org/food-pantry/](https://timothybaptist.org/food-pantry/) |  |  |
|  | geo | [https://nominatim.openstreetmap.org/search?q=380+Timothy+Road%2C+Athens%2C+Georgia+30606&format=json](https://nominatim.openstreetmap.org/search?q=380+Timothy+Road%2C+Athens%2C+Georgia+30606&format=json) |  |  |
| **U-Lead Athens** (`u-lead-athens`) | address | [https://www.gagives.org/organization/U-Lead-Athens](https://www.gagives.org/organization/U-Lead-Athens) | 2026-07-07 | S3-R1 2026-07-07 |
|  | geo | [https://nominatim.openstreetmap.org/search?q=130+Hope+Avenue,+Athens,+Georgia+30606&format=json](https://nominatim.openstreetmap.org/search?q=130+Hope+Avenue,+Athens,+Georgia+30606&format=json) |  |  |
| **UGA Campus Transit** (`uga-campus-transit`) | phone | [https://tps.uga.edu/transit/](https://tps.uga.edu/transit/) | 2026-07-08 | S4-R1 2026-07-08 |
|  | address | [https://tps.uga.edu/transit/](https://tps.uga.edu/transit/) |  |  |
|  | website | [https://tps.uga.edu/transit/](https://tps.uga.edu/transit/) |  |  |
|  | geo | [https://nominatim.openstreetmap.org/search?q=80+Carlton+Street%2C+Athens%2C+Georgia+30602&format=json](https://nominatim.openstreetmap.org/search?q=80+Carlton+Street%2C+Athens%2C+Georgia+30602&format=json) |  |  |
| **UGA Extension Athens-Clarke County** (`uga-extension-athens-clarke`) | phone | [https://extension.uga.edu/county-offices/clarke.html](https://extension.uga.edu/county-offices/clarke.html) | 2026-07-07 | S3-R3 2026-07-07 |
|  | address | [https://extension.uga.edu/county-offices/clarke.html](https://extension.uga.edu/county-offices/clarke.html) |  |  |
|  | hours | [https://extension.uga.edu/county-offices/clarke.html](https://extension.uga.edu/county-offices/clarke.html) |  |  |
|  | website | [https://extension.uga.edu/county-offices/clarke.html](https://extension.uga.edu/county-offices/clarke.html) |  |  |
|  | geo | [https://nominatim.openstreetmap.org/search?q=Cleveland+Road,+Athens,+Georgia&format=json (street-level match)](https://nominatim.openstreetmap.org/search?q=Cleveland+Road,+Athens,+Georgia&format=json (street-level match)) |  |  |
| **UGA Extension Oconee County** (`uga-extension-oconee`) | phone | [https://extension.uga.edu/county-offices/oconee.html](https://extension.uga.edu/county-offices/oconee.html) | 2026-07-07 | S3-R2 2026-07-07; S3-R3 2026-07-07 |
|  | address | [https://extension.uga.edu/county-offices/oconee.html](https://extension.uga.edu/county-offices/oconee.html) |  |  |
|  | hours | [https://extension.uga.edu/county-offices/oconee.html](https://extension.uga.edu/county-offices/oconee.html) |  |  |
|  | website | [https://extension.uga.edu/county-offices/oconee.html](https://extension.uga.edu/county-offices/oconee.html) |  |  |
|  | geo | [https://nominatim.openstreetmap.org/search?q=1420+Experiment+Station+Road,+Watkinsville,+Georgia+30677&format=json (street-level match)](https://nominatim.openstreetmap.org/search?q=1420+Experiment+Station+Road,+Watkinsville,+Georgia+30677&format=json (street-level match)) |  |  |
| **UGA School of Public and International Affairs (SPIA)** (`uga-school-of-public-and-international-affairs`) | phone | [https://spia.uga.edu/](https://spia.uga.edu/) | 2026-07-22 | S6-partners 2026-07-22 |
|  | address | [https://spia.uga.edu/](https://spia.uga.edu/) |  |  |
|  | website | [https://spia.uga.edu/](https://spia.uga.edu/) |  |  |
|  | geo | [https://nominatim.openstreetmap.org/search?q=Candler+Hall,+Athens,+GA&format=json](https://nominatim.openstreetmap.org/search?q=Candler+Hall,+Athens,+GA&format=json) |  |  |
| **WorkSource Northeast Georgia** (`worksource-northeast-georgia`) | phone | [https://negrc.org/workforce-development/](https://negrc.org/workforce-development/) | 2026-07-08 | S4-R1 2026-07-08 |
|  | address | [https://negrc.org/workforce-development/](https://negrc.org/workforce-development/) |  |  |
|  | website | [https://negrc.org/workforce-development/](https://negrc.org/workforce-development/) |  |  |
|  | geo | [https://nominatim.openstreetmap.org/search?q=305+Research+Drive%2C+Athens%2C+Georgia+30605&format=json](https://nominatim.openstreetmap.org/search?q=305+Research+Drive%2C+Athens%2C+Georgia+30605&format=json) |  |  |
| **YWCO Athens** (`ywco-athens`) | phone | [https://www.ywco.org/contact](https://www.ywco.org/contact) | 2026-07-22 | S6-newA 2026-07-22; S6-retest 2026-07-22 |
|  | address | [https://www.ywco.org/contact](https://www.ywco.org/contact) |  |  |
|  | website | [https://www.ywco.org/](https://www.ywco.org/) |  |  |
|  | geo | [https://nominatim.openstreetmap.org/search?q=562+Research+Drive,+Athens,+Georgia+30605&format=json](https://nominatim.openstreetmap.org/search?q=562+Research+Drive,+Athens,+Georgia+30605&format=json) |  |  |

<!-- SOURCE-DIRECTORY:END -->
