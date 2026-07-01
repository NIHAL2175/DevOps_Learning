# Investigation Report

# Incident Summary

The customer application failed to access DynamoDB after deployment.

Observed Symptoms:

- Pod entered CrashLoopBackOff state.
- Application terminated immediately.
- DynamoDB operations failed.

---

# Investigation Steps

## Step 1 – Verify Pod Status

Command:

```bash
kubectl get pods
```

Observation:

```
customer-app   CrashLoopBackOff
```

Finding:

Application continuously restarted.

---

## Step 2 – Review Application Logs

Command:

```bash
kubectl logs customer-app
```

Observation:

```
Starting customer application...
Connecting to DynamoDB...
AccessDeniedException: Unable to locate IAM credentials
```

Finding:

Application could not authenticate with AWS.

---

## Step 3 – Verify Service Account

Command:

```bash
kubectl get pod customer-app -o jsonpath="{.spec.serviceAccountName}"
```

Observation:

```
default
```

Finding:

Application used the default Kubernetes Service Account.

---

## Step 4 – Inspect Service Account

Command:

```bash
kubectl describe serviceaccount default
```

Observation:

```
Annotations:
<none>
```

Finding:

No IAM Role annotation configured.

---

# Root Cause Analysis

Root Cause:

The application was deployed using the default Kubernetes Service Account instead of an IRSA-enabled Service Account.

Because no IAM Role was associated with the pod, AWS credentials were unavailable, resulting in authentication failure while accessing DynamoDB.

---

# Resolution

Implemented:

- Created customer-app-sa
- Added IRSA IAM Role annotation
- Updated pod to use customer-app-sa
- Redeployed application

---

# Result

Application successfully authenticated using IAM Role and completed DynamoDB operations without AWS Access Keys.