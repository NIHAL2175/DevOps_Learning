Prometheus Monitoring Failure

## Incident

Metrics disappeared from Grafana.

### Symptoms

Grafana:
```text
No Data
```

Prometheus Targets:
```text
payment-service DOWN
```

Prometheus Logs:
```text
context deadline exceeded
```

ServiceMonitor:
```yaml
port: metrics
```

Service:
```yaml
port:
  name: prometheus
```

---

## Investigation

The ServiceMonitor was configured to scrape a port named:

```yaml
port: metrics
```

However, the Kubernetes Service exposed the metrics endpoint using:

```yaml
name: prometheus
```

Prometheus uses the ServiceMonitor to discover targets. Since the port names did not match, Prometheus could not find the correct endpoint.

---

## Root Cause

Port name mismatch between ServiceMonitor and Service.

Expected:

```yaml
port: metrics
```

Found:

```yaml
name: prometheus
```

Because of this mismatch, Prometheus could not scrape metrics and marked the target as DOWN.

---

## Impact

- Prometheus target became DOWN
- Metrics collection stopped
- Grafana dashboards showed No Data

---

## Fix

### Option 1

Update Service port name:

```yaml
ports:
- name: metrics
```

### Option 2

Update ServiceMonitor:

```yaml
endpoints:
- port: prometheus
```

Ensure both configurations reference the same port name.

---

## Validation

Verify Prometheus targets:

```bash
kubectl port-forward svc/prometheus-k8s 9090
```

Open:

```text
http://localhost:9090/targets
```

Expected:

```text
payment-service UP
```

Verify metrics endpoint:

```bash
curl http://payment-service:8080/metrics
```

Metrics should be visible again in Grafana.

---

## Conclusion

The monitoring outage was caused by a configuration mismatch between the ServiceMonitor and the Kubernetes Service. Aligning the port names restored Prometheus scraping and Grafana metrics.