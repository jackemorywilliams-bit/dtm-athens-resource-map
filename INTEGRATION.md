# Putting the map on the DTM website

The simplest possible guide, written against the two architectures as they
actually are.

## The two architectures, side by side

| | DTM website | This map |
|---|---|---|
| Platform | WordPress (WPBakery Page Builder) on BigScoots hosting | One self-contained HTML file, no server code at all |
| How pages are made | Staff edit pages in the WordPress admin; PHP builds each page | GitHub rebuilds `docs/index.html` automatically on every data edit |
| Where it lives | downtownministries.org | https://jackemorywilliams-bit.github.io/dtm-athens-resource-map/ |
| What it needs to run | PHP, database, theme, plugins | Nothing: it is already running, for free, on GitHub Pages |

Because the map is a complete, already-hosted page, the WordPress site never
has to run it, store it, or understand it. It only has to show it, the same
way it would show a YouTube video: with an embed. That is the whole
integration.

**Why not paste the map's code into WordPress instead?** Then every data
update would need a second manual paste, WPBakery would fight the map's CSS,
and a WordPress theme update could break it. The embed keeps one source of
truth: edit `resources.json` here, and the copy inside the DTM site updates
itself within a couple of minutes, with the verify.py safety wall still in
front of every change.

## The integration (10 minutes, no plugins)

1. Log in to the WordPress admin at downtownministries.org.
2. Pages → **Add New**. Title it "Athens Resource Map" (the URL becomes
   `/athens-resource-map/`).
3. On the WPBakery editor, add a **Raw HTML** element (if the page opens in
   the standard block editor instead, use a **Custom HTML** block — same
   thing) and paste:

   ```html
   <iframe
     src="https://jackemorywilliams-bit.github.io/dtm-athens-resource-map/"
     title="Athens Area Resource Map"
     allow="geolocation"
     style="width:100%; height:85vh; border:0; border-radius:12px;"
     loading="lazy"></iframe>
   ```

4. Publish, then add the page to the site menu: Appearance → **Menus** →
   check "Athens Resource Map" → Add to Menu → drag into place → Save.

That is the entire integration. Notes on the two attributes that matter:

- `allow="geolocation"` — without it the map's "Near me" button cannot ask
  for location from inside an iframe (it fails politely, but it will never
  work).
- `height:85vh` — the map fills most of the screen. Use a WPBakery full-width
  row and the page will feel native.

## Optional polish (later, not required)

- **DTM-branded address.** The map can live at a DTM subdomain such as
  `resources.downtownministries.org`: add a CNAME record for `resources`
  pointing to `jackemorywilliams-bit.github.io` at the domain registrar, and
  set the same custom domain in this repo's Settings → Pages. The embed src
  then changes to the new address. Cosmetic only — everything works without it.
- **Move the repo to a DTM-owned GitHub account** so ownership does not sit
  with a personal account. Transferring changes the github.io URL (one-line
  edit to the embed), which is another argument for doing the subdomain first.

## Who maintains what, after integration

- **Map content** (add an org, fix a phone number): edited in this repo per
  `EDITING_GUIDE.md` — in the browser, no code. The embedded copy on the DTM
  site updates automatically. WordPress is never touched.
- **The WordPress page**: set it up once and forget it. Theme changes,
  plugin updates, and redesigns cannot break the map, because the map is not
  made of WordPress parts.
- The map page stays live even if the WordPress site is down, at its
  github.io address.
