# Investigation Report

## Incident

Application could not scale beyond 5 replicas.

---

## Initial Symptoms

- HPA Desired Replicas: 15
- Current Replicas: 5
- New pods remained in Pending state.
- Scheduler reported:
  ```
  0/3 nodes available: Insufficient CPU
  ```
- Cluster Autoscaler logs:
  ```
  No node group config found
  ```

---

# Investigation Steps

## Step 1 – Horizontal Pod Autoscaler (HPA)

Command

```bash
kubectl get hpa
kubectl describe hpa payment-service-hpa
```

Observation

- HPA was configured correctly.
- Minimum replicas: 5
- Maximum replicas: 15
- HPA attempted to increase replicas.

Conclusion

✅ HPA is functioning correctly.

---

## Step 2 – Kubernetes Scheduler

Command

```bash
kubectl describe pod <pending-pod>
```

Observation

```
0/3 nodes available:
Insufficient CPU
```

Conclusion

Pods could not be scheduled because the worker nodes had insufficient CPU resources.

---

## Step 3 – Cluster Nodes

Command

```bash
kubectl describe nodes
```

Observation

Worker nodes had reached their CPU capacity.

Conclusion

Additional worker nodes were required.

---

## Step 4 – Cluster Autoscaler

Command

```bash
kubectl logs deployment/cluster-autoscaler -n kube-system
```

Observation

```
No node group config found
```

Conclusion

Cluster Autoscaler failed to discover the EKS Managed Node Group.

---

# Root Cause

The Horizontal Pod Autoscaler correctly requested additional replicas.

The Kubernetes scheduler was unable to schedule new pods due to insufficient CPU resources.

The Cluster Autoscaler failed to provision additional worker nodes because the Managed Node Group auto-discovery configuration was missing or incorrect.

---

# Final Conclusion

| Component | Status |
|-----------|--------|
| HPA | ✅ Healthy |
| Scheduler | ✅ Working |
| Worker Nodes | ❌ Insufficient CPU |
| Cluster Autoscaler | ❌ Misconfigured |
| Root Cause | Missing Node Group Auto Discovery |