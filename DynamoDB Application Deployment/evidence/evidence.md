# Evidence Report

# Evidence 1 – Pod Failure

Command:

```bash
kubectl get pods
```

Output:

```
customer-app   0/1   CrashLoopBackOff
```

Evidence:

Application failed after deployment.

---

# Evidence 2 – Application Logs

Command:

```bash
kubectl logs customer-app
```

Output:

```
Starting customer application...
Connecting to DynamoDB...
AccessDeniedException: Unable to locate IAM credentials
```

Evidence:

AWS authentication failure.

---

# Evidence 3 – Service Account

Command:

```bash
kubectl get pod customer-app -o jsonpath="{.spec.serviceAccountName}"
```

Output:

```
default
```

Evidence:

Application deployed using the default Service Account.

---

# Evidence 4 – Service Account Details

Command:

```bash
kubectl describe serviceaccount default
```

Output:

```
Annotations:
<none>
```

Evidence:

No IAM Role associated with the Service Account.

---

# Evidence 5 – Fix Applied

Created:

```
manifests/serviceaccount.yaml
```

Created:

```
manifests/customer-app-fixed.yaml
```

Evidence:

Application updated to use an IRSA-enabled Service Account.

---

# Evidence 6 – Successful Deployment

Command:

```bash
kubectl get pods
```

Output:

```
customer-app   1/1   Running
```

Evidence:

Application successfully deployed.

---

# Evidence 7 – Successful Application Logs

Command:

```bash
kubectl logs customer-app
```

Output:

```
Starting customer application...
Connecting to DynamoDB...
IAM Role assumed successfully
Customer Read Successful
Customer Write Successful
Customer Update Successful
```

Evidence:

- IAM Role successfully assumed.
- DynamoDB Read successful.
- DynamoDB Write successful.
- DynamoDB Update successful.

---

# Conclusion

The deployment issue was caused by the absence of an IRSA-enabled Service Account. After creating an annotated Service Account and updating the application to use it, the application successfully authenticated with AWS and completed all required DynamoDB operations without using AWS Access Keys.