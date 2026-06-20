# Investigation Report

## Incident
Prometheus Monitoring Failure

## Symptoms
- Grafana showed No Data
- Prometheus target status showed DOWN
- Prometheus logs reported context deadline exceeded

## Investigation

Checked ServiceMonitor configuration:

port: metrics

Checked Service configuration:

name: prometheus

A mismatch was identified between the ServiceMonitor endpoint port and the Service port name.

## Root Cause

Prometheus discovers service endpoints using port names. The ServiceMonitor expected a port named metrics, but the Service exposed a port named prometheus.

Because of this mismatch, Prometheus could not discover the endpoint.

## Resolution

Updated the Service port name from prometheus to metrics using service-fixed.yaml.