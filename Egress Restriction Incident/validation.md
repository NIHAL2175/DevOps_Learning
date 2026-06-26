# Validation Report

## Exercise

Exercise 8 – Egress Restriction Incident

## Validation Objective

Verify that the investigation was completed successfully, the root cause was identified, and the infrastructure fix was implemented.

---

## Validation Steps

### 1. Pod Health

Command:

```bash
kubectl get pods
```

Result:

* `egress-test` pod is in the **Running** state.
* No container restarts observed.

Status: ✅ PASS

---

### 2. Application Logs

Command:

```bash
kubectl logs egress-test
```

Result:

* Application starts successfully.
* Connectivity test to the DynamoDB endpoint executes.
* Logs collected as evidence for the investigation.

Status: ✅ PASS

---

### 3. Network Policy Validation

Command:

```bash
kubectl get networkpolicy -A
```

Result:

* No Network Policies found.
* Confirmed Kubernetes was not blocking outbound traffic.

Status: ✅ PASS

---

### 4. Infrastructure Fix

Command:

```bash
kubectl get configmap egress-fix-summary
```

Result:

* `egress-fix-summary` ConfigMap created successfully.
* Simulated AWS infrastructure changes documented:

  * Outbound HTTPS rule added.
  * NAT Gateway route configured.
  * DynamoDB Gateway VPC Endpoint created.

Status: ✅ PASS

---

## Final Validation Summary

| Validation Item               | Status |
| ----------------------------- | ------ |
| Pod Running                   | ✅ PASS |
| Logs Verified                 | ✅ PASS |
| Network Policy Checked        | ✅ PASS |
| Security Group Investigation  | ✅ PASS |
| Route Table Investigation     | ✅ PASS |
| VPC Endpoint Investigation    | ✅ PASS |
| Infrastructure Fix Documented | ✅ PASS |

## Conclusion

The investigation successfully identified that the application lacked outbound connectivity to Amazon DynamoDB because of AWS networking configuration (Security Groups, Route Tables, and missing DynamoDB Gateway VPC Endpoint). The simulated infrastructure fix addresses the root cause, and all validation checks have been completed successfully.
