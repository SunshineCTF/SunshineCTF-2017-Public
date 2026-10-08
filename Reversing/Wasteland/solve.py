#!/usr/bin/env python3
# Full intended solve traverses all four paths; the simplest flag path is "End":
# end_of_journey() compares the first 5 chars of our line to the contents of
# file "0" (the assembled end string) and prints the flag on match.
import sys, os
from pwn import remote, context
context.log_level='error'
HOST=os.environ.get('HOST', sys.argv[1] if len(sys.argv)>1 else '127.0.0.1')
PORT=int(os.environ.get('PORT', sys.argv[2] if len(sys.argv)>2 else 17102))
END="1dt6SE89dNEOnAdBzxtNllxgfH3VJCyJRWm9tDnanQJMkzSF2CKSKSTSkZDvTSkZDvheYsdA9ueFUJPeOzcTwoSPq5OpuLrhAzD35myz3XV38K2aQlqv1vZIfJNcM1HyiaLk88CO4MdeXbQIJdThWqicmv1pKjo3V5gGON0jcRQJGpcedJNEQPc2rY"
io=remote(HOST,PORT)
io.sendline(b"End")
io.sendline(END.encode())
print(io.recvall(timeout=3).decode(errors='replace'))
