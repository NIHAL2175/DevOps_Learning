# Evidence Collection

## Evidence 1 – Application Logs

Command:

```bash
kubectl logs customer-app
```

Output:

```text
2026-05-10T08:12:13Z ERROR
botocore.exceptions.ClientError:
An error occurred (AccessDeniedException)
when calling the GetItem operation:
User: arn:aws:sts::123456789012:assumed-role/eks-nodegroup-role
is not authorized to perform:
dynamodb:GetItem
on resource:
arn:aws:dynamodb:ap-south-1:123456789012:table/customer-data
```

---

## Evidence 2 – ServiceAccount Before Fix

Command:

```bash
kubectl get sa customer-app-sa -o yaml
```

Finding:

```text
No IRSA annotation present
```

Missing:

```yaml
eks.amazonaws.com/role-arn
```

---

## Evidence 3 – Pod ServiceAccount Mapping

Command:

```bash
kubectl get pod customer-app -o yaml | findstr serviceAccount
```

Output:

```text
serviceAccount: customer-app-sa
serviceAccountName: customer-app-sa
```

Finding:

Pod correctly referenced customer-app-sa.

---

## Evidence 4 – ServiceAccount After Fix

Command:

```bash
kubectl get sa customer-app-sa -o yaml
```

Output:

```yaml
annotations:
  eks.amazonaws.com/role-arn: arn:aws:iam::123456789012:role/customer-app-irsa-role
```

Finding:

IRSA role annotation successfully configured.

---

## Evidence 5 – Successful Application Logs

Command:

```bash
kubectl logs customer-app
```

Output:

```text
Assuming IAM role via IRSA...
Successfully authenticated
DynamoDB GetItem succeeded
```

Finding:

Application successfully accessed DynamoDB using IRSA credentials.
