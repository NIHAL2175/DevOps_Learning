# Investigation Report

## Exercise

Exercise 8 – Egress Restriction Incident

## Incident

Application could not access Amazon DynamoDB.

## Symptoms

* Connection timeout while connecting to DynamoDB.
* Application connectivity to AWS service failed.

## Investigation Performed

### 1. Security Groups

* Reviewed outbound security group rules.
* Expected HTTPS (TCP 443) access was missing.
* Result: Failed.

### 2. Kubernetes Network Policies

Command:

```
kubectl get networkpolicy -A
```

Observation:

```
No resources found
```

Result:
No Network Policies were blocking outbound traffic.

### 3. Route Tables

* Private subnet did not have a route to a NAT Gateway.
* Result: Failed.

### 4. VPC Endpoint

* No DynamoDB Gateway VPC Endpoint configured.
* Result: Failed.

## Root Cause

The application was deployed in a private subnet without outbound connectivity to AWS services. Since neither a NAT Gateway route nor a DynamoDB Gateway VPC Endpoint existed, requests to DynamoDB timed out.

## Recommended Fix

* Allow outbound HTTPS (TCP 443).
* Configure NAT Gateway routing for private subnets or create a DynamoDB Gateway VPC Endpoint.
* Validate application connectivity after implementation.
