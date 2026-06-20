# 📸 Evidence Report – Helm Upgrade Failure

## Incident Evidence

This document contains the evidence collected during the investigation and resolution of the Helm upgrade failure.

---

# Evidence 1 – Version 1 Deployment

### Selector Configuration

```yaml
matchLabels:
  app: payment
```

### Helm Installation

Command:

```bash
helm install payment-service .
```

Result:

```text
STATUS: deployed
REVISION: 1
```

### Deployment Verification

Command:

```bash
kubectl get deployment payment-service -o yaml | findstr "app:"
```

Output:

```text
app: payment
```

---

# Evidence 2 – Version 2 Configuration

### Updated Selector

```yaml
matchLabels:
  app: payment-v2
```

### Template Verification

Command:

```bash
helm template payment-service . | findstr app:
```

Output:

```text
app: payment-v2
```

---

# Evidence 3 – Upgrade Failure

### Upgrade Command

```bash
helm upgrade payment-service .
```

### Error Output

```text
UPGRADE FAILED

Deployment.apps "payment-service" is invalid:

spec.selector:
Invalid value:
{"matchLabels":{"app":"payment-v2"}}

field is immutable
```

### Observation

Kubernetes rejected the Deployment update because the selector field had changed.

---

# Evidence 4 – Existing Deployment Selector

Command:

```bash
kubectl get deployment payment-service -o yaml | findstr "app:"
```

Output:

```text
app: payment
```

### Observation

The existing Deployment selector was still:

```text
app: payment
```

while the upgraded chart attempted to use:

```text
app: payment-v2
```

---

# Evidence 5 – Safe Upgrade

### Remove Existing Release

Command:

```bash
helm uninstall payment-service
```

Result:

```text
release "payment-service" uninstalled
```

### Install New Release

Command:

```bash
helm install payment-service .
```

Result:

```text
STATUS: deployed
```

---

# Evidence 6 – Final Validation

Command:

```bash
kubectl get deployment payment-service -o yaml | findstr "app:"
```

Output:

```text
app: payment-v2
```

### Observation

The Deployment was recreated successfully using the new selector.

---

# Evidence Summary

| Evidence              | Result       |
| --------------------- | ------------ |
| Version 1 Deployment  | ✅ Verified   |
| Version 2 Chart       | ✅ Verified   |
| Upgrade Failure       | ✅ Reproduced |
| Immutable Field Error | ✅ Confirmed  |
| Safe Upgrade          | ✅ Applied    |
| Final Deployment      | ✅ Validated  |

---

# Conclusion

The collected evidence confirms that the Helm upgrade failed because the Deployment selector was modified from:

```text
app: payment
```

to:

```text
app: payment-v2
```

Since Kubernetes treats Deployment selectors as immutable fields, the upgrade was rejected.

The issue was successfully resolved using a safe deployment recreation approach.
