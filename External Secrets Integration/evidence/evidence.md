# Evidence Report

## Incident Evidence

### 1. Pod Failure

Command:

```bash
kubectl get pods
```

Output:

```text
demo-app   0/1   CreateContainerConfigError
```

---

### 2. Pod Description

Command:

```bash
kubectl describe pod demo-app
```

Evidence:

```text
Error: secret "app-secret" not found
```

---

### 3. External Secret Failure

Command:

```bash
kubectl get externalsecret
```

Output:

```text
STATUS: SecretSyncedError
READY : False
```

---

### 4. Authentication Errors

Observed Errors:

```text
UnrecognizedClientException
```

```text
InvalidSignatureException
```

---

### 5. Root Cause Evidence

AWS Secrets Manager secret was stored in an invalid format, preventing External Secrets from locating:

* DB_USERNAME
* DB_PASSWORD
* JWT_SECRET

---

## Post-Fix Evidence

### External Secret

```bash
kubectl get externalsecret
```

Output:

```text
STATUS: SecretSynced
READY : True
```

---

### Kubernetes Secret

```bash
kubectl get secret app-secret
```

Output:

```text
app-secret   Opaque   3
```

---

### Application Validation

```bash
kubectl logs demo-app
```

Output:

```text
Starting Application...
Reading Kubernetes Secret...
DB_USERNAME=admin
Application Started Successfully
```

---

## Conclusion

The External Secrets Operator successfully synchronized the secret from AWS Secrets Manager, automatically created the Kubernetes Secret, and the application started successfully using the injected secret values.
