# Hey Subrat Personal Brand Website Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build a polished, responsive, accessible static personal-brand website for Subrat Mishra that is ready for Cloudflare Pages.

**Architecture:** A single semantic HTML document contains all content and progressive-enhancement hooks. One stylesheet owns the design system, layouts, responsive states, CSS artwork, and motion preferences; one dependency-free script owns the mobile menu, current year, and optional entrance reveals. Local SVG placeholders keep favicon and Open Graph paths valid without external image dependencies.

**Tech Stack:** HTML5, modern CSS, vanilla JavaScript, SVG, Node.js syntax checks, Python static HTTP server, browser responsive inspection

**Spec:** `docs/superpowers/specs/2026-09-11-heysubrat-personal-brand-design.md`

## Global Constraints

- Use only semantic HTML5, modern CSS, minimal vanilla JavaScript, and local SVG assets.
- Do not add a framework, build process, external UI library, backend, external font, or external image dependency.
- Cloudflare Pages build command remains blank and output directory is exactly `public`.
- The site must remain coherent and navigable without JavaScript.
- Use a dark charcoal background, warm off-white text, and one energetic orange accent.
- Include explicit replacement comments for biography, profile photograph, YouTube URL, Instagram URL, email address, current activities, content cards, and Open Graph image.
- Preserve the existing untracked `.DS_Store` and any unrelated user work.

---

### Task 1: Semantic Page, Metadata, and Content

**Files:**
- Create: `public/index.html`

**Interfaces:**
- Produces: IDs `about`, `interests`, `logs`, and `connect`; mobile navigation controls using `data-menu-toggle` and `data-menu`; current-year target using `data-current-year`; reveal targets using `data-reveal`.
- Consumes: Future local assets at `images/favicon.svg` and `images/og-image-placeholder.svg`; stylesheet at `styles.css`; script at `script.js`.

- [ ] **Step 1: Run a failing structure check**

Run:

```bash
node -e "const fs=require('fs');const p='public/index.html';if(!fs.existsSync(p))throw new Error('public/index.html missing')"
```

Expected: FAIL with `public/index.html missing`.

- [ ] **Step 2: Create the semantic document**

Create `public/index.html` with:

- `<!doctype html>`, English language, UTF-8, responsive viewport, canonical URL, SEO title and description.
- Open Graph title, description, URL, type, and the commented placeholder image path `https://heysubrat.com/images/og-image-placeholder.svg`.
- Local favicon, stylesheet, and deferred script references.
- A skip link and semantic `header`, labelled `nav`, `main`, sections, articles, `address`, and `footer`.
- Header links to `#about`, `#interests`, `#logs`, and `#connect`; an accessible button with `aria-controls="site-menu"`, `aria-expanded="false"`, and `data-menu-toggle`.
- Hero copy and CTAs exactly matching the approved content direction.
- Current chapter rows for Building, Lifting, Running, and Experimenting.
- Six interests and three explicitly marked sample life logs with category/platform metadata.
- About philosophy and a profile placeholder.
- YouTube placeholder link, Instagram `https://www.instagram.com/heysubrat/`, and visible `mailto:hello@heysubrat.com` link.
- A `<noscript>`-safe year value of `2026` inside the `data-current-year` element.
- Explicit `REPLACE:` comments for all eight placeholder categories in the spec.

- [ ] **Step 3: Run structural and content assertions**

Run:

```bash
node -e "const h=require('fs').readFileSync('public/index.html','utf8');const req=['<header','<nav','<main','<footer','id=\"about\"','id=\"interests\"','id=\"logs\"','id=\"connect\"','Hey, I’m Subrat.','Software engineer · Curious human','hello@heysubrat.com','data-menu-toggle','data-current-year'];for(const s of req)if(!h.includes(s))throw new Error('missing '+s);const h1=(h.match(/<h1\b/g)||[]).length;if(h1!==1)throw new Error('expected one h1, got '+h1);console.log('HTML structure OK')"
```

Expected: `HTML structure OK`.

- [ ] **Step 4: Verify replacement comments**

Run:

```bash
node -e "const h=require('fs').readFileSync('public/index.html','utf8').toLowerCase();for(const s of ['biography','profile photograph','youtube url','instagram url','email address','current activities','content cards','open graph image'])if(!h.includes('replace: '+s))throw new Error('missing replacement comment: '+s);console.log('Replacement comments OK')"
```

Expected: `Replacement comments OK`.

- [ ] **Step 5: Commit the page structure**

```bash
git add public/index.html
git commit -m "feat: add Hey Subrat page content"
```

### Task 2: Editorial Visual System and Responsive Layout

**Files:**
- Create: `public/styles.css`
- Modify: `public/index.html`

**Interfaces:**
- Consumes: Semantic classes and data attributes from `public/index.html`.
- Produces: CSS custom-property design system, CSS-only hero portrait, responsive grids, mobile-menu presentation, focus states, no-script menu fallback, and reduced-motion behavior.

- [ ] **Step 1: Run failing style-contract checks**

Run:

```bash
node -e "const fs=require('fs');const p='public/styles.css';if(!fs.existsSync(p))throw new Error('public/styles.css missing')"
```

Expected: FAIL with `public/styles.css missing`.

- [ ] **Step 2: Build the design system and base layout**

Create `public/styles.css` with custom properties grouped under `:root` for:

- Charcoal canvas and elevated surface colors.
- Warm off-white primary text and muted text.
- One orange accent plus a darker accessible accent-hover state.
- System display/body/monospace-label stacks.
- Fluid type sizes using `clamp()`.
- Spacing scale, radii, one-pixel rules, content width, and transition duration.

Add reset and global rules for `box-sizing`, responsive media, body overflow prevention, legible line heights, smooth anchor scrolling, a visible skip link, and orange-offset `:focus-visible` outlines.

- [ ] **Step 3: Implement the responsive editorial composition**

Style:

- A compact sticky header with a wordmark and transform-based menu icon.
- An asymmetrical desktop hero and stacked mobile hero.
- A CSS-only abstract portrait using nested circles/blocks, index labels, a warm accent disc, and restrained grid lines; mark the artwork decorative in HTML.
- Current chapter as a ruled status ledger rather than generic cards.
- Interest cards as a connected numbered collection with varying spans on large screens.
- Life-log cards with editorial thumbnails made from CSS shapes and typography.
- About and connect sections as high-contrast, spacious compositions.
- Hover movement of at most four pixels and no continuous decorative animation.
- Breakpoints near 48rem and 70rem, plus specific protection for narrow phones around 24rem.

- [ ] **Step 4: Add no-JavaScript and motion safety**

Use an early HTML class switch:

```html
<script>document.documentElement.classList.replace('no-js', 'js');</script>
```

Keep desktop navigation visible by default; only collapse it under the `.js` class at mobile widths. Under `@media (prefers-reduced-motion: reduce)`, disable smooth scrolling, reveal transforms, and nonessential transitions.

- [ ] **Step 5: Run CSS contract checks**

Run:

```bash
node -e "const c=require('fs').readFileSync('public/styles.css','utf8');for(const s of [':root','--color-accent','box-sizing: border-box','focus-visible','prefers-reduced-motion','overflow-x','@media','clamp('])if(!c.includes(s))throw new Error('missing CSS contract: '+s);console.log('CSS contracts OK')"
```

Expected: `CSS contracts OK`.

- [ ] **Step 6: Commit the visual system**

```bash
git add public/index.html public/styles.css
git commit -m "feat: add responsive field-journal design"
```

### Task 3: Progressive Enhancement and Local Assets

**Files:**
- Create: `public/script.js`
- Create: `public/images/favicon.svg`
- Create: `public/images/og-image-placeholder.svg`

**Interfaces:**
- Consumes: `[data-menu-toggle]`, `[data-menu]`, `[data-current-year]`, and `[data-reveal]` from `public/index.html`.
- Produces: Synchronized mobile menu state, Escape and navigation-link closure, automatic year, motion-aware intersection reveals, and valid local metadata image targets.

- [ ] **Step 1: Run failing asset checks**

Run:

```bash
node -e "const fs=require('fs');for(const p of ['public/script.js','public/images/favicon.svg','public/images/og-image-placeholder.svg'])if(!fs.existsSync(p))throw new Error('missing '+p)"
```

Expected: FAIL naming the first missing asset.

- [ ] **Step 2: Implement defensive progressive enhancement**

Create `public/script.js` in an IIFE with strict mode. Query each optional target before using it. Implement:

```js
const setMenuState = (open) => {
  toggle.setAttribute('aria-expanded', String(open));
  menu.dataset.open = String(open);
};
```

Toggle from the button, close on menu-link activation, close on Escape while returning focus to the button, and close when resizing above the mobile breakpoint. Set the year with `new Date().getFullYear()`. Only use `IntersectionObserver` when it exists and `prefers-reduced-motion: reduce` does not match; otherwise reveal items immediately.

- [ ] **Step 3: Create local SVG placeholders**

Create:

- A square `favicon.svg` using the dark background, orange accent, and a legible `H` mark.
- A 1200×630 `og-image-placeholder.svg` using the same palette with “Hey Subrat”, “Software engineer · Curious human”, and restrained field-journal linework.

Both SVG files must have explicit `viewBox` attributes and no remote references, embedded raster data, scripts, or animation.

- [ ] **Step 4: Validate JavaScript and asset references**

Run:

```bash
node --check public/script.js
```

Expected: exit code 0 with no output.

Run:

```bash
node -e "const fs=require('fs');const h=fs.readFileSync('public/index.html','utf8');for(const p of ['styles.css','script.js','images/favicon.svg','images/og-image-placeholder.svg']){if(!h.includes(p))throw new Error('HTML does not reference '+p);if(!fs.existsSync('public/'+p))throw new Error('missing public/'+p)}console.log('Local assets OK')"
```

Expected: `Local assets OK`.

- [ ] **Step 5: Commit enhancement and assets**

```bash
git add public/script.js public/images/favicon.svg public/images/og-image-placeholder.svg
git commit -m "feat: add navigation enhancement and local brand assets"
```

### Task 4: Editing Guide and Cloudflare Pages Instructions

**Files:**
- Create: `README.md`

**Interfaces:**
- Consumes: Final `public/` layout and replacement comments.
- Produces: Exact local-preview, editing, placeholder, and deployment guidance.

- [ ] **Step 1: Run a failing documentation check**

Run:

```bash
node -e "const fs=require('fs');if(!fs.existsSync('README.md'))throw new Error('README.md missing')"
```

Expected: FAIL with `README.md missing`.

- [ ] **Step 2: Write the README**

Document:

- Local preview using `python3 -m http.server 8000 --directory public`, then `http://localhost:8000`.
- `public/index.html` for copy, links, metadata, and section structure.
- `public/styles.css` for colors, typography, spacing, layout, and responsive behavior.
- `public/script.js` for menu, year, and reveal behavior.
- `public/images/` for favicon, Open Graph art, and future profile imagery.
- Searching `public/index.html` for `REPLACE:` comments to update every placeholder.
- Cloudflare Pages: connect the repository, leave Framework preset as None, leave Build command blank, set Build output directory to `public`, and deploy.
- The visible email is provisional and should not be published unchanged if that mailbox is inactive.

- [ ] **Step 3: Validate deployment guidance**

Run:

```bash
node -e "const r=require('fs').readFileSync('README.md','utf8').toLowerCase();for(const s of ['python3 -m http.server','public/index.html','public/styles.css','public/script.js','build command','blank','output directory','public','cloudflare pages','replace:'])if(!r.includes(s))throw new Error('README missing: '+s);console.log('README guidance OK')"
```

Expected: `README guidance OK`.

- [ ] **Step 4: Commit documentation**

```bash
git add README.md
git commit -m "docs: add editing and deployment guide"
```

### Task 5: Local Serving, Responsive QA, and Final Corrections

**Files:**
- Modify if required: `public/index.html`
- Modify if required: `public/styles.css`
- Modify if required: `public/script.js`
- Modify if required: `README.md`

**Interfaces:**
- Consumes: Complete static site.
- Produces: Verified HTTP paths and a visually checked, accessible final page.

- [ ] **Step 1: Start the static server**

Run in a retained terminal session:

```bash
python3 -m http.server 8000 --directory public
```

Expected: server reports listening on port 8000.

- [ ] **Step 2: Verify every local HTTP path**

Run:

```bash
for path in / /styles.css /script.js /images/favicon.svg /images/og-image-placeholder.svg; do curl --fail --silent --show-error "http://127.0.0.1:8000${path}" >/dev/null || exit 1; done
```

Expected: exit code 0 with no output.

- [ ] **Step 3: Inspect mobile layout at 360×800**

In the browser, confirm:

- No horizontal scrolling (`document.documentElement.scrollWidth === document.documentElement.clientWidth`).
- Hero heading remains fully visible and CTA targets do not overlap.
- Menu button opens the navigation, updates `aria-expanded`, closes on Escape, and returns focus.
- Cards and current-chapter rows form a readable single column.
- Focus indicators are visible for the skip link, navigation, CTAs, cards, and social links.

- [ ] **Step 4: Inspect tablet layout at 768×1024**

Confirm the hero remains balanced, card grids move to two columns without stranded or clipped content, section spacing is proportionate, and all anchors land below the sticky header.

- [ ] **Step 5: Inspect desktop layout at 1440×1000**

Confirm the hero uses its asymmetrical two-column composition, interest cards form a coherent connected grid, text line lengths remain readable, and the capped page width prevents excessive stretching.

- [ ] **Step 6: Verify reduced motion and no-JavaScript presentation**

Emulate `prefers-reduced-motion: reduce` and confirm content appears without transforms or smooth scrolling. Disable JavaScript and reload; confirm the navigation, content, CTAs, contact links, and fallback copyright year remain present and usable.

- [ ] **Step 7: Apply and recheck any corrections**

Limit changes to issues found in Steps 2–6. Rerun `node --check public/script.js`, the HTML/CSS/README contract commands from earlier tasks, and all five HTTP requests after edits.

- [ ] **Step 8: Inspect the final change set**

Run:

```bash
git status --short
git diff --check
git log --oneline -5
```

Expected: only intended files are changed or committed; `.DS_Store` remains untouched; `git diff --check` reports no whitespace errors.

- [ ] **Step 9: Commit QA corrections if any**

```bash
git add public/index.html public/styles.css public/script.js README.md
git commit -m "fix: polish responsive and accessible behavior"
```

Skip this commit only if QA required no corrections.
