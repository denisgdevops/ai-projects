# API Security Standard

All external APIs must be exposed through the enterprise API gateway.

Authentication must use OAuth 2.0.

JWT tokens must be validated at the API gateway.

Service-to-service integrations should use mutual TLS where required.

APIs must not expose credentials, passwords, PINs, or secrets.

Sensitive API transactions must be logged using approved security logging standards.
