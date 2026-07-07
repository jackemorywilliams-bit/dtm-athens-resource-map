# Editing Guide — for DTM staff (no coding needed)

This guide is for keeping the resource map up to date. You'll edit one file,
`resources.json`, right in your web browser. You cannot break the live map by
mistake — a robot checker catches errors before they ever reach the public page.

## How to edit

1. Open the repository on GitHub and click `resources.json`.
2. Click the pencil icon (✏️, top right of the file view) to edit in the browser.
3. Make your change (see field meanings below).
4. Scroll down, write a one-line note about what you changed (e.g. "updated Mercy
   Health hours"), and click **Commit changes**.

That's it. GitHub runs the checker automatically on every save.

## What the fields mean

Each resource looks like this (shortened):

```json
{
  "id": "mercy-health-center",
  "name": "Mercy Health Center",
  "categories": ["Healthcare (free/low-cost)", "Counseling & Mental Health"],
  "description": "Warm 1-2 sentence description.",
  "whatToBring": "What someone should bring, if anything.",
  "warmNextStep": "The human first move: 'Call and say…'",
  "busRoute": "",
  "contact": {
    "phone":   { "value": "706-425-9445", "source": "https://…" },
    "address": { "value": "700 Oglethorpe Ave…", "source": "https://…" },
    "hours":   { "value": "Monday–Thursday 8:30am–4:30pm…", "source": "https://…" },
    "website": { "value": "https://…", "source": "https://…" }
  },
  "servesPopulation": ["Uninsured adults"],
  "geo": { "lat": 33.96, "lng": -83.41, "source": "https://…" },
  "lastVerified": "2026-07-07",
  "verified": true
}
```

The rules that keep the map trustworthy:

- **Every `value` needs a `source`** — the web page where that exact fact is
  visibly written. If you can't point to a page, leave both `value` and `source`
  as empty quotes (`""`). An honest blank beats a guess.
- **`categories` is a list** and must use only these names, spelled exactly:
  Food · Housing & Shelter · Counseling & Mental Health · Jobs & Workforce ·
  GED & Adult Education · Addiction Recovery · Healthcare (free/low-cost) ·
  Transportation · Legal Aid · Churches & Volunteer Groups · Youth & Family
- **`verified` is `true` only if** the entry has a sourced phone or address.
- **When you touch an entry, update `lastVerified`** to today's date
  (format: `2026-07-07`). Entries older than 12 months fail the checker on
  purpose — it's a nudge to re-confirm.
- **Confidential locations stay confidential.** Project Safe's shelter address is
  never entered anywhere, even if you know it.

## The robot checker (what "the Action" does)

Every time anyone saves a change, GitHub automatically runs `verify.py`. It
catches a missing comma or bracket, a value without a source, a wrong category
name, an out-of-county location, or a stale date — and shows a red ✗ on the
commit. **A red ✗ means the live map was NOT updated** — the broken change stays
quarantined until fixed. Click the ✗ to read what's wrong, then edit the file
again. A green ✓ means all checks passed.

## If something goes wrong

You can always undo. On the `resources.json` page click **History**, open the
last good version, and copy it back over the file (pencil → paste → commit).
Nothing is ever lost — every version is kept forever.

## Needs human call-down

`PROGRESS.md` has a section at the bottom called **Needs human call-down** — a
list of entries the robots could not fully confirm. Those need a human to call
the organization, confirm the facts, and update the entry (bumping
`lastVerified`). Check it now and then.
