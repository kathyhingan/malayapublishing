# Malaya Publishing — Website

Static marketing site for Malaya Publishing. 16 HTML pages + one shared stylesheet. No build step, no framework. Deploys as-is to GitHub Pages, Cloudflare Pages, or Netlify.

---

## Rule #1: keep all files flat, together

Every page links to `malaya.css` and to other pages by plain filename (`href="about.html"`). So **all 17 files must sit in the same folder** (repo root is easiest). Do not split them into subfolders, or the styles and links break.

```
/ (repo root)
├── index.html            ← homepage
├── malaya.css            ← shared stylesheet (edit once, all pages update)
├── about.html
├── services.html
├── ai-automation.html
├── lead-generation.html
├── seo-ai-visibility.html
├── social-media.html
├── podcast.html
├── local-businesses.html
├── ecommerce.html
├── professional-services.html
├── diy-courses.html
├── done-with-you.html
├── done-for-you.html
├── fractional-cmo.html   ← walled-off fCMO page (not in main nav)
└── contact.html
```

---

## Deploy (quick version)

1. Put all files above in a GitHub repo (root level, flat).
2. Connect the repo to **Cloudflare Pages** or **Netlify** (both free, one-click from GitHub). Framework preset: **None / static HTML**. Build command: none. Output dir: `/` (root).
3. You get a test URL. Check pages load, popups open, links work.
4. **Keep the old WordPress site running.** Only point `malayapublishing.com` at the new host after testing.
5. No redirect map needed — the old site has no SEO equity; content starts fresh here.

---

## The ONLY thing left to make it fully live: 3 form embeds

All buttons and links are already wired. The three lead-capture forms are CRM embeds that get pasted in when ready. Search each file for `PASTE` to find the exact spot.

| What | Where to paste | Which file |
|---|---|---|
| **Audit form** (from "Start My Free Growth Audit" popup) | `<div id="malaya-audit-slot">` | in every page (shared modal) — edit once per page or via find/replace |
| **Waitlist form** (from course "Join the Waitlist" popup) | `<div id="malaya-waitlist-slot">` | in every page (shared modal) |
| **Contact form** (inline on the contact page) | `<div id="contact-form-slot">` | `contact.html` only |

**Audit vs waitlist are two separate forms**, so leads never get mixed. The waitlist buttons also carry a `data-source` (`waitlist-customgpt` / `waitlist-gbp`) so you can tell which course a lead wanted.

Until the embeds are pasted, those three forms show a "form loads here" placeholder. Everything else works.

---

## Links already wired (live on launch)

- **Habit Hero** → members.bestbusinesscoach.ca sales page
- **fCMO "Request a Fit Call"** → go.oncehub.com/Strategy-Session-Discovery
- **Take the Quiz** → quiz.bestbusinesscoach.ca (interim; rebuild native later)

---

## Still to add after launch (none block going live)

- Real logo (replaces the CSS placeholder mark in header/footer)
- Real photos (About page has 3 photo slots; segment/service pages can take photos)
- Trust-strip logos + permission to name Gerber, NeuroGym, Eram, Axis, Sugar Gliders, Luxury Tours
- Contact details on `contact.html` (Messenger, Viber, email, phone, address — marked placeholders)
- Results / case-study hub (deliberately deferred — building each study properly)
- Native quiz (replace the interim BBC link)
- Favicon, Open Graph tags, sitemap.xml, robots.txt, schema markup (SEO/AEO)

See `LAUNCH_READINESS.md` (kept outside the repo) for the full punch-list.

---

## Editing tips

- **Change a color, font, or button style:** edit `malaya.css` once — every page updates.
- **Change the popup headline/subtext:** it's in the `<script>` block near the bottom of each page (the `COPY` object).
- **Palette:** green `#0F8A4D` (freedom + money), deep green `#14532D`, sand `#F7F3E8`, gold `#F5A623` (CTAs), teal `#0EA5A5`, ink `#2B2118`.
