# Distributed Tracing Investigation

## Metrics Investigation

Observed:

- Checkout API latency: 4.8s (P95)
- Request count normal
- Error rate normal

Conclusion:

Traffic volume is healthy.

Latency is being introduced somewhere in the service chain.

## Logs Investigation

Observed:

payment-service logs show request processing activity.

Review of application behavior shows a 4-second processing delay.

Conclusion:

payment-service is introducing significant latency before responding.

## Trace Investigation

Tempo trace shows:

checkout-service : 4.8s

inventory-service : 4.5s

payment-service : 4.2s

Observation:

payment-service consumes the majority of total request duration.

Conclusion:

Distributed tracing identifies payment-service as the latency bottleneck.

## Root Cause Analysis

Root Cause:

payment-service contains an artificial processing delay of 4 seconds.

Evidence:

- Grafana P95 latency: 4.8s
- Prometheus request count: normal
- Tempo trace: payment-service = 4.2s
- Logs show payment processing delay

Impact:

Checkout requests experience elevated latency.

Users observe slow checkout performance.

Final Root Cause:

Latency introduced by payment-service processing logic.