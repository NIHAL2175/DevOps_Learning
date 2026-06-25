# Evidence Collection

## Incident Summary

Application could not scale from 5 replicas to 15 replicas.

---

# Evidence 1 – Horizontal Pod Autoscaler

Command

```bash
kubectl get hpa
```

Expected Production Output

```text
NAME                  REFERENCE                    TARGETS    MINPODS   MAXPODS   REPLICAS
payment-service-hpa   Deployment/payment-service   95%/50%    5         15        5
```

Observation

- HPA detected high CPU utilization.
- Desired replicas increased to 15.
- Current replicas remained at 5.

Result

✅ HPA was functioning correctly.

---

# Evidence 2 – Pending Pods

Command

```bash
kubectl get pods
```

Expected Production Output

```text
payment-service-1     Running
payment-service-2     Running
payment-service-3     Running
payment-service-4     Running
payment-service-5     Running

payment-service-6     Pending
payment-service-7     Pending
payment-service-8     Pending
payment-service-9     Pending
payment-service-10    Pending
```

Observation

New pods remained in the Pending state.

---

# Evidence 3 – Scheduler Events

Command

```bash
kubectl describe pod payment-service-6
```

Expected Production Output

```text
Warning  FailedScheduling

0/3 nodes available:
Insufficient CPU
```

Observation

The scheduler could not place the pods because all worker nodes had exhausted their available CPU.

---

# Evidence 4 – Cluster Autoscaler

Command

```bash
kubectl logs deployment/cluster-autoscaler -n kube-system
```

Expected Production Output

```text
No node group config found
```

Observation

The Cluster Autoscaler failed to discover the EKS Managed Node Group and therefore could not provision additional worker nodes.

---

# Evidence Summary

| Evidence | Result |
|----------|--------|
| HPA | ✅ Requested additional replicas |
| Scheduler | ❌ Insufficient CPU |
| Pending Pods | ❌ Could not be scheduled |
| Cluster Autoscaler | ❌ Node group discovery failed |

---

# Root Cause Evidence

The application did not fail because of the Deployment or HPA configuration.

The failure occurred because:

- Worker nodes reached CPU capacity.
- Cluster Autoscaler could not discover the Managed Node Group.
- No new worker nodes were created.
- Pending pods remained unscheduled.