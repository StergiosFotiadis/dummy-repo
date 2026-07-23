# Existing vulnerabilities 1-3 (unchanged placeholder)
# VULNERABILITY 1: SQL Injection
import sqlite3
conn = sqlite3.connect(':memory:')
user_input = "' OR '1'='1"
conn.execute("SELECT * FROM users WHERE name = '" + user_input + "'")

# VULNERABILITY 2: Hardcoded Credentials
password = "supersecret123"

# VULNERABILITY 3: Command Injection
import os
os.system("ls " + user_input)

# VULNERABILITY 4: Insecure Deserialization
import pickle
fake_payload = b"\x80\x04\x95\x1a\x00\x00\x00\x00\x00\x00\x00\x8c\x08__main__\x94\x8c\x04fake\x94\x93\x94)\x81\x94."
data = pickle.loads(fake_payload)
