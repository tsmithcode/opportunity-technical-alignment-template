# Tech Stack Shaping Guide

Use this guide to adapt the template to any opportunity or project.

## Opportunity Fields To Capture

| Field | Why it matters |
|---|---|
| Company/client | Sets audience and brand context. |
| Opportunity/project name | Makes the proof specific. |
| Category/status | Distinguishes inbound lead, active process, follow-up, offer, or project work. |
| Source quality | Prevents overclaiming when evidence is thin. |
| Role family | Groups the opportunity into delivery lanes. |
| Keywords/tech stack | Drives architecture and proof sections. |
| Evidence/proof files | Makes claims inspectable. |
| Privacy notes | Keeps public artifacts safe. |

## Stack Layers

Always try to map these layers, even if the answer is "unknown, confirm":

| Layer | Examples |
|---|---|
| Frontend/UI | React, Angular, Vue, static site, internal portal, desktop UI. |
| API/backend | .NET, Java/Spring, Node.js, Python/FastAPI, serverless functions. |
| Cloud/platform | AWS, Azure, GCP, Vercel, on-prem, hybrid. |
| Data | SQL Server, PostgreSQL, DynamoDB, Cosmos DB, files, object storage, APIs. |
| Workflow/queue | SQS, Step Functions, EventBridge, Azure Service Bus, Celery, Hangfire. |
| Worker/runtime | Container, VM, Windows worker, CAD worker, batch job, external API. |
| Observability | CloudWatch, Datadog, Splunk, OpenTelemetry, logs/metrics/traces. |
| Security/governance | IAM, Entra ID, KMS, Secrets Manager, Key Vault, audit trail. |
| AI | Approved RAG, code assist, summarization, synthetic data, guardrails. |

## Architecture Rule

Separate the shape into:

```text
UI -> API -> state -> storage -> orchestration/queue -> worker/runtime -> output storage -> review/notification -> observability/audit
```

If a layer is not needed, say why. If a layer is unknown, mark it as a question.

