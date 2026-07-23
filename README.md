# Vulnerable Fixture

This repository is a deliberately vulnerable code fixture evaluated by SecureScan.

## Vulnerability Inventory

| # | Class | Location | Reference |
|---|-------|----------|-----------|
| 1 | SQL Injection | `main.py` | Unsanitized user input in SQL query |
| 2 | Hardcoded Credentials | `main.py` | Plaintext password assignment |
| 3 | Command Injection | `main.py` | Unsanitized input passed to `os.system()` |
| 4 | Insecure Deserialization | `main.py` — `pickle.loads()` call; `requirements.txt` — `PyYAML==5.3.1` | CVE-2020-14343; unsafe `pickle.loads()` on untrusted data with no safe-load alternative |

## Scan-Trigger Log

- VULNERABILITY 1: SQL Injection — added
- VULNERABILITY 2: Hardcoded Credentials — added
- VULNERABILITY 3: Command Injection — added
- VULNERABILITY 4: Insecure Deserialization — added (`pickle.loads()` in `main.py`; `PyYAML==5.3.1` pin, CVE-2020-14343, in `requirements.txt`)
