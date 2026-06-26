# Evidence Report

## Exercise

Exercise 8 – Egress Restriction Incident

## Evidence Collected

### Pod Status

Command:

```bash
kubectl get pods
```

Observation:

* `egress-test` pod was in the **Running** state.
* No container restart failures were observed.

---

### Application Logs

Command:

```bash
kubectl logs egress-test
```

Observation:

```text
Starting application...
Trying to access DynamoDB...
healthy: dynamodb.ap-south-1.amazonaws.com
Connection timeout
```

---

### Pod Description

Command:

```bash
kubectl describe pod egress-test
```

Observation:

* Container started successfully.
* No Kubernetes scheduling issues.
* No restart events.

---

### Network Policies

Command:

```bash
kubectl get networkpolicy -A
```

Observation:

```text
No resources found
```

Conclusion:

No Kubernetes Network Policies were blocking outbound traffic.

---

### Kubernetes Services

Command:

```bash
kubectl get svc
```

Observation:

* `kubernetes`
* `payment-service`

No DynamoDB-related Kubernetes Service exists because DynamoDB is an AWS-managed service.

---

### Infrastructure Investigation (AWS)

Security Groups:

* Outbound HTTPS (TCP 443) rule missing.

Route Tables:

* Private subnet had no route to a NAT Gateway.

VPC Endpoint:

* DynamoDB Gateway VPC Endpoint was not configured.

---

## Final Evidence Summary

| Component           | Result                        |
| ------------------- | ----------------------------- |
| Pod Health          | ✅ Healthy                     |
| Application Logs    | ✅ Connection timeout observed |
| Network Policies    | ✅ Not the cause               |
| Kubernetes Services | ✅ Not the cause               |
| Security Groups     | ❌ Misconfigured               |
| Route Tables        | ❌ Missing NAT route           |
| VPC Endpoint        | ❌ Missing                     |
