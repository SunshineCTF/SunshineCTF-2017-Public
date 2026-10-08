#!/usr/bin/env python3
# AES-CBC padding oracle. The server reveals whether PKCS#7 padding is valid
# ("Correct padding") for any submitted base64 ciphertext. The IV is the known
# "injection vector", so we recover every block including the first.
import sys, os, base64
from pwn import remote, context
context.log_level='error'
HOST=os.environ.get('HOST', sys.argv[1] if len(sys.argv)>1 else '127.0.0.1')
PORT=int(os.environ.get('PORT', sys.argv[2] if len(sys.argv)>2 else 17402))
IV=b"WHAT_IN_THE_BOOM"
CT=base64.b64decode("uRew7ow7HvGH1UF06hEiMqMENgH8A2HLpZbczI0TAFlRv87LI3F1GrBVwExYvcdykYD2laxRsDToBFrFtjp2vw==")
BS=16
def oracle(data):
    io=remote(HOST,PORT)
    io.sendline(base64.b64encode(data))
    r=io.recvline_contains(b"padding", timeout=5) if False else io.recvline(timeout=5)
    io.close()
    return b"Correct padding" in r
def decrypt_block(prev, cur):
    # returns intermediate state I = D(cur); plaintext = I ^ prev
    inter=bytearray(BS)
    for pad in range(1, BS+1):
        forged=bytearray(BS)
        for k in range(1, pad):
            forged[BS-k]=inter[BS-k]^pad
        found=False
        for g in range(256):
            forged[BS-pad]=g
            if oracle(bytes(forged)+cur):
                # guard against false positive at pad==1 (e.g. 0x02 0x02)
                if pad==1:
                    t=bytearray(forged); t[BS-2]^=0xff
                    if not oracle(bytes(t)+cur):
                        continue
                inter[BS-pad]=g^pad
                found=True
                break
        if not found:
            raise Exception("no byte for pad %d"%pad)
    return bytes(inter)
blocks=[IV]+[CT[i:i+BS] for i in range(0,len(CT),BS)]
pt=b""
for i in range(1,len(blocks)):
    inter=decrypt_block(blocks[i-1], blocks[i])
    pt+=bytes(a^b for a,b in zip(inter, blocks[i-1]))
    sys.stderr.write("block %d done\n"%i)
print(pt)
