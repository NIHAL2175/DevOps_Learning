# Evidence Collection

## Application Logs

```text
INFO Payment processed
```

Status:

```text
PASS
```

---

## Alloy Logs

```text
failed to push logs
HTTP 403
```

Status:

```text
FAIL
```

---

## Loki Logs

```text
authentication failed
```

Status:

```text
FAIL
```

---

## Failure Point

```text
Application
    ↓
Alloy
    ↓
HTTP 403
    ↓
Loki Authentication Failure
    ↓
Grafana No Logs
```
