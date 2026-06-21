# Incident Evidence

## Node Status

```text
kubectl get nodes

NAME           STATUS     ROLES           AGE
docker-desktop NotReady   control-plane   120d
```

## Node Conditions

```text
kubectl describe node docker-desktop

Conditions:
Type           Status
DiskPressure   True
Ready          False
```

## Journal Evidence

```text
journalctl -u kubelet

failed to write log
no space left on device
```

## Disk Usage

```text
du -sh /var/log/containers/*

95G /var/log/containers
```

## Impact

* Node entered NotReady state.
* New pods could not be scheduled.
* Existing workloads became unstable.
* Root cause suspected to be disk exhaustion caused by container logs.

```
```
