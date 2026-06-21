# Evidence Collection

## Git Desired State

replicas: 3

## Cluster State During Incident

replicas: 5

## Deployment Events

Scaled up replica set payment-service from 0 to 3

Scaled up replica set payment-service from 3 to 5

## Validation Events

Scaled down replica set payment-service from 5 to 3

## Observations

Git repository and cluster configuration were different.

This caused ArgoCD to report OutOfSync.

Application health remained Healthy because all replicas were available.
