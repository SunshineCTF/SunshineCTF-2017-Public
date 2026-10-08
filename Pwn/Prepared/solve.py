#!/usr/bin/env python3
import sys, os, time, ctypes
from pwn import remote, context
context.log_level='error'
HOST=os.environ.get('HOST', sys.argv[1] if len(sys.argv)>1 else '127.0.0.1')
PORT=int(os.environ.get('PORT', sys.argv[2] if len(sys.argv)>2 else 17001))
libc=ctypes.CDLL("libc.so.6")
io=remote(HOST,PORT)
# seed matches server's time(NULL); use current second
libc.srand(ctypes.c_uint(int(time.time())))
for i in range(50):
    io.recvuntil(b"without an incident.\n")
    n=libc.rand()%100
    io.sendline(str(n).encode())
data=io.recvall(timeout=3)
print(data.decode(errors='replace'))
