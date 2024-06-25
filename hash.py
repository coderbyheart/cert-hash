import hashlib
import sys

with open(sys.argv[1], 'rb') as file:
    cred_text = file.read()
cred_text = cred_text.strip()
cred_text = b"\n" + cred_text

print(hashlib.sha256(cred_text).hexdigest().upper().strip(), end="")