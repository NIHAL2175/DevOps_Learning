# Validation Report

## Pre-Fix State

Grafana P95 Latency: 4.8s

Tempo Trace:

checkout-service : 4.8s
inventory-service : 4.5s
payment-service : 4.2s

Result:

Checkout API slow.

---

## Fix Applied

Reduced payment-service processing delay.

Before:

sleep 4

After:

sleep 1

---

## Post-Fix State

Grafana P95 Latency: 1.4s

Tempo Trace:

checkout-service : 1.4s
inventory-service : 1.2s
payment-service : 1.0s

---

## Final Result

Latency bottleneck removed.

Checkout API performance restored.