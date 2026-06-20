# Validation Report

## Validation Steps

1. Verified ServiceMonitor configuration.
2. Verified Service configuration.
3. Confirmed port-name mismatch.
4. Applied corrected Service configuration.
5. Verified Service port name changed to metrics.
6. Confirmed ServiceMonitor and Service use the same port name.

## Result

Validation successful.

ServiceMonitor:
- port: metrics

Service:
- name: metrics

Prometheus can now successfully discover the endpoint.