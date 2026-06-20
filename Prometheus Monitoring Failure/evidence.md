# Evidence

## Before Fix

ServiceMonitor

port: metrics

Service

name: prometheus

Result:
- Port mismatch detected

## After Fix

ServiceMonitor

port: metrics

Service

name: metrics

Result:
- Port names match successfully
- Monitoring configuration corrected