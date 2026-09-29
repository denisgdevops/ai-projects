# Microservice Standard

Microservices must expose HTTP health endpoints.

Services must implement readiness and liveness probes.

Applications must not rely on local session state.

Applications should support horizontal scaling.

Services must implement appropriate retry, timeout and circuit breaker patterns.

Production services must support high availability across multiple instances.
