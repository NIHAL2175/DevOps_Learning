# Evidence – Complete Production Outage

## Evidence 1 – Pod Status

Command

```bash
kubectl get pods
```

Result

* payment-service: Running
* No CrashLoopBackOff
* No ImagePullBackOff

Conclusion

The Kubernetes platform was healthy.

---

## Evidence 2 – Application Logs

Command

```bash
kubectl logs payment-service
```

Failure Output

```text
Starting payment-service...
ERROR: Cannot connect to Redis
HTTP 503 Service Unavailable
```

Conclusion

The application failed while connecting to Redis.

---

## Evidence 3 – Kubernetes Secret

Command

```bash
kubectl describe secret db-secret
```

Observation

* Secret exists.
* Managed by External Secrets.
* Contains DB_PASSWORD.

Conclusion

The Kubernetes Secret was available.

---

## Evidence 4 – External Secret

Command

```bash
kubectl describe externalsecret db-password
```

Observation

* Refresh Interval: 1 minute
* SecretSynced: True
* Previous UpdateFailed events recorded.

Conclusion

External Secrets synchronized the Kubernetes Secret, but earlier synchronization failures were observed.

---

## Evidence 5 – Redis (Exercise Scenario)

Expected Redis Log

```text
Authentication failed
```

Conclusion

Redis rejected the application because it received an invalid password.

---

## Evidence 6 – Validation After Fix

Command

```bash
kubectl logs payment-service
```

Output

```text
Starting payment-service...
Loading updated Kubernetes Secret...
Connecting to Redis...
Redis authentication successful
Application started successfully
```

Conclusion

The application successfully authenticated with Redis after the fix.
