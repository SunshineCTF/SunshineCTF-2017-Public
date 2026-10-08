#!/usr/bin/env python3
# python3 port of solution.py: BFS the printed maze from P to E and walk the
# shortest path (server only accepts distance-reducing "optimal" moves).
import sys, os
from collections import deque
from pwn import remote, context
context.log_level='error'
HOST=os.environ.get('HOST', sys.argv[1] if len(sys.argv)>1 else '127.0.0.1')
PORT=int(os.environ.get('PORT', sys.argv[2] if len(sys.argv)>2 else 17203))
def bfs(grid):
    H=len(grid); W=max(len(r) for r in grid)
    g=[r.ljust(W) for r in grid]
    start=end=None
    for r in range(H):
        for c in range(W):
            if g[r][c]=='P': start=(r,c)
            elif g[r][c]=='E': end=(r,c)
    dr=[-1,1,0,0]; dc=[0,0,-1,1]; mv=['U','D','L','R']
    prev={start:None}; q=deque([start])
    while q:
        cur=q.popleft()
        if cur==end: break
        for i in range(4):
            nr,nc=cur[0]+dr[i],cur[1]+dc[i]
            if 0<=nr<H and 0<=nc<W and g[nr][nc] in ' PE' and (nr,nc) not in prev:
                prev[(nr,nc)]=(cur,mv[i]); q.append((nr,nc))
    path=[]; cur=end
    while prev[cur] is not None:
        p,m=prev[cur]; path.append(m); cur=p
    return ''.join(reversed(path))
io=remote(HOST,PORT)
io.recvuntil(b"Press enter to begin")
io.sendline(b"")                      # begin
for maze_num in range(10):
    io.recvuntil(b"Number of rows:"); rows=int(io.recvline().strip())
    io.recvuntil(b"Number of columns:"); io.recvline()
    grid=[io.recvline().rstrip(b"\r\n").decode() for _ in range(rows)]
    path=bfs(grid)
    for m in path:
        io.recvuntil(b"Enter your move:")
        io.sendline(m.encode())
    io.recvuntil(b"Press enter to continue")
    io.sendline(b"")                  # continue / final flag trigger
print(io.recvall(timeout=5).decode(errors='replace').strip().splitlines()[-1])
