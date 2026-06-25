# Validation Report

## Pre-Fix State

- Users received **504 Gateway Timeout**.
- ALB Ingress was created but no external endpoint was available.
- AWS Load Balancer Controller reported:
  - Unable to discover subnets
  - Target registration failed

---

## Fix Applied

Added the required subnet annotation to the Ingress configuration:

```yaml
alb.ingress.kubernetes.io/subnets:
  subnet-0123456789abcdef0,
  subnet-0fedcba9876543210
```

---

## Validation Commands

```bash
kubectl get pods
kubectl get svc
kubectl get ingress
```

---

## Validation Results

### Pods

- All application pods are in the **Running** state.

### Service

- ClusterIP service is available.
- Backend endpoints are healthy.

### Ingress

- Ingress configuration updated successfully.

> Note:
> This project was demonstrated on a Kind cluster. Therefore, an AWS Application Load Balancer (ALB) was not provisioned and the ADDRESS field remains empty. On Amazon EKS, the Ingress would receive an ALB DNS name after successful subnet discovery.

---

## Final Result

✔ Incident investigated successfully.

✔ Root cause identified.

✔ Ingress configuration corrected.

✔ Deployment validated successfully.

✔ Documentation completed.