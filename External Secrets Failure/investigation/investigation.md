# External Secrets Failure Investigation

## Incident

Application startup failure.

## Symptoms

Application logs:

FATAL:
Database password not found
Environment Variable DB_PASSWORD missing

Pod Status:

CrashLoopBackOff

---

## Investigation

### Application Investigation

Observed:

* Application failed during startup.
* DB_PASSWORD environment variable missing.

Evidence:

kubectl logs customer-app

Output:

FATAL:
Database password not found
Environment Variable DB_PASSWORD missing

---

### Kubernetes Investigation

Observed:

kubectl get secrets

Output:

No resources found in default namespace.

Finding:

No Kubernetes Secret existed.

---

### SecretStore Investigation

Observed:

kubectl describe secretstore aws-secretsmanager

Output:

InvalidProviderConfig

failed to refresh cached credentials

no EC2 IMDS role found

Finding:

External Secrets Operator unable to authenticate to AWS.

---

### Controller Investigation

Observed:

kubectl logs -n external-secrets deployment/external-secrets

Output:

failed to refresh cached credentials

no EC2 IMDS role found

Finding:

AWS credentials unavailable.

---

### ExternalSecret Investigation

Observed:

kubectl describe externalsecret db-password

Output:

UnrecognizedClientException

The security token included in the request is invalid

Finding:

Invalid AWS credentials stored in Kubernetes Secret.

---

## Root Cause

External Secrets Operator could not authenticate to AWS Secrets Manager.

As a result:

* SecretStore validation failed
* ExternalSecret sync failed
* Kubernetes Secret was not created
* DB_PASSWORD was unavailable
* Application entered CrashLoopBackOff
