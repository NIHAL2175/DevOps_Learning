# ALB Ingress Failure Investigation

## Incident Summary

The application became inaccessible after exposing it through an AWS Application Load Balancer (ALB) Ingress.

Users received:

```text
504 Gateway Timeout
```

---

## Investigation Steps

### Step 1 – Verify Application Pods

Command:

```bash
kubectl get pods
```

Observation:

- All application pods were in the Running state.
- No container failures were observed.

Conclusion:

Application was healthy.

---

### Step 2 – Verify Service

Command:

```bash
kubectl get svc
```

Observation:

- Service was available.
- ClusterIP assigned successfully.

Conclusion:

Service configuration was correct.

---

### Step 3 – Verify Ingress

Command:

```bash
kubectl get ingress
kubectl describe ingress payment-ingress
```

Observation:

- Ingress resource existed.
- ADDRESS field was empty.
- No external endpoint was created.

Conclusion:

Ingress was not provisioned successfully.

---

### Step 4 – Review Controller Logs

Command:

```bash
kubectl logs -n kube-system deployment/aws-load-balancer-controller
```

Observed Error:

```text
Unable to discover subnets
```

Conclusion:

AWS Load Balancer Controller could not locate eligible subnets for ALB creation.

---

## Root Cause

The required AWS subnet tags for ALB auto-discovery were missing.

As a result:

- ALB was not created.
- Target registration failed.
- Application remained inaccessible.
- Users experienced a 504 Gateway Timeout.
