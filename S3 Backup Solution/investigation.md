# Investigation Report

# Incident Summary

During routine maintenance, the local application and configuration files were accidentally deleted from the production server.

Since the application files were no longer available locally, a recovery process was required to restore the environment.

---

# Investigation Steps

## Step 1 – Verify Local Application Files

Command

```powershell
tree /F
```

Observation

```
application/
config/
```

Both directories existed but no files were present.

Result

Application files were missing.

---

## Step 2 – Verify Configuration Files

Command

```powershell
tree /F
```

Observation

```
config/

(Empty)
```

Result

Configuration files were also deleted.

---

## Step 3 – Verify AWS Authentication

Command

```powershell
aws sts get-caller-identity
```

Observation

AWS CLI was successfully authenticated.

Result

AWS account access verified.

---

## Step 4 – Verify Backup Availability

Command

```powershell
aws s3 ls s3://nihal-s3-backup-solution-928974129633 --recursive
```

Observation

```
application/app.txt
config/application.properties
```

Result

Backup files were safely stored in Amazon S3.

---

# Root Cause Analysis

The investigation confirmed that the backup was successfully created before the incident.

The application outage occurred because the local application and configuration files were accidentally removed from the server.

Since an S3 backup existed, the application could be recovered without recreating the files manually.

---

# Root Cause

Human Error

↓

Application files deleted

↓

Configuration files deleted

↓

Local application unavailable

↓

Recovery required

↓

Restore performed from Amazon S3

---

# Resolution Plan

• Verify S3 backup

• Restore application files

• Restore configuration files

• Validate restored data

• Confirm backup remains available in S3