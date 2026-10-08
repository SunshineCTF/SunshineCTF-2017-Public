# Prepared Writeup

This is a simple challenge, where a random number generator uses system time as a seed. Just get the same seed, generate the same sequence, and pipe it into the program. Using the exploit binary, just type:

```bash
./exploit | nc pwn.sunshinectf.org 20001
```
