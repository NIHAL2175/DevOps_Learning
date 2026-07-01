# Investigation Report

## Objective

Integrate AWS Secrets Manager with Kubernetes using External Secrets Operator to automatically create Kubernetes Secrets.

## Incident Summary

The application pod (`demo-app`) failed to start because it expected a Kubernetes Secret named `app-secret`, but the secret did not exist.

## Investigation Performed

### 1. Pod Investigation

Command:

```bash
kubectl describe pod demo-app
```

Observation:

* Pod status: `CreateContainerConfigError`
* Error:

```
secret "app-secret" not found
```

---

### 2. Kubernetes Secret Verification

Command:

```bash
kubectl get secret
```

Observation:

* `app-secret` was missing.

---

### 3. External Secrets Operator Verification

Commands:

```bash
kubectl get pods -n external-secrets
kubectl get secretstore
kubectl get externalsecret
```

Observation:

* Operator installed successfully.
* SecretStore was Ready.
* ExternalSecret failed to synchronize.

---

### 4. AWS Authentication Investigation

Observed errors:

```
UnrecognizedClientException
```

Later:

```
InvalidSignatureException
```

Root Cause:

The Kubernetes `aws-secret` contained an incorrect Secret Access Key.

---

### 5. AWS Secrets Manager Investigation

Command:

```bash
aws secretsmanager get-secret-value --secret-id app-secret
```

Observation:

The secret was stored in an invalid JSON format.

Example:

```
{DB_USERNAME:admin,DB_PASSWORD:Password@123,JWT_SECRET:jwt-secret-123}
```

---

### 6. Final Investigation

After correcting AWS credentials and updating the secret to valid JSON, the External Secrets Operator synchronized successfully and created the Kubernetes Secret automatically.
