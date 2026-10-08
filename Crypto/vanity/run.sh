#!/bin/bash
socat tcp4-l:40001,reuseaddr,fork EXEC:"python chall.py",pty,ctty,echo=0
