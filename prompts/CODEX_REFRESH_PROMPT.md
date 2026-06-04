# Codex Refresh Prompt

Use this prompt when refreshing the template for a specific opportunity or project.

```text
You are working in the `opportunity-technical-alignment-template` repo.

Goal:
Refresh this template into a public-safe technical alignment proof for:
{CLIENT_OR_PROJECT_NAME}

Inputs:
- Brand/site URL: {BRAND_SITE_URL}
- Four dominant brand colors:
  1. Primary: {PRIMARY_HEX}
  2. Secondary: {SECONDARY_HEX}
  3. Accent: {ACCENT_HEX}
  4. Support: {SUPPORT_HEX}
- Opportunity/project summary: {SUMMARY}
- Audience: {AUDIENCE}
- Target use case: {TARGET_USE_CASE}
- Expected input package: {INPUTS}
- Expected output package: {OUTPUTS}
- Known/probable tech stack: {TECH_STACK}
- Cloud/platform preference: {CLOUD_OR_PLATFORM}
- Worker/runtime constraints: {WORKER_RUNTIME}
- Proof files available: {PROOF_FILES}
- Public share URL target: {RENDERED_BRIEF_URL}
- Source repo URL: {SOURCE_REPO_URL}
- Internal live-call page needed: {YES_OR_NO}
- Live call start time, if known: {CALL_START_TIME}

Instructions:
1. Update `index.html` only where needed. Preserve the template structure.
2. Set the four brand colors in `:root`:
   - `--brand-primary`
   - `--brand-secondary`
   - `--brand-accent`
   - `--brand-support`
3. Use the brand/site URL only for public positioning and visual inspiration. Do not copy proprietary text, logos, protected imagery, or private content.
4. Replace placeholders with client-safe language.
5. Shape the tech stack section around the actual opportunity:
   - frontend/UI
   - API/backend
   - cloud/platform
   - data
   - workflow/queue
   - worker/runtime
   - observability
   - security/governance
   - AI guardrails
6. Keep claims evidence-based. If a fact is uncertain, phrase it as a qualification question.
7. Add or update proof file links only if the proof is public-safe.
8. Do not include raw conversation records, private names, meeting links, nonpublic correspondence, compensation, credentials, local private paths, or proprietary client files.
9. If an internal live-call page is needed, use `templates/internal-live-call-control-panel.template.html` as the private companion. Keep any populated version local or in a private repo; do not publish it as the client-facing brief.
10. Promote only sanitized, evidence-based points from the internal page into `index.html`.
11. Run `python3 scripts/verify_readiness.py`.
12. Start a local server and verify the rendered HTML has no horizontal overflow.
13. Commit and push.
14. If GitHub Pages is enabled, wait for Pages to build and verify the rendered URL.

Output:
- Brief summary of changed sections.
- Commit hash.
- Rendered brief URL.
- Source repo URL.
- Internal template path or private live-call file path, if created.
- Any remaining manual placeholders or questions.
```
