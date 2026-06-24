# Validation Report

## Objective

Validate that the IAM / IRSA issue has been resolved and the application can successfully access DynamoDB.

---

## Validation 1 – ServiceAccount Annotation

Command:

```bash id="jlwm72"
kubectl get sa customer-app-sa -o yaml
```

Expected:

```yaml id="2n0j2z"
annotations:
  eks.amazonaws.com/role-arn: arn:aws:iam::123456789012:role/customer-app-irsa-role
```

Result:

PASS

---

## Validation 2 – Pod Health

Command:

```bash id="8w0up9"
kubectl get pods
```

Expected:

```text id="c7hz08"
customer-app   1/1 Running
```

Result:

PASS

---

## Validation 3 – Application Authentication

Command:

```bash id="yax6lc"
kubectl logs customer-app
```

Expected:

```text id="2vwhg9"
Assuming IAM role via IRSA...
Successfully authenticated
DynamoDB GetItem succeeded
```

Result:

PASS

---

## Validation Summary

| Check                         | Result |
| ----------------------------- | ------ |
| IRSA Annotation Present       | PASS   |
| Pod Running                   | PASS   |
| DynamoDB Access Successful    | PASS   |
| AccessDeniedException Removed | PASS   |

---

## Final Result

The ServiceAccount was updated with the required IRSA role annotation.

The pod successfully assumed the IAM role through IRSA and accessed DynamoDB without using the node IAM role.

Incident resolved successfully.
