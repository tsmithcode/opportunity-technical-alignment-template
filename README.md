# Opportunity Technical Alignment Template

Reusable public-safe template for turning any opportunity, project conversation, or technical discovery into a rendered alignment brief and source proof repo.

Use it when you need to show:

- What problem was heard.
- What use case is being estimated.
- What technical stack likely fits.
- What architecture/service map would be proposed.
- What proof files support the claim.
- What quality, observability, security, and AI-governance controls reduce risk.
- What follow-up message should be shared.

## Quick Start

1. Create a new repo from this template or copy the folder.
2. Edit the four brand colors in [`index.html`](index.html) under `:root`.
3. Fill [`config/opportunity.config.json`](config/opportunity.config.json).
4. Fill [`config/brand.config.json`](config/brand.config.json).
5. Replace placeholder text in [`index.html`](index.html).
6. Run:

```zsh
python3 scripts/verify_readiness.py
```

7. Push to GitHub and enable GitHub Pages from `main` / root.

## Template Variants

- [`index.html`](index.html) is the client-facing rendered brief for GitHub Pages.
- [`templates/internal-live-call-control-panel.template.html`](templates/internal-live-call-control-panel.template.html) is the private internal companion for live calls, search, copy-ready answer shapes, auto-saved notes, architecture capture, and post-call scoring.

Use the internal template only as a placeholder source in this public repo. Populated live-call pages should stay local or in a private repo. See [`docs/INTERNAL_LIVE_CALL_TEMPLATE_GUIDE.md`](docs/INTERNAL_LIVE_CALL_TEMPLATE_GUIDE.md).

## Four-Color Brand System

Set these four values first:

```css
--brand-primary: #2f155e;
--brand-secondary: #d02e53;
--brand-accent: #00a6a6;
--brand-support: #0875be;
```

The rest of the page uses those tokens for hero, cards, links, borders, buttons, and proof callouts.

See [`docs/BRAND_COLOR_GUIDE.md`](docs/BRAND_COLOR_GUIDE.md).

## Opportunity Structure

The template is shaped around the fields commonly needed across opportunity/project proof work:

- opportunity name
- company/client
- category/status
- source quality
- role family
- keywords/tech stack
- target use case
- architecture map
- proof files
- delivery readiness
- privacy/sanitization notes
- follow-up/share message

See [`docs/TECH_STACK_SHAPING_GUIDE.md`](docs/TECH_STACK_SHAPING_GUIDE.md).

## Codex Refresh Prompt

Use [`prompts/CODEX_REFRESH_PROMPT.md`](prompts/CODEX_REFRESH_PROMPT.md) when you want Codex to restyle and reshape the template for a specific opportunity using:

- four dominant brand colors
- brand/site URL
- opportunity description
- tech stack
- proof files
- share audience

## Public Safety

Before sharing, run the readiness script and review [`docs/SANITIZATION_CHECKLIST.md`](docs/SANITIZATION_CHECKLIST.md).

This template should never include proprietary client files, nonpublic correspondence, raw conversation records, meeting links, credentials, browser data, or unapproved source material.
