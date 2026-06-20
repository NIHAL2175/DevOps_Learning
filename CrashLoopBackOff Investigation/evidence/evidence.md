# Evidence Collection

## Evidence 1 – Pod Status

Before Fix

```bash
kubectl get pods
```

Output:

```text
payment-service   CrashLoopBackOff
```

---

## Evidence 2 – Application Logs

Command:

```bash
kubectl logs payment-service
```

Output:

```text
Starting payment-service...
panic:
dial tcp 10.20.0.15:5432
connection refused
```

---

## Evidence 3 – Pod Events

Command:

```bash
kubectl describe pod payment-service
```

Output:

```text
Warning  BackOff
Back-off restarting failed container
```

---

## Evidence 4 – Database Service Check

Command:

```bash
kubectl get svc | findstr postgres
```

Output:

```text
No PostgreSQL service found
```

---

## Evidence 5 – Database Pod Check

Command:

```bash
kubectl get pods
```

Output:

```text
No PostgreSQL pod found
```

---

## Evidence 6 – Secret Check

Command:

```bash
kubectl describe pod payment-service | findstr Environment
```

Output:

```text
Environment: <none>
```

---

## Evidence 7 – PostgreSQL Deployment

Command:

```bash
kubectl apply -f manifests/postgres.yaml
```

Output:

```text
pod/postgres created
service/postgres created
```

---

## Evidence 8 – Validation

Command:

```bash
kubectl logs payment-service
```

Output:

```text
Connecting to PostgreSQL...
Database connection successful
```
