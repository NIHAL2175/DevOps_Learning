ROOT CAUSE ANALYSIS
===================

Incident
--------
Application could not access Amazon DynamoDB.

Symptoms
--------
- Connection timeout while accessing DynamoDB.
- Application failed to communicate with the AWS service.

Investigation Summary
---------------------
1. Security Groups
   - Outbound HTTPS (TCP 443) traffic was blocked.

2. Network Policies
   - No Kubernetes Network Policies were present.
   - Eliminated as a cause.

3. Route Tables
   - Private subnet had no route to a NAT Gateway.

4. VPC Endpoints
   - No Gateway VPC Endpoint configured for DynamoDB.

Root Cause
----------
The application was running in a private subnet without outbound connectivity to AWS services. Because there was no NAT Gateway route and no DynamoDB Gateway VPC Endpoint, requests to DynamoDB timed out.

Recommended Fix
---------------
- Allow outbound HTTPS (TCP 443) in the Security Group.
- Add a NAT Gateway route for private subnets or create a DynamoDB Gateway VPC Endpoint.
- Validate connectivity after the changes.