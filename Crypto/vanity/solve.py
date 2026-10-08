#!/usr/bin/env python3
# Vanity: for each round the vendor only checks the first 4 base58 chars of the
# address. Mine a private key whose uncompressed P2PKH address matches target[:4]
# (char 0 is always '1'), then submit the key as hex.
#
# Mining is sped up with incremental point addition: pick a random base scalar d0
# (one full scalar multiply), then step the public key by repeatedly adding G
# (one field inversion per step) instead of recomputing d*G from scratch each
# time. We also skip the base58check checksum while matching, since the first 4
# address characters depend only on the high-order bytes (version + hash160), not
# on the 4 trailing checksum bytes.
import sys, os, hashlib
from ecdsa.ecdsa import generator_secp256k1 as G
from pwn import remote, context
context.log_level='error'
HOST=os.environ.get('HOST', sys.argv[1] if len(sys.argv)>1 else '127.0.0.1')
PORT=int(os.environ.get('PORT', sys.argv[2] if len(sys.argv)>2 else 17401))
B58="123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
ORDER=G.order()

def b58_prefix4(payload):
    # base58-encode a 24+ byte payload and return the first 4 chars. The payload
    # starts with the 0x00 version byte (-> leading '1') + hash160; trailing
    # checksum bytes don't influence the first 4 characters.
    n=int.from_bytes(payload,'big'); s=""
    while n>0:
        n,r=divmod(n,58); s=B58[r]+s
    pad=len(payload)-len(payload.lstrip(b'\x00'))
    s=B58[0]*pad+s
    return s[:4]

def addr_prefix(point):
    pub=b'\x04'+point.x().to_bytes(32,'big')+point.y().to_bytes(32,'big')
    h160=hashlib.new('ripemd160', hashlib.sha256(pub).digest()).digest()
    return b58_prefix4(b'\x00'+h160+b'\x00\x00\x00\x00')

def mine(prefix):
    d=int.from_bytes(os.urandom(32),'big') % ORDER
    P=d*G                                   # one scalar multiply to seed
    while True:
        if addr_prefix(P)==prefix:
            return d
        d+=1
        P=P+G                               # cheap incremental step

io=remote(HOST,PORT)
for _ in range(5):
    io.recvuntil(b"Bitcoin address:")
    io.recvline()                       # blank
    target=io.recvline().strip().decode()
    d=mine(target[:4])
    io.recvuntil(b"private key(in hex, uncompressed):")
    io.sendline(format(d,'x').encode())
print(io.recvall(timeout=5).decode(errors='replace').strip().splitlines()[-1])
