#!/bin/bash
# The flag is returned in a custom "flag:" HTTP response header.
HOST="${URL:-${1:-http://127.0.0.1:17301}}"
curl -s -D - -o /dev/null "$HOST/index.php" | grep -i '^flag:' | grep -o 'sun{[^}]*}'
