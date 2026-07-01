# Investigation Report

## Objective
Expose three applications using an AWS Application Load Balancer (ALB) Ingress with production-ready configuration.

---

# Incident Summary

The Production ALB Ingress was deployed with an incomplete configuration.

The ingress exposed the application only through HTTP and lacked production features including SSL termination, HTTP to HTTPS redirection, and Target Group health checks.

Additionally, the backend services referenced by the ingress were not available.

---

# Investigation Steps

## Step 1 – Verify Ingress

Command

```bash
kubectl get ingress
```

Observation

- Ingress created successfully
- Ingress Class was missing
- Only HTTP listener available

---

## Step 2 – Describe Ingress

Command

```bash
kubectl describe ingress production-alb
```

Observation

- Deprecated annotation used
- No SSL configuration
- No HTTPS listener
- No redirect configuration
- Missing health check annotations
- Backend services not found

---

## Step 3 – Verify Backend Services

Command

```bash
kubectl get svc
```

Observation

The following services were missing:

- api-service
- admin-service
- dashboard-service

---

# Root Cause

The ingress manifest was not production ready.

Issues identified:

- Missing ingressClassName
- Deprecated ingress annotation
- No SSL certificate configuration
- No HTTP → HTTPS redirect
- No Target Group health checks
- Backend services unavailable

---

# Resolution

Created a production-ready ingress manifest containing:

- ingressClassName: alb
- SSL certificate annotation
- HTTP & HTTPS listeners
- Automatic SSL redirect
- Health check path
- Internet-facing ALB
- Target type IP

---

# Status

Issue Resolved Successfully