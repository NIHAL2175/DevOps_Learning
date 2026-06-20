# CrashLoopBackOff Investigation

## Incident

The payment-service pod entered CrashLoopBackOff state in Kubernetes.

Observed status:

```bash
kubectl get pods

payment-service   CrashLoopBackOff
```

## Error Logs

```text
panic:
dial tcp 10.20.0.15:5432
connection refused
```

## Investigation Performed

### 1. Log Analysis

Collected application logs using:

```bash
kubectl logs payment-service
```

Observation:

```text
dial tcp 10.20.0.15:5432
connection refused
```

### 2. Pod Events Analysis

Collected pod events using:

```bash
kubectl describe pod payment-service
```

Observation:

```text
Back-off restarting failed container
```

### 3. DNS Investigation

Checked whether the application was using DNS names.

Observation:

```text
Application was connecting directly to IP 10.20.0.15
```

Result:

```text
DNS issue ruled out.
```

### 4. Database Investigation

Checked for PostgreSQL services:

```bash
kubectl get svc | findstr postgres
```

Result:

```text
No PostgreSQL service found.
```

Checked running pods:

```bash
kubectl get pods
```

Result:

```text
No PostgreSQL pod found.
```

Conclusion:

```text
Database endpoint unavailable.
```

### 5. Secret Investigation

Checked environment variables:

```bash
kubectl describe pod payment-service
```

Result:

```text
Environment: <none>
```

Conclusion:

```text
No secret-related issue detected.
```

## Root Cause

The payment-service application attempted to connect to PostgreSQL on port 5432, but no PostgreSQL service or pod was available in the cluster. The application exited with code 1, causing Kubernetes to continuously restart the container and place the pod into CrashLoopBackOff state.
