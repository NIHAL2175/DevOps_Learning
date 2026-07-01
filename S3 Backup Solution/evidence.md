# Evidence Report

# Evidence 1 – Project Structure

Command

```powershell
tree /F
```

Result

```
application/
config/
backup/
restore/
evidence/
Architecture/
```

Status

PASS

---

# Evidence 2 – Backup Uploaded to Amazon S3

Command

```powershell
aws s3 ls s3://nihal-s3-backup-solution-928974129633 --recursive
```

Result

```
application/app.txt
config/application.properties
```

Status

PASS

---

# Evidence 3 – Failure State

Command

```powershell
tree /F
```

Observation

```
application/

config/
```

Folders existed but contained no files.

Status

Incident Successfully Reproduced

---

# Evidence 4 – Restore Operation

Commands

```powershell
aws s3 cp s3://nihal-s3-backup-solution-928974129633/application application --recursive

aws s3 cp s3://nihal-s3-backup-solution-928974129633/config config --recursive
```

Status

Restore Completed Successfully

---

# Evidence 5 – Restored Files

Command

```powershell
tree /F
```

Result

```
application
 └── app.txt

config
 └── application.properties
```

Status

PASS

---

# Evidence 6 – File Verification

Command

```powershell
type application\app.txt

type config\application.properties
```

Result

```
Production Payment Service

ENV=production
DB_HOST=database.internal
LOG_LEVEL=INFO
```

Status

PASS

---

# Evidence 7 – Backup Verification

Command

```powershell
aws s3 ls s3://nihal-s3-backup-solution-928974129633 --recursive
```

Result

```
application/app.txt
config/application.properties
```

Status

PASS

---

# Final Evidence Summary

✓ Backup created successfully

✓ Backup stored in Amazon S3

✓ Failure state reproduced

✓ Files restored successfully

✓ Backup verified after restore

✓ Disaster recovery completed successfully