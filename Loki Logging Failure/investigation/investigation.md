# Loki Logging Failure - Investigation Report

## Incident Summary

Application logs stopped appearing in Grafana.

Observed Errors:

### Alloy

```text
failed to push logs
HTTP 403
```

### Loki

```text
authentication failed
```

---

## Investigation Process

### Step 1 - Application Verification

Command:

```powershell
kubectl logs sample-app --tail=10
```

Result:

```text
INFO Payment processed
```

Finding:

* Application generating logs successfully.
* Application not identified as failure point.

---

### Step 2 - Alloy Verification

Command:

```powershell
kubectl logs alloy
```

Result:

```text
failed to push logs
HTTP 403
```

Finding:

* Alloy receiving logs.
* Alloy attempting to forward logs.
* Push requests rejected.

---

### Step 3 - Loki Verification

Command:

```powershell
kubectl logs loki
```

Result:

```text
authentication failed
```

Finding:

* Loki received requests.
* Authentication validation failed.

---

## Root Cause

Invalid or missing authentication credentials between Alloy and Loki.

Loki rejected incoming requests with HTTP 403.

As a result logs never reached Grafana.
