# TSmithCode Opportunity Technical Alignment Template

**A reusable public-safe system for converting discovery into an inspectable technical decision brief.**

The template combines a rendered GitHub Pages brief, structured configuration, proof links, architecture mapping, readiness checks, and sanitization controls.

**Artifact class:** Reusable decision artifact.

## Evaluator question

Can an ambiguous opportunity be translated into a clear problem statement, bounded use case, technical approach, evidence map, risk controls, and next decision without exposing private source material?

## Decision this proves

Use this template to decide whether an opportunity is understood well enough to proceed to a technical interview, paid diagnostic, bounded prototype, or implementation estimate.

## Best for

- Software consultants preparing an opportunity-specific technical alignment brief.
- Technical leaders documenting a proposed architecture and evidence route before funding implementation.
- Recruiters or hiring managers who want a role-specific proof page without private correspondence.
- CAD Guardian engagements that need a branded engineering-automation brief while preserving private client context.

## Quick start

1. Create a repository from this template or copy the folder.
2. Fill [`config/opportunity.config.json`](config/opportunity.config.json).
3. Fill [`config/brand.config.json`](config/brand.config.json).
4. Replace the public placeholder content in [`index.html`](index.html).
5. Run the readiness gate:

```zsh
python3 scripts/verify_readiness.py
```

6. Review the sanitization checklist.
7. Publish through GitHub Pages only after the public/private boundary is confirmed.

## Expected decision packet

The rendered brief is designed to show:

- the problem and business context heard during discovery;
- the bounded use case being evaluated;
- likely technical stack and integration boundaries;
- an architecture or service map;
- public proof files that support the proposed approach;
- delivery-readiness, observability, security, and AI-governance controls;
- known assumptions, risks, and unresolved questions;
- the next decision and follow-up message.

## Template variants

- [`index.html`](index.html) — public client/evaluator brief for GitHub Pages.
- [`templates/internal-live-call-control-panel.template.html`](templates/internal-live-call-control-panel.template.html) — private companion template for live calls, search, notes, answer shaping, architecture capture, and post-call scoring.

The internal template in this public repository is intentionally unpopulated. Completed live-call control panels belong locally or in a private repository. See [`docs/INTERNAL_LIVE_CALL_TEMPLATE_GUIDE.md`](docs/INTERNAL_LIVE_CALL_TEMPLATE_GUIDE.md).

## Brand system

The page uses four configurable tokens:

```css
--brand-primary: #2f155e;
--brand-secondary: #d02e53;
--brand-accent: #00a6a6;
--brand-support: #0875be;
```

Use brand colors to establish hierarchy, not to substitute for clear evidence. The rest of the page inherits these values for hero, cards, links, borders, buttons, and proof callouts.

See [`docs/BRAND_COLOR_GUIDE.md`](docs/BRAND_COLOR_GUIDE.md).

## Opportunity data model

The template supports:

- opportunity and company name;
- category and status;
- source quality;
- role or engagement family;
- keywords and technical stack;
- target use case;
- architecture map;
- proof files;
- delivery readiness;
- privacy and sanitization notes;
- follow-up and share message.

See [`docs/TECH_STACK_SHAPING_GUIDE.md`](docs/TECH_STACK_SHAPING_GUIDE.md).

## Codex-assisted refresh

[`prompts/CODEX_REFRESH_PROMPT.md`](prompts/CODEX_REFRESH_PROMPT.md) can be used to reshape the template for a specific opportunity using the approved brand, opportunity summary, stack, proof files, and audience.

The prompt is an implementation aid, not authorization to copy private opportunity data into a public repository.

## Proof boundary

This template proves a repeatable discovery-to-decision method. It does not prove that the proposed solution has already been deployed, that a customer approved the architecture, or that an estimate is valid without private discovery.

Never publish proprietary client files, nonpublic correspondence, raw call notes, meeting links, credentials, browser data, restricted screenshots, or unapproved source material.

Before sharing, run the readiness script and review [`docs/SANITIZATION_CHECKLIST.md`](docs/SANITIZATION_CHECKLIST.md).

## What to send

For an evaluator review, send:

- the rendered public brief;
- the source repository;
- the readiness-gate result;
- the approved proof links;
- one sentence naming the decision requested from the recipient.

Keep private call notes and populated internal control panels out of the public package.

## Related TSmithCode proof system

- [TSmithCode software proof kits](https://tsmithcode.ai/software-proof-kits)
- [Software discovery diagnostic](https://tsmithcode.ai/software-discovery-diagnostic)
- [Software consulting contact](https://tsmithcode.ai/software-consulting-contact)
- [TSmithCode public proof standard](docs/TSMITHCODE_PUBLIC_PROOF_STANDARD.md)

For CAD, Autodesk, SolidWorks, BIM, Vault, or PDM/PLM engagements, route the buyer through [CAD Guardian services](https://www.cadguardian.com/services).
