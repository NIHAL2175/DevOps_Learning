# Investigation Report

## Investigation 1 - Node Health

Command:

```bash
kubectl get nodes
```

Finding:

```text
docker-desktop NotReady
```

Conclusion:

Node is unavailable for workload scheduling.

---

## Investigation 2 - Node Conditions

Command:

```bash
kubectl describe node docker-desktop
```

Finding:

```text
DiskPressure=True
Ready=False
```

Conclusion:

Node storage exhaustion is impacting kubelet operations.

---

## Investigation 3 - Kubelet Logs

Command:

```bash
journalctl -u kubelet
```

Finding:

```text
no space left on device
```

Conclusion:

Kubelet cannot write required files because disk capacity is exhausted.

---

## Investigation 4 - Disk Usage Analysis

Command:

```bash
du -sh /var/log/containers/*
```

Finding:

```text
95GB consumed
```

Conclusion:

Container log files are consuming the majority of available storage.

---

## Root Cause

Excessive container log growth under:

```text
/var/log/containers
```

consumed available disk capacity.

This triggered:

```text
DiskPressure=True
```

which caused the Kubernetes node to transition into:

```text
NotReady
```

state.
