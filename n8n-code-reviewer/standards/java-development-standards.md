# DEMO STANDARDS — REPLACE WITH ORGANIZATION STANDARDS

Version: 1.0

## JAVA-001 — Dependency Injection

Category: Maintainability
Technology: Java

Application classes must prefer constructor injection over field injection so dependencies are explicit and testable.

## JAVA-002 — Null Handling

Category: Reliability
Technology: Java

Public service methods must validate required inputs or document nullable parameters explicitly. Avoid returning null from collection-returning methods.

## JAVA-003 — Resource Management

Category: Reliability
Technology: Java

Resources that hold network, file, database, or stream handles must be closed using framework-managed lifecycles or try-with-resources.
