# Incident Evidence

## User Complaint

Checkout API is slow.

---

## Grafana

95th Percentile Latency

4.8 seconds

---

## Prometheus

Request Rate

Normal

Error Rate

0%

---

## Tempo Trace

checkout-service
  Duration: 4.8s

inventory-service
  Duration: 4.5s

payment-service
  Duration: 4.2s

---

Observation:

Most latency originates from payment-service.