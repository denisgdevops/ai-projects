# DEMO STANDARDS — REPLACE WITH ORGANIZATION STANDARDS

Version: 1.0

## API-001 — API Versioning

Category: API
Technology: REST

REST endpoints must use approved API versioning. Public and internal APIs must include an explicit version in the path, header, or media type according to the owning domain standard.

## API-002 — Correlation IDs

Category: API
Technology: REST

Correlation IDs must be accepted from inbound requests when provided and propagated to outbound service calls. If absent, services must create a correlation ID at the boundary.

## API-003 — Error Response Hygiene

Category: API
Technology: REST

Internal implementation details must not be exposed in error responses. Error responses must use the approved error envelope and safe messages.
