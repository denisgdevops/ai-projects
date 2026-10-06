# DEMO STANDARDS — REPLACE WITH ORGANIZATION STANDARDS

Version: 1.0

## SB-001 — Health Endpoints

Category: Operations
Technology: Spring Boot

All Spring Boot services must expose health endpoints using Spring Boot Actuator. Production deployments must make readiness and liveness health information available to the platform.

## SB-002 — Outbound HTTP Communication

Category: Integration
Technology: Spring Boot

Outbound HTTP calls must define connection and response timeouts. WebClient, RestClient, RestTemplate, Feign, and generated API clients must use the approved timeout configuration rather than default indefinite waits.

## SB-003 — Controller Responsibilities

Category: Architecture
Technology: Spring Boot

Business logic must not reside directly in REST controllers. Controllers should validate transport-level input, delegate to services, and translate service results into API responses.

## SB-004 — Exception Handling

Category: Error Handling
Technology: Spring Boot

Approved exception handling patterns must be used. REST APIs must use centralized exception mapping, such as ControllerAdvice, and must not expose stack traces or implementation details to clients.
