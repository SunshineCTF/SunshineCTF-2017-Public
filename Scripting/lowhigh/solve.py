#!/usr/bin/env python3
# python3 port: binary search each round using Higher/Lower feedback, mirroring
# the server's own (low+high)//2 search so the guess budget matches. The pty
# emits an extra blank line per response, which we skip.
import sys, os
from pwn import remote, context
context.log_level='error'
HOST=os.environ.get('HOST', sys.argv[1] if len(sys.argv)>1 else '127.0.0.1')
PORT=int(os.environ.get('PORT', sys.argv[2] if len(sys.argv)>2 else 17202))
def rline(io):
    while True:
        l=io.recvline().strip()
        if l: return l
def attempt():
    io=remote(HOST,PORT)
    try:
        for run in range(1,16):
            io.recvuntil(b"High: "); high=int(io.recvline().strip()); low=0
            while True:
                io.recvuntil(b"Input a value:")
                g=(low+high)//2; io.sendline(str(g).encode())
                r=rline(io)
                if b"Correct" in r: break
                if b"Higher" in r: low=g
                elif b"Lower" in r: high=g
                else: return None
        data=io.recvall(timeout=4).decode(errors='replace')
        for ln in data.splitlines():
            if "sun{" in ln: return ln.strip()
    except EOFError: return None
    finally: io.close()
    return None
for _ in range(20):
    f=attempt()
    if f: print(f); break
