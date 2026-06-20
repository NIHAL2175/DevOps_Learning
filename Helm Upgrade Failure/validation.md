# ✅ Validation Report – Helm Upgrade Failure

## Validation Objective

Validate the cause of the Helm upgrade failure and verify the safe upgrade solution.

---

## Validation Steps

### Step 1 – Deploy Version 1

The Helm chart was configured with:

```yaml
matchLabels:
  app: payment
```

Deployment command:

```bash
helm install payment-service .
```

Result:

```text
STATUS: deployed
REVISION: 1
```

Validation:

```bash
kubectl get deployment payment-service -o yaml | findstr "app:"
```

Output:

```text
app: payment
```

---

### Step 2 – Modify Chart to Version 2

The Helm chart selector was updated to:

```yaml
matchLabels:
  app: payment-v2
```

Validation:

```bash
helm template payment-service . | findstr app:
```

Output:

```text
app: payment-v2
```

---

### Step 3 – Execute Helm Upgrade

Command:

```bash
helm upgrade payment-service .
```

Result:

```text
UPGRADE FAILED

Deployment.apps "payment-service" is invalid:

spec.selector:
Invalid value:
{"matchLabels":{"app":"payment-v2"}}

field is immutable
```

Validation Outcome:

* Error successfully reproduced.
* Kubernetes rejected selector modification.
* Incident scenario confirmed.

---

### Step 4 – Apply Safe Upgrade Approach

Existing release removed:

```bash
helm uninstall payment-service
```

New release installed:

```bash
helm install payment-service .
```

Result:

```text
STATUS: deployed
```

---

### Step 5 – Validate New Deployment

Command:

```bash
kubectl get deployment payment-service -o yaml | findstr "app:"
```

Output:

```text
app: payment-v2
```

Validation Outcome:

* New Deployment created successfully.
* Updated selector applied.
* Upgrade completed safely.

---

## Validation Summary

| Validation Item                   | Status    |
| --------------------------------- | --------  |
| Version 1 Deployment              | ✅ Passed |
| Version 2 Chart Generated         | ✅ Passed |
| Immutable Field Error Reproduced  | ✅ Passed |
| Root Cause Confirmed              | ✅ Passed |
| Safe Upgrade Applied              | ✅ Passed |
| Deployment Recreated Successfully | ✅ Passed |

---

## Final Result

The Helm upgrade failure was successfully investigated and reproduced.

The root cause was identified as a modification of the immutable Deployment selector.

The issue was resolved by uninstalling and reinstalling the release, allowing Kubernetes to create a new Deployment with the updated selector.
