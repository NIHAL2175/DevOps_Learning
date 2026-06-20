Investigation Commands

kubectl get servicemonitor payment-service -o yaml

kubectl get svc payment-service -o yaml

kubectl get endpoints payment-service

kubectl port-forward svc/prometheus-k8s 9090

Check : http://localhost:9090/targets