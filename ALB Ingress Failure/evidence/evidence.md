# Evidence Collection

## Incident Information

**Exercise:** Exercise 7 – ALB Ingress Failure

**Incident:**
Application inaccessible through AWS ALB Ingress.

**User Error:**

```text
504 Gateway Timeout
```

---

# Evidence 1 – Application Pods

## Command

```bash
kubectl get pods
```

## Output

```text
payment-service-59d96b6f8c-74bmk   1/1 Running
payment-service-59d96b6f8c-7gnfz   1/1 Running
payment-service-59d96b6f8c-cn6v8   1/1 Running
payment-service-59d96b6f8c-ld2rf   1/1 Running
payment-service-59d96b6f8c-wctjt   1/1 Running
```

### Observation

* Application Pods are healthy.
* No CrashLoopBackOff.
* No container failures.

---

# Evidence 2 – Service Verification

## Command

```bash
kubectl get svc
```

## Output

```text
payment-service   ClusterIP   10.96.200.121   80/TCP
```

### Observation

* Kubernetes Service exists.
* Backend service is healthy.

---

# Evidence 3 – Ingress Verification

## Command

```bash
kubectl get ingress
```

## Output

```text
NAME              CLASS    HOSTS   ADDRESS   PORTS
payment-ingress   <none>   *                 80
```

### Observation

* Ingress resource exists.
* ADDRESS field is empty.
* External Load Balancer was not provisioned.

---

# Evidence 4 – Ingress Description

## Command

```bash
kubectl describe ingress payment-ingress
```

## Important Findings

* Ingress annotation:

```yaml
alb.ingress.kubernetes.io/target-type: ip
```

* No ALB address assigned.

---

# Evidence 5 – AWS Load Balancer Controller

## Command

```bash
kubectl logs -n kube-system deployment/aws-load-balancer-controller
```

## Error

```text
Unable to discover subnets
```

---

# Evidence 6 – User Impact

Observed by users:

```text
504 Gateway Timeout
```

### Impact

* Application inaccessible.
* Requests timed out.
* ALB not created.
* Target registration failed.

---

# Conclusion

The application itself was healthy.

The Kubernetes Service was healthy.

The failure occurred because the AWS Load Balancer Controller could not discover eligible subnets required to provision the Application Load Balancer.

This prevented target registration and resulted in a 504 Gateway Timeout for end users.
