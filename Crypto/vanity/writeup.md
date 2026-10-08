# Vanity Writeup

## Additional notes

The vendor only checks the first four characters of the address. The solver (`solve.py`) mines a vanity key for each round: it brute-forces private keys until the resulting address matches the vendor's first four characters, then submits that key. This is probabilistic, so the solver can take a while.
