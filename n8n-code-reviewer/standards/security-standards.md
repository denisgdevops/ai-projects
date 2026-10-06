# DEMO STANDARDS — REPLACE WITH ORGANIZATION STANDARDS

Version: 1.0

## SEC-001 — Secrets in Source Control

Category: Security
Technology: All

Credentials, tokens, private keys, passwords, and connection strings containing secrets must never be committed to source control.

## SEC-002 — Parameterized SQL

Category: Security
Technology: Database

SQL queries must use parameterized queries or approved ORM query binding. Queries must not be constructed by concatenating user-controlled input into SQL strings.

## SEC-003 — Sensitive Logging

Category: Security
Technology: All

Sensitive information, including credentials, personal data, payment data, and security tokens, must not be written to application logs.
