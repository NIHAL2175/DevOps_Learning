# Validation Report

## Objective
Validate that the application can successfully perform DynamoDB operations using IAM Roles for Service Accounts (IRSA) without AWS Access Keys.

---

# Pre-Fix Validation

## Pod Status

Command:

```bash
kubectl get pods
```

Result:

```
customer-app   0/1   CrashLoopBackOff
```

Status:
- Application failed to start successfully.
- Pod repeatedly restarted.

---

## Application Logs

Command:

```bash
kubectl logs customer-app
```

Result:

```
Starting customer application...
Connecting to DynamoDB...
AccessDeniedException: Unable to locate IAM credentials
```

Status:
- Application unable to authenticate with AWS.
- No IAM credentials available.

---

## Service Account Validation

Command:

```bash
kubectl get pod customer-app -o jsonpath="{.spec.serviceAccountName}"
```

Result:

```
default
```

Status:
- Default Service Account used.
- No IRSA configuration.

---

# Fix Applied

Implemented:

- Created IRSA Service Account
- Associated IAM Role annotation
- Updated application to use customer-app-sa
- Redeployed application

---

# Post-Fix Validation

## Pod Status

Command:

```bash
kubectl get pods
```

Result:

```
customer-app   1/1   Running
```

Status:
- Application running successfully.

---

## Application Logs

Command:

```bash
kubectl logs customer-app
```

Result:

```
Starting customer application...
Connecting to DynamoDB...
IAM Role assumed successfully
Customer Read Successful
Customer Write Successful
Customer Update Successful
```

Status:
- Application authenticated successfully.
- Read operation successful.
- Write operation successful.
- Update operation successful.

---

# Validation Summary

| Validation | Status |
|------------|--------|
| Pod Running | ✅ PASS |
| IRSA Service Account Configured | ✅ PASS |
| IAM Role Used | ✅ PASS |
| DynamoDB Read | ✅ PASS |
| DynamoDB Write | ✅ PASS |
| DynamoDB Update | ✅ PASS |

---

# Final Result

The application successfully accessed DynamoDB using IAM Roles for Service Accounts (IRSA) without AWS Access Keys. All required customer operations (Read, Write, Update) completed successfully.