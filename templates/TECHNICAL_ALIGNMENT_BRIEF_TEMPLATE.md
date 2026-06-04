# Technical Alignment Brief Template

## Share Links

- Rendered brief: {RENDERED_BRIEF_URL}
- Source repo: {SOURCE_REPO_URL}

## One-Line Summary

{CLIENT_OR_PROJECT_NAME} appears to need {CORE_OUTCOME} by connecting {INPUTS} to {AUTOMATION_OR_DELIVERY_SYSTEM} with {VALIDATION_OR_REVIEW_MODEL}.

## What The Discussion Clarified

- Current workflow: {CURRENT_WORKFLOW}
- Primary pain: {PRIMARY_PAIN}
- Business driver: {BUSINESS_DRIVER}
- Technical driver: {TECHNICAL_DRIVER}
- Trust or risk issue: {TRUST_OR_RISK_ISSUE}
- Urgency or timing: {URGENCY}

## Target Use Case

```text
{USER_ACTION} -> {INPUT_PACKAGE} -> {AUTOMATION_OR_SERVICE_LAYER} -> {OUTPUT_PACKAGE}
```

## Architecture Map

```text
{UI} -> {API} -> {STATE} -> {STORAGE_INPUT} -> {ORCHESTRATION_QUEUE} -> {WORKER} -> {STORAGE_OUTPUT} -> {REVIEW_NOTIFY} -> {OBSERVABILITY_AUDIT}
```

## Expected Services

| Layer | Service/technology | Why |
|---|---|---|
| UI | {UI_SERVICE} | {UI_REASON} |
| API | {API_SERVICE} | {API_REASON} |
| State | {STATE_SERVICE} | {STATE_REASON} |
| Storage | {STORAGE_SERVICE} | {STORAGE_REASON} |
| Orchestration | {ORCHESTRATION_SERVICE} | {ORCHESTRATION_REASON} |
| Queue/broker | {QUEUE_SERVICE} | {QUEUE_REASON} |
| Worker/runtime | {WORKER_SERVICE} | {WORKER_REASON} |
| Observability | {OBSERVABILITY_SERVICE} | {OBSERVABILITY_REASON} |
| Security/audit | {SECURITY_AUDIT_SERVICE} | {SECURITY_AUDIT_REASON} |

## Proof Files

| Proof file | What it demonstrates |
|---|---|
| {PROOF_FILE_1} | {PROOF_POINT_1} |
| {PROOF_FILE_2} | {PROOF_POINT_2} |
| {PROOF_FILE_3} | {PROOF_POINT_3} |

## Pilot Path

| Phase | Activity | Deliverable |
|---|---|---|
| 1 | {PHASE_1_ACTIVITY} | {PHASE_1_DELIVERABLE} |
| 2 | {PHASE_2_ACTIVITY} | {PHASE_2_DELIVERABLE} |
| 3 | {PHASE_3_ACTIVITY} | {PHASE_3_DELIVERABLE} |

