# DEMO STANDARDS — REPLACE WITH ORGANIZATION STANDARDS

Version: 1.0

## OBS-001 — Structured Logging for Integrations

Category: Observability
Technology: All

Critical integration flows must provide structured logging for request start, dependency outcome, and failure conditions without logging sensitive payloads.

## OBS-002 — Correlation in Logs

Category: Observability
Technology: All

Correlation IDs must be included in relevant application logs and propagated across service boundaries so distributed requests can be traced.

## OBS-003 — External Dependency Failures

Category: Observability
Technology: All

External dependency failures must be observable through logs, metrics, or tracing. Failures must include dependency name and safe diagnostic context.
