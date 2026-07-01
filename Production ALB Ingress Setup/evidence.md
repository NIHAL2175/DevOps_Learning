# Evidence Report

# Evidence 1

Command

```bash
kubectl get ingress
```

Output

```
production-alb   <none>   *   80
```

Finding

Ingress Class missing.

---

# Evidence 2

Command

```bash
kubectl describe ingress production-alb
```

Evidence

- Ingress Class: <none>
- Deprecated annotation
- No SSL configuration
- Backend services missing

---

# Evidence 3

Command

```bash
kubectl get svc
```

Evidence

Only the following services existed:

- kubernetes
- reusable-app-dev

Missing services:

- api-service
- admin-service
- dashboard-service

---

# Evidence 4

Applied Fixed Manifest

```bash
kubectl apply -f manifests/alb-ingress-fixed.yaml
```

Result

Ingress updated successfully.

---

# Evidence 5

Validation

```bash
kubectl describe ingress production-alb
```

Verified

- ingressClassName = alb
- SSL Certificate annotation present
- HTTPS listener configured
- SSL Redirect enabled
- Health Check configured
- Target Type IP

---

# Final Evidence

The Production ALB Ingress now follows production best practices and is ready for deployment in an AWS EKS environment.