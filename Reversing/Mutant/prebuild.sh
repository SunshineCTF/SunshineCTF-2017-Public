#!/bin/bash
# Runs during pwnmake image initialization: Mutant is built with nasm + gcc
# directly in the pwnmake container (see Build.mk).
set -e
apt-get update
apt-get install -y --no-install-recommends nasm gcc libc6-dev binutils
