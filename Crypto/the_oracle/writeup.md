# The Oracle Writeup

## How it works

The server will just read in a line and first check if it is base 64 encoded properly then it will decrypt the string using AES-CBC with a hardcoded key and injection vector. The injection vector and the encrypted and base 64 encoded flag will both be given to the player.

## Solution

The player will be given hints that they must use an oracle padding attack to get the flag.
