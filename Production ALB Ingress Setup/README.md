<div align="center">

# 🚀 Production ALB Ingress Setup (AWS EKS)

![AWS](https://img.shields.io/badge/AWS-EKS-orange)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Ingress-blue)
![ALB](https://img.shields.io/badge/AWS-Application_Load_Balancer-yellow)
![Ingress](https://img.shields.io/badge/Ingress-Production-success)
![SSL](https://img.shields.io/badge/SSL-HTTPS-green)
![Health Checks](https://img.shields.io/badge/Health_Checks-Enabled-brightgreen)

<img src="Architecture/Arch.png" width="100%">

</div>

---

# 📂 Project Structure

| Folder | Description |
|---------|-------------|
| 📁 Architecture | Before & After architecture diagrams |
| 📁 manifests | Kubernetes Ingress manifests (Broken & Fixed) |
| 📄 investigation.md | Complete investigation report |
| 📄 evidence.md | Commands and collected evidence |
| 📄 validation.md | Validation after implementing the fix |
| 📄 README.md | Project documentation |

---

# 🧠 Project Overview

This project demonstrates how to configure a **Production-ready AWS Application Load Balancer (ALB) Ingress** for Kubernetes applications running on **Amazon EKS**.

The exercise reproduces a real-world production incident where the ALB Ingress was deployed with an incomplete configuration.

The investigation identifies the missing production configurations and implements a fully compliant ALB Ingress with:

- SSL/TLS Termination
- HTTP → HTTPS Redirection
- Target Group Health Checks
- Internet-facing ALB
- AWS ALB Controller
- Production Best Practices

---

# 🚨 Incident Summary

The ALB Ingress was deployed using an incomplete Kubernetes manifest.

The deployment suffered from multiple production issues:

- Missing Ingress Class
- Deprecated annotations
- No SSL Certificate
- HTTP only
- No HTTPS Redirect
- Missing Health Checks
- Backend services unavailable

As a result, the ingress was **not suitable for production deployment**.

---

# 🏗️ Architecture Overview

```
                 DevOps Engineer
                        │
                        ▼
                 GitHub Repository
                        │
                        ▼
             Kubernetes Ingress Manifest
                        │
                        ▼
          AWS Load Balancer Controller
                        │
                        ▼
        Application Load Balancer (ALB)
                        │
        ┌───────────────┼───────────────┐
        ▼               ▼               ▼
   /api/*          /admin/*      /dashboard/*
        │               │               │
        ▼               ▼               ▼
 api-service     admin-service   dashboard-service
```

---

# 🔧 Technologies Used

| Layer | Tool | Purpose |
|---------|------|---------|
| ☁ Cloud | AWS EKS | Kubernetes Cluster |
| ☸ Orchestration | Kubernetes | Container Orchestration |
| 🌐 Load Balancer | AWS ALB | External Traffic Routing |
| 🚦 Ingress | AWS Load Balancer Controller | Creates ALB from Kubernetes Ingress |
| 🔒 Security | AWS Certificate Manager (ACM) | SSL Certificates |
| 🛣 Routing | Kubernetes Ingress | URL Path Routing |

---

# ❌ Initial Configuration (Broken)

The original ingress manifest contained only:

- HTTP Listener
- Deprecated Annotation
- No SSL
- No HTTPS Redirect
- No Health Checks
- Missing ingressClassName

Example

```yaml
metadata:
  annotations:
    kubernetes.io/ingress.class: alb
```

Result

- HTTP only
- No TLS
- Production requirements not met

---

# 🔍 Investigation Process

The following commands were used during the investigation.

### Verify Ingress

```bash
kubectl get ingress
```

---

### Inspect Ingress

```bash
kubectl describe ingress production-alb
```

---

### Verify Services

```bash
kubectl get svc
```

---

# 🔎 Root Cause Analysis

The investigation identified several configuration issues.

| Issue | Impact |
|--------|--------|
| Missing ingressClassName | ALB Controller configuration incomplete |
| Deprecated Annotation | Legacy configuration |
| No SSL Certificate | HTTPS unavailable |
| HTTP Only | Insecure communication |
| Missing HTTPS Redirect | Traffic remained unencrypted |
| No Health Checks | Target Groups unhealthy |
| Missing Backend Services | Routes unavailable |

---

# ✅ Fix Implementation

A new production-ready ingress manifest was created.

The fixed configuration includes:

- ingressClassName
- Internet-facing ALB
- SSL Certificate
- HTTP & HTTPS Listeners
- Automatic HTTPS Redirect
- Target Group Health Checks
- Target Type IP

Example

```yaml
spec:
  ingressClassName: alb
```

Annotations

```yaml
alb.ingress.kubernetes.io/listen-ports

alb.ingress.kubernetes.io/certificate-arn

alb.ingress.kubernetes.io/ssl-redirect

alb.ingress.kubernetes.io/healthcheck-path

alb.ingress.kubernetes.io/target-type

alb.ingress.kubernetes.io/scheme
```

---

# 🚀 Deployment

Broken Version

```bash
kubectl apply -f manifests/alb-ingress.yaml
```

Production Version

```bash
kubectl apply -f manifests/alb-ingress-fixed.yaml
```

---

# ✔ Validation

Commands

```bash
kubectl get ingress

kubectl describe ingress production-alb

kubectl get svc
```

Verified

- Ingress Class = alb
- SSL Annotation Present
- HTTPS Listener Configured
- HTTP Redirect Enabled
- Health Check Enabled
- Internet Facing ALB
- Target Type IP

---

# 📊 Before vs After

| Before | After |
|----------|--------|
| HTTP Only | HTTP + HTTPS |
| No SSL | SSL Enabled |
| No Redirect | HTTP → HTTPS Redirect |
| No Health Checks | Health Checks Enabled |
| Deprecated Annotation | ingressClassName |
| Production Issues | Production Ready |

---

# 🎯 Key Learnings

- Kubernetes Ingress
- AWS Load Balancer Controller
- AWS ALB
- SSL/TLS using ACM
- HTTPS Redirect
- Target Group Health Checks
- URL Path Routing
- Production Ingress Best Practices
- Troubleshooting Kubernetes Ingress
- AWS EKS Networking

---

<div align="center">

# 👨‍💻 Author

**NIHAL N** — DevOps & Cloud Engineer

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Nihal%20N-blue?logo=linkedin)](https://www.linkedin.com/in/nihal-n-cse/)

---

**If this project helped you understand Production ALB Ingress on AWS EKS, consider giving it a ⭐**

</div>