# Internal Live Call Template Guide

Use `templates/internal-live-call-control-panel.template.html` for private preparation and live technical or team calls.

This template is the private companion to the client-facing `index.html` brief:

- `index.html`: public-safe, rendered, shareable technical alignment brief.
- `templates/internal-live-call-control-panel.template.html`: private working surface for search, copy-ready answer shapes, live notes, architecture capture, follow-up capture, and post-call scoring.

## Recommended Workflow

1. Copy the internal template into a private opportunity folder or private repo.
2. Replace placeholders with private working notes.
3. Open it locally during the call.
4. Capture notes in the browser textareas.
5. Promote only sanitized, evidence-based points into `index.html`.
6. Run `python3 scripts/verify_readiness.py` before anything public is pushed.

## Do Not Publish Populated Internal Pages

The public template repo intentionally tracks only the placeholder template. Populated live-call pages can include names, meeting context, urgency, objections, private notes, and unapproved source references.

The `.gitignore` blocks common private variants such as `*.private.html`, `*.internal.html`, and generated live-call files. Keep real versions local or in a private repo.

## What To Promote Into The Client Brief

- Target use case.
- Architecture map.
- Qualified service map.
- Public-safe proof files.
- Risk controls.
- Open qualification questions.
- Pilot path.
- Clean follow-up message.

## What To Remove

- Private names.
- Meeting details.
- Internal staffing or urgency notes.
- Compensation, rate, or hiring-process details.
- Personal prep notes.
- Unapproved files, screenshots, source records, or correspondence.
- Unsupported claims.
