# Secret Rotation Outage Investigation

## Incident Summary

Following AWS Secrets Manager rotation, the application started returning:

* 401 Unauthorized
* Token validation failed

## Investigation Steps

### Application Logs

Observed:

401 Unauthorized

Token validation failed

### Kubernetes Secret Review

Secret inspected:

payment-secret

Stored value:

old-token

### Secret Decoding

Base64 decoded token:

old-token

### Comparison

AWS Secrets Manager:
new-token

Kubernetes Secret:
old-token

## Root Cause

AWS Secrets Manager successfully rotated the secret.

The Kubernetes Secret was not synchronized after rotation.

The application continued using stale credentials, causing authentication failures.

## Conclusion

Secret rotation completed successfully in AWS, but the updated secret was not propagated to Kubernetes.
