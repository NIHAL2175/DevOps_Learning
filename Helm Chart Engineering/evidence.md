# Evidence Report

## Environment

Cluster

```
helm-engineering-cluster
```

Helm Version

```
v4.2.2
```

Kubectl Version

```
v1.34.1
```

---

# Evidence 1

## Helm Validation

Command

```
helm lint reusable-app
```

Result

```
1 chart(s) linted
0 chart(s) failed
```

Status

PASS

---

# Evidence 2

## Template Rendering

Command

```
helm template reusable-app
```

Verified Resources

- Deployment
- Service
- ConfigMap
- Secret
- ServiceAccount
- HPA
- Ingress

Status

PASS

---

# Evidence 3

## Helm Installation

Command

```
helm install reusable-app-dev
```

Result

```
STATUS: deployed
```

Status

PASS

---

# Evidence 4

## Kubernetes Resources

Command

```
kubectl get all
```

Verified

- Pod
- Deployment
- ReplicaSet
- Service

Pod Status

```
Running
```

Status

PASS

---

# Evidence 5

## ConfigMap

Command

```
kubectl describe configmap reusable-app-dev-config
```

Verified

```
APP_NAME=reusable-app
APP_ENV=dev
```

Status

PASS

---

# Evidence 6

## Secret

Command

```
kubectl describe secret reusable-app-dev-secret
```

Verified

```
USERNAME
PASSWORD
```

Secret Type

```
Opaque
```

Status

PASS

---

# Evidence 7

## Helm Release

Command

```
helm status reusable-app-dev
```

Verified

```
STATUS: deployed
```

Resources

- Deployment
- Pod
- ConfigMap
- Secret
- Service
- ServiceAccount

Status

PASS

---

# Overall Result

All engineering objectives completed successfully.

The reusable Helm chart is production-ready and successfully deployed on Kubernetes.