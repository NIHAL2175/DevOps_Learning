# Investigation Report

## Incident

ArgoCD reported:

Status: OutOfSync
Health: Healthy

## Investigation Steps

### 1. Verify Desired State

Deployment manifest in Git:

replicas: 3

### 2. Verify Live Cluster State

Command:

kubectl get deploy payment-service

Result:

replicas: 5

### 3. Deployment Analysis

Command:

kubectl describe deploy payment-service

Evidence:

Scaled up replica set payment-service from 3 to 5

### 4. Rollout History

Command:

kubectl rollout history deployment/payment-service

Result:

Revision 1

### 5. Root Cause

A manual scaling operation changed the deployment replica count from 3 to 5 directly in the cluster.

The change bypassed the GitOps workflow.

ArgoCD detected configuration drift and reported OutOfSync.

## Why Health Was Healthy

All pods were running successfully.

The application was operational even though desired and actual states differed.
