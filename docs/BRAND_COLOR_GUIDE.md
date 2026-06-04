# Brand Color Guide

This template is designed to be restyled from four dominant colors.

## Required Colors

| Token | Purpose |
|---|---|
| `--brand-primary` | Hero, major headings, primary structure. |
| `--brand-secondary` | Main action color, urgency, active accents. |
| `--brand-accent` | Validation, success, workflow highlights. |
| `--brand-support` | Links, architecture/system items, secondary actions. |

## How To Update

Edit [`index.html`](../index.html):

```css
:root{
  --brand-primary:#2f155e;
  --brand-secondary:#d02e53;
  --brand-accent:#00a6a6;
  --brand-support:#0875be;
}
```

Then verify:

- Text is readable on every color.
- Buttons and links are visually distinct.
- The page does not become dominated by a single hue.
- The brand colors support the opportunity rather than making the page feel like a marketing clone.

## When Given A Brand URL

Use the URL for public positioning and visual inspiration only. Do not copy private content, protected assets, logos, or large blocks of text. Prefer the user's provided four color values when available.

