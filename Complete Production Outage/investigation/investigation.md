# Investigation Report – Complete Production Outage

## Incident Summary

**Incident Time:** 

Users reported HTTP 503 Service Unavailable immediately after a successful deployment.

Although ArgoCD showed the application as Healthy and all Kubernetes resources were Running, the application was unable to serve requests.

---

## Investigation Timeline

### Step 1 – Verify ArgoCD

**Observation**

* Application status: Healthy
* Sync status: Synced

**Conclusion**

Deployment completed successfully.

---

### Step 2 – Verify Kubernetes Pods

Command:

```bash
kubectl get pods
```

**Observation**

* payment-service pod was Running.
* No CrashLoopBackOff or ImagePullBackOff.

**Conclusion**

Kubernetes infrastructure was healthy.

---

### Step 3 – Review Application Logs

Command:

```bash
kubectl logs payment-service
```

**Observation**

```
Starting payment-service...
ERROR: Cannot connect to Redis
HTTP 503 Service Unavailable
```

**Conclusion**

Application could not authenticate with Redis.

---

### Step 4 – Verify Kubernetes Secret

Command:

```bash
kubectl describe secret db-secret
```

**Observation**

* Secret exists.
* Managed by External Secrets.
* Contains DB_PASSWORD.

**Conclusion**

The application secret was present inside Kubernetes.

---

### Step 5 – Verify External Secret

Command:

```bash
kubectl get externalsecrets
kubectl describe externalsecret db-password
```

**Observation**

* Refresh interval: 1 minute
* Status: SecretSynced
* Previous UpdateFailed events observed.

**Conclusion**

External Secrets successfully manages the Kubernetes Secret, although previous synchronization failures were recorded.

---

### Step 6 – Verify Redis

**Exercise Scenario**

Redis authentication failed after the password stored in AWS Secrets Manager was rotated.

---

## Root Cause

The Redis password stored in AWS Secrets Manager was rotated before the application started using the updated credentials.

As a result, the application attempted to authenticate using an outdated password, causing Redis authentication failures and HTTP 503 responses even though Kubernetes resources remained healthy.
