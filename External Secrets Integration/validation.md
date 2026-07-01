# Validation Report

## Validation Objective

Verify that AWS Secrets Manager is successfully integrated with Kubernetes using the External Secrets Operator and that the application can consume the synchronized secret.

---

## Validation Steps

### 1. External Secrets Operator

Command:

```bash
kubectl get pods -n external-secrets
```

Expected Result:

* All External Secrets Operator components are in the `Running` state.

Status:

* **PASS**

---

### 2. SecretStore Validation

Command:

```bash
kubectl get secretstore
```

Expected Result:

```text
READY   True
```

Status:

* **PASS**

---

### 3. ExternalSecret Validation

Command:

```bash
kubectl get externalsecret
```

Expected Result:

```text
STATUS  SecretSynced
READY   True
```

Status:

* **PASS**

---

### 4. Kubernetes Secret Validation

Command:

```bash
kubectl get secret app-secret
```

Expected Result:

```text
app-secret   Opaque   3
```

Status:

* **PASS**

---

### 5. Application Validation

Command:

```bash
kubectl get pods
```

Expected Result:

```text
demo-app   1/1   Running
```

Status:

* **PASS**

---

### 6. Runtime Validation

Command:

```bash
kubectl logs demo-app
```

Expected Result:

```text
Starting Application...
Reading Kubernetes Secret...
DB_USERNAME=admin
Application Started Successfully
```

Status:

* **PASS**

---

## Final Result

All validation checks completed successfully.

The External Secrets Operator synchronized secrets from AWS Secrets Manager, automatically created the Kubernetes Secret, and the application successfully consumed the secret without any manual intervention.
