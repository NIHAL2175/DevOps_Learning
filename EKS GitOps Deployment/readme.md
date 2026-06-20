<div align="center">

# 🚀 Payment Service GitOps Deployment Project ☸️

![Kubernetes](https://img.shields.io/badge/Kubernetes-K8s-blue)
![Helm](https://img.shields.io/badge/Helm-Package_Manager-blueviolet)
![ArgoCD](https://img.shields.io/badge/ArgoCD-GitOps-orange)
![Prometheus](https://img.shields.io/badge/Prometheus-Monitoring-red)
![Grafana](https://img.shields.io/badge/Grafana-Visualization-yellow)
![Docker](https://img.shields.io/badge/Docker-Containerization-blue)

<img src="architecture/arch.png" width="100%">

</div>

---

# 📖 Project Overview

This project demonstrates a complete **GitOps-based Kubernetes deployment workflow** for a microservice called **payment-service**.

The project showcases modern DevOps practices including:

* Helm Chart Deployment
* ArgoCD GitOps
* Kubernetes Secrets
* Service Accounts
* NGINX Ingress
* Prometheus Monitoring
* Grafana Dashboards
* Resource Management
* Automated Synchronization

---

# 🏗️ Architecture

```text
Developer
    │
    ▼
GitHub Repository
    │
    ▼
ArgoCD (GitOps)
    │
    ▼
Helm Chart
    │
    ▼
Kind Kubernetes Cluster
    │
 ┌──┴──────────────┐
 ▼                 ▼
Service         Deployment
                    │
                    ▼
              Payment Service Pod
                    │
                    ▼
              NGINX Ingress

Monitoring Stack
─────────────────────
Prometheus
      │
      ▼
Grafana

Security
─────────────────────
Kubernetes Secret
ServiceAccount
```

---

# 📂 Repository Structure

```text
DevOps_Learning/
│
├── .github/
│   └── workflows/
│
├── architecture/
│   └── arch.png
│
├── EKS GitOps Deployment/
│   └── helm/
│       └── payment-service/
│           ├── Chart.yaml
│           ├── values.yaml
│           └── templates/
│
└── README.md
```

---

# 🔧 Tech Stack

| Layer            | Tool              | Purpose                       |
| ---------------- | ----------------- | ----------------------------- |
| Containerization | Docker            | Package application           |
| Orchestration    | Kubernetes (Kind) | Run workloads                 |
| Package Manager  | Helm              | Kubernetes package management |
| GitOps           | ArgoCD            | Continuous deployment         |
| Monitoring       | Prometheus        | Metrics collection            |
| Visualization    | Grafana           | Dashboard monitoring          |
| Ingress          | NGINX Ingress     | Traffic routing               |
| Source Control   | GitHub            | Version control               |
| Application      | Flask             | Backend microservice          |

---

# ☸️ Kubernetes Resources

The following Kubernetes resources are deployed:

### Deployment

```yaml
Deployment
```

### Service

```yaml
ClusterIP Service
```

### Ingress

```yaml
NGINX Ingress
```

### ServiceMonitor

```yaml
Prometheus ServiceMonitor
```

### Secret

```yaml
payment-secret
```

### Service Account

```yaml
payment-service-sa
```

---

# 🚀 GitOps Workflow

```text
Code Change
     │
     ▼
Git Push
     │
     ▼
GitHub Repository
     │
     ▼
ArgoCD Detects Change
     │
     ▼
Automatic Sync
     │
     ▼
Helm Deployment Updated
     │
     ▼
Kubernetes Cluster Updated
```

---

# 🔐 Security Implementation

### Kubernetes Secret

Sensitive configuration is stored using Kubernetes Secrets.

```text
payment-secret
```

Contains:

* DB_USER
* DB_PASSWORD

### Service Account

Dedicated Service Account:

```text
payment-service-sa
```

Used by payment-service pods.

---

# 📊 Monitoring Stack

## Prometheus

Prometheus collects metrics from:

* Kubernetes Cluster
* Payment Service
* ServiceMonitor

## Grafana

Grafana dashboards display:

* CPU Usage
* CPU Utilization
* Memory Usage
* Memory Utilization
* Pod Health
* Namespace Metrics

---

# 🎯 Key Learnings

* Kubernetes Fundamentals
* Helm Package Management
* GitOps with ArgoCD
* Service Monitoring
* Grafana Dashboards
* Kubernetes Secrets
* Kubernetes Service Accounts
* Resource Management
* Ingress Configuration

---

<div align="center">

## 👨‍💻 Author

 # NIHAL N

DevOps | Cloud | Kubernetes | GitOps

⭐ If you found this project useful, consider giving it a star!

</div>
