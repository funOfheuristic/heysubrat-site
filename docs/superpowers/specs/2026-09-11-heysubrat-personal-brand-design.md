# Hey Subrat Personal Brand Website Design

## Purpose

Create the first version of `heysubrat.com`: a distinctive, static personal-brand website for Subrat Mishra. The site should connect software engineering, physical training, making, and experimentation as one continuing story of curiosity and deliberate growth. It must not read as a conventional developer portfolio or a software product landing page.

## Audience and Message

The primary audience is software engineers and other curious, growth-oriented people who enjoy learning by doing. The core message is: Subrat builds software, trains his body, tries unfamiliar things, and shares honest progress rather than presenting himself as an expert at everything.

The public identity is:

- Brand mark: Hey Subrat
- Display name: Subrat Mishra
- Domain: `https://heysubrat.com`
- Instagram: `@heysubrat`
- YouTube: placeholder URL until the real channel is supplied
- Email: visible placeholder `hello@heysubrat.com`

## Visual Direction

Use an editorial field-journal aesthetic: dark charcoal surfaces, warm off-white text, and one energetic orange accent. The visual language should combine human movement with builder precision through oversized type, restrained grid lines, index numbers, status marks, and simple CSS geometry.

The page should feel confident, warm, and slightly experimental. Avoid neon-heavy effects, glass panels, large gradients, stock developer imagery, terminal motifs, code snippets, excessive animation, and SaaS-style feature grids.

Typography will use a system font stack so the site has no external dependencies. Display text will be compact, bold, and large; body copy will be relaxed and highly legible. CSS custom properties will define colors, font families, type scale, spacing, radii, borders, shadows, and page width.

## Page Architecture

The site is a single semantic HTML page with these landmarks and sections:

1. A sticky or visually persistent header containing the text mark, desktop navigation, and an accessible mobile menu.
2. A hero with the eyebrow “Software engineer · Curious human,” heading “Hey, I’m Subrat.”, supporting statement, two calls to action, and an abstract CSS-built portrait/profile composition.
3. A “Current chapter” section with editable placeholder activities for building, lifting, running, and experimenting.
4. An interests section with six connected cards: software engineering, gym and fitness, running, boxing, 3D printing, and new experiments.
5. A life-logs section containing three clearly labelled sample content cards with category and platform metadata.
6. An about section explaining the site’s beginner-minded, honest-progress philosophy and including a profile-photo placeholder.
7. A connect section linking to YouTube, Instagram, and email without a contact form.
8. A footer with Subrat Mishra, `heysubrat.com`, and a JavaScript-enhanced current year with a useful no-JavaScript fallback.

The narrative order moves from identity, to present action, to enduring interests, to documented output, to personal philosophy, and finally to connection.

## Interaction and Progressive Enhancement

JavaScript is limited to:

- Toggling the mobile navigation with synchronized `aria-expanded` state.
- Closing the mobile menu after link selection and when Escape is pressed.
- Updating the copyright year.
- Adding reveal classes through `IntersectionObserver` when motion is allowed.

All content, navigation links, calls to action, contact links, and section layouts must remain usable when JavaScript is unavailable. Motion is subtle and disabled or reduced under `prefers-reduced-motion: reduce`.

## Responsive Behavior

- Small phones: single-column flow, compact header, large but bounded hero type, thumb-friendly controls, stacked current-activity rows and cards.
- Tablets: expanded spacing, two-column interest and log layouts where space permits, balanced hero composition.
- Desktops: asymmetrical two-column hero, multi-column card grids, editorial section labels, and generous whitespace within a capped content width.
- Very large screens: content remains centered and readable rather than stretching indefinitely.

All widths must avoid horizontal overflow. Interactive controls must have visible focus indicators, adequate targets, and strong color contrast.

## Content and Placeholder Strategy

Clear HTML comments will identify where to replace:

- Biography and supporting copy
- Profile photograph or portrait treatment
- YouTube URL
- Instagram URL
- Email address, including a warning to change it if the mailbox is inactive
- Current activities
- Sample content cards
- Open Graph image path

The Open Graph image and favicon paths will be present as explicit placeholders in metadata, with matching placeholder files in `public/images/` so local requests do not break. The placeholder assets will be lightweight, locally authored SVG files rather than remote images.

## File Responsibilities

- `public/index.html`: semantic structure, copy, metadata, links, accessible controls, and editing comments.
- `public/styles.css`: complete visual system, responsive layout, interaction states, reduced-motion handling, and CSS artwork.
- `public/script.js`: progressive enhancement for navigation, year, and entrance effects.
- `public/images/favicon.svg`: local favicon placeholder.
- `public/images/og-image-placeholder.svg`: local Open Graph image placeholder.
- `README.md`: preview, editing, placeholder replacement, and Cloudflare Pages deployment instructions.

No framework, package manager, build tooling, backend, external library, web font, or remote image is used.

## Accessibility and Semantics

Use semantic header, navigation, main, section, article, address, and footer elements; one `h1`; logical descending heading levels; descriptive link text; a skip link; accessible navigation labelling; decorative shapes hidden from assistive technology; visible `:focus-visible` styles; and contrast appropriate for normal text. The mobile menu remains keyboard operable and Escape-dismissible.

## Validation

Before completion:

- Parse and inspect the HTML structure and local asset references.
- Check JavaScript syntax and ensure no console-breaking assumptions.
- Serve `public/` from a local HTTP server and confirm HTML, CSS, JavaScript, favicon, and Open Graph placeholder return successfully.
- Inspect the rendered page at representative mobile, tablet, and desktop widths.
- Verify mobile-menu keyboard behavior, focus visibility, anchor navigation, reduced-motion rules, and no horizontal overflow.
- Confirm the page remains coherent with JavaScript disabled.

## Acceptance Criteria

The completed repository contains the requested `public/` structure and README, looks polished across the specified viewport classes, contains every requested content section and edit comment, has no external runtime or image dependencies, works from a plain local HTTP server, and is ready for Cloudflare Pages with a blank build command and `public` as its output directory.
