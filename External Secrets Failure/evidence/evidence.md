# Evidence Collection

## Evidence 1 — Application Failure

Command:

kubectl logs customer-app

Output:

FATAL:
Database password not found
Environment Variable DB_PASSWORD missing

Finding:

Application startup failed due to missing DB_PASSWORD.

---

## Evidence 2 — Pod Status

Command:

kubectl get pods

Output:

customer-app   0/1   CrashLoopBackOff

Finding:

Application continuously restarted.

---

## Evidence 3 — Missing Kubernetes Secret

Command:

kubectl get secrets

Output:

No resources found in default namespace.

Finding:

Required Kubernetes Secret did not exist.

---

## Evidence 4 — SecretStore Failure

Command:

kubectl get secretstore

Output:

aws-secretsmanager   InvalidProviderConfig   False

Finding:

SecretStore validation failed.

---

## Evidence 5 — SecretStore Error

Command:

kubectl describe secretstore aws-secretsmanager

Output:

failed to refresh cached credentials

no EC2 IMDS role found

Finding:

External Secrets Operator could not authenticate to AWS.

---

## Evidence 6 — Controller Logs

Command:

kubectl logs -n external-secrets deployment/external-secrets

Output:

unable to validate store

failed to refresh cached credentials

Finding:

AWS authentication issue confirmed.

---

## Evidence 7 — ExternalSecret Failure

Command:

kubectl describe externalsecret db-password

Output:

UnrecognizedClientException

The security token included in the request is invalid

Finding:

Invalid AWS credentials were configured.

---

## Evidence 8 — SecretStore Fixed

Command:

kubectl get secretstore

Output:

aws-secretsmanager   Valid   True

Finding:

AWS authentication restored.

---

## Evidence 9 — ExternalSecret Fixed

Command:

kubectl get externalsecret

Output:

db-password   SecretSynced   True

Finding:

Secret successfully synchronized.

---

## Evidence 10 — Secret Created

Command:

kubectl get secret db-secret

Output:

db-secret   Opaque   1

Finding:

Secret available inside Kubernetes.

---

## Evidence 11 — Application Recovery

Command:

kubectl logs customer-app

Output:

Database password loaded successfully
Application started

Finding:

Application successfully recovered.
