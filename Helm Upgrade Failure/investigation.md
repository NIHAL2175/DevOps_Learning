# 🔍 Investigation Report – Helm Upgrade Failure

## Incident Summary

A production deployment failed during a Helm upgrade operation.

The following command was executed:

```bash
helm upgrade payment-service .
```

The upgrade failed with the error:

```text
UPGRADE FAILED:

Deployment.apps "payment-service" is invalid:

spec.selector:
Invalid value:
{"matchLabels":{"app":"payment-v2"}}

field is immutable
```

---

## Symptoms Observed

* Helm upgrade operation failed.
* Deployment was not updated.
* New application version could not be deployed.
* Kubernetes rejected the Deployment update request.

---

## Environment

| Component       | Value           |
| --------------- | --------------- |
| Kubernetes      | Kind Cluster    |
| Package Manager | Helm            |
| Resource Type   | Deployment      |
| Release Name    | payment-service |

---

## Initial Deployment (Version 1)

The application was initially deployed with the selector:

```yaml
selector:
  matchLabels:
    app: payment
```

Deployment completed successfully.

Kubernetes stored this selector permanently as part of the Deployment specification.

---

## Upgrade Attempt (Version 2)

The Helm chart was modified to use:

```yaml
selector:
  matchLabels:
    app: payment-v2
```

A Helm upgrade was executed:

```bash
helm upgrade payment-service .
```

---

## Findings

The Deployment already existed in the cluster.

During the upgrade, Helm attempted to modify:

```yaml
spec.selector.matchLabels
```

from:

```yaml
app: payment
```

to:

```yaml
app: payment-v2
```

Kubernetes rejected the request because Deployment selectors are immutable after resource creation.

---

## Root Cause

The root cause was a modification of the Deployment selector label.

Kubernetes uses selectors to identify and manage Pods belonging to a Deployment.

Changing the selector after creation could cause the Deployment to lose control of existing Pods.

To prevent this situation, Kubernetes marks:

```yaml
spec.selector
```

as an immutable field.

---

## Impact

* Deployment upgrade failed.
* New version was not released.
* Existing workload remained unchanged.
* Production deployment process was interrupted.

---

## Resolution Strategy

Instead of modifying the selector on an existing Deployment:

1. Remove the existing Helm release.
2. Recreate the Deployment using the new selector.

Commands used:

```bash
helm uninstall payment-service
helm install payment-service .
```

This allowed Kubernetes to create a brand-new Deployment using the updated selector.

---

## Conclusion

The failure occurred because the Helm upgrade attempted to modify an immutable Kubernetes Deployment selector.

The issue was resolved by recreating the Deployment instead of updating the selector in-place.
