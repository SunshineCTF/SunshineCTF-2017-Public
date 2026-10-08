#!/usr/bin/env python3
# python3 port of the original solution.py (factor the number against the word
# table and reply; FAKE NUMBER if none divide).
import sys, os
from pwn import remote, context
context.log_level='error'
HOST=os.environ.get('HOST', sys.argv[1] if len(sys.argv)>1 else '127.0.0.1')
PORT=int(os.environ.get('PORT', sys.argv[2] if len(sys.argv)>2 else 17201))
words="""2 fallout
3 survivor
5 comrade
7 nuclear
11 apocalypse
13 shelter
17 war
19 radioactive
23 atom
29 bomb
31 radiation
37 destruction
41 mushroom
43 armageddon
47 disaster
53 pollution
59 military
61 science
67 winter
71 death
73 atmosphere
79 bunker
83 soldier
89 danger
97 doomsday"""
vals=[(int(a),b) for a,b in (l.split() for l in words.splitlines())]
def sol(n):
    ans="".join(w for p,w in vals if n%p==0)
    return ans if ans else "FAKE NUMBER"
io=remote(HOST,PORT)
while b"enter" not in io.recvline().lower():
    pass
io.sendline(b"")
while True:
    line=io.recvline().strip()
    try:
        num=int(line)
    except ValueError:
        sys.stdout.write(line.decode(errors='replace')+"\n")
        # read any trailing flag line
        try: print(io.recvline().strip().decode(errors='replace'))
        except: pass
        break
    io.sendline(sol(num).encode())
