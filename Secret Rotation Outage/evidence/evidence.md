# Evidence Collection

## Evidence 1 – Application Failure

kubectl logs payment-service

Output:

Using token from Kubernetes Secret...
401 Unauthorized
Token validation failed

## Evidence 2 – Stale Secret

kubectl get secret payment-secret -o yaml

Encoded token:

b2xkLXRva2Vu

Decoded value:

old-token

## Evidence 3 – Updated Secret

kubectl get secret payment-secret -o yaml

Encoded token:

bmV3LXRva2Vu

Decoded value:

new-token

## Evidence 4 – Post Fix Validation

kubectl logs payment-service

Output:

Using rotated token...
Token validation successful
Authentication successful
