# Investigation Report

## Objective

Build a reusable Helm chart that supports:

- Replica configuration
- Resource limits & requests
- ConfigMaps
- Secrets
- Ingress
- Horizontal Pod Autoscaler (HPA)
- Multiple environments
  - Development
  - QA
  - Production

---

## Investigation Summary

The default Helm chart generated using `helm create` provides only a basic Kubernetes deployment.

A detailed investigation was performed to determine whether the chart satisfied production-grade deployment requirements.

---

## Investigation Performed

### 1. Helm Chart Structure Review

Verified chart directory:

```
reusable-app/
├── Chart.yaml
├── values.yaml
├── templates/
└── charts/
```

Result:

Basic chart successfully generated.

---

### 2. Deployment Configuration Review

Checked Deployment template.

Observed:

- Replica count configurable
- Image configurable
- Resources partially configurable

Missing:

- ConfigMap integration
- Secret integration

---

### 3. Configuration Management Review

Verified external configuration support.

Observed:

No dedicated ConfigMap template.

Action Taken:

Created:

```
templates/configmap.yaml
```

Added configurable application configuration through:

```
values.yaml
```

---

### 4. Secret Management Review

Verified Secret support.

Observed:

No Secret template.

Action Taken:

Created:

```
templates/secret.yaml
```

Added configurable secret values.

---

### 5. Ingress Review

Verified ingress support.

Observed:

Ingress template already available.

Configured production values.

---

### 6. Autoscaling Review

Verified HPA support.

Observed:

HorizontalPodAutoscaler template available.

Configured:

- minReplicas
- maxReplicas
- CPU utilization threshold

---

### 7. Environment Configuration Review

Created separate environment configurations:

```
values-dev.yaml
values-qa.yaml
values-prod.yaml
```

Verified:

- Development
- QA
- Production

---

### 8. Helm Validation

Executed:

```
helm lint
```

Result:

Validation successful.

---

### 9. Template Rendering

Executed:

```
helm template
```

Verified:

- Deployment
- Service
- ConfigMap
- Secret
- HPA
- Ingress

---

### 10. Kubernetes Deployment

Installed chart into dedicated Kind cluster.

Cluster:

```
helm-engineering-cluster
```

Verified deployment completed successfully.

---

## Final Investigation Result

The reusable Helm chart satisfies all exercise requirements and supports reusable deployments across multiple environments.