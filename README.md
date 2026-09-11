# Hey Subrat

The first static version of [heysubrat.com](https://heysubrat.com), built with semantic HTML, modern CSS, and a small amount of vanilla JavaScript. There are no packages, remote assets, or build steps.

## Preview locally

From the project root, run:

```bash
python3 -m http.server 8000 --directory public
```

Then open [http://localhost:8000](http://localhost:8000). Stop the server with `Ctrl+C`.

Opening `public/index.html` directly will display most of the site, but a local HTTP server gives the closest match to Cloudflare Pages and confirms that all relative asset paths work.

## Where to edit

- `public/index.html` contains the text, metadata, links, section structure, current activities, content cards, and contact details.
- `public/styles.css` contains the colour variables, typography, spacing, layouts, responsive breakpoints, CSS artwork, and motion settings. Start with the custom properties under `:root` when changing the visual theme.
- `public/script.js` contains the mobile-menu behavior, automatic copyright year, and optional entrance reveals.
- `public/images/` contains the favicon and Open Graph placeholder. Add a future profile photograph here as an optimized local image.

## Replace the placeholders

Search `public/index.html` for `REPLACE:`. Each comment identifies an intentional first-version placeholder:

1. Biography — update the hero statement and longer about copy.
2. Profile photograph — replace either CSS placeholder with a local, optimized portrait and meaningful alt text.
3. YouTube URL — replace the provisional `https://www.youtube.com/@heysubrat` address with the confirmed channel URL.
4. Instagram URL — currently points to `https://www.instagram.com/heysubrat/`.
5. Email address — `hello@heysubrat.com` is provisional. Change both the visible text and `mailto:` value if that mailbox is not active.
6. Current activities — keep the Building, Lifting, Running, and Experimenting notes specific and current.
7. Content cards — replace all three cards labelled “Sample” with real videos, posts, or short updates and their final links.
8. Open Graph image — replace `public/images/og-image-placeholder.svg` with final 1200 × 630 social artwork and update the metadata path if the filename changes.

The favicon in `public/images/favicon.svg` is also intentionally simple and can be replaced without changing the markup if the filename stays the same.

## Deploy with Cloudflare Pages

1. Push this repository to your Git provider.
2. In Cloudflare, create a Pages project and connect the repository.
3. Choose **None** for the framework preset.
4. Leave the **Build command blank**. This project has no build process.
5. Set the **Build output directory** to `public`.
6. Deploy the project, then attach the `heysubrat.com` custom domain in the Pages project settings.

Every push to the configured production branch will publish the files inside `public` directly.
