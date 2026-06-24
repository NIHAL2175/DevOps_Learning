# IAM / IRSA Failure Investigation

## Incident Summary

Application suddenly lost access to DynamoDB.

Observed Error:

```text
botocore.exceptions.ClientError:
An error occurred (AccessDeniedException)
when calling the GetItem operation:
User:
arn:aws:sts::123456789012:assumed-role/eks-nodegroup-role
is not authorized to perform:
dynamodb:GetItem
```

---

## Investigation Step 1 – Review Application Logs

Command:

```bash
kubectl logs customer-app
```

Finding:

Application was attempting to access DynamoDB using the worker node IAM role.

---

## Investigation Step 2 – Verify ServiceAccount

Command:

```bash
kubectl get sa customer-app-sa -o yaml
```

Finding:

ServiceAccount existed but did not contain the required IRSA annotation.

Missing:

```yaml
eks.amazonaws.com/role-arn
```

---

## Investigation Step 3 – Verify Pod Configuration

Command:

```bash
kubectl get pod customer-app -o yaml | findstr serviceAccount
```

Finding:

```text
serviceAccountName: customer-app-sa
```

The pod was correctly using the ServiceAccount.

---

## Root Cause

The ServiceAccount was missing the IRSA role annotation.

Because no IAM role was associated with the ServiceAccount, the pod inherited credentials from the EKS worker node role (eks-nodegroup-role).

The worker node role did not have permission to perform DynamoDB GetItem operations, resulting in AccessDeniedException.

---

## Corrective Action

Added:

```yaml
annotations:
  eks.amazonaws.com/role-arn: arn:aws:iam::123456789012:role/customer-app-irsa-role
```

Recreated the pod.

---

## Result

Application successfully authenticated through IRSA and DynamoDB access was restored.
