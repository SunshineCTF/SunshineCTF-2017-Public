TARGET := the_memory_remains

# 32-bit challenge (shipped with libpwnableharness32.so); needs glibc 2.23 from
# the original ubuntu:16.04 runtime.
BITS := 32
UBUNTU_VERSION := 16.04

# Docker configuration
DOCKER_IMAGE := sun17-the_memory_remains
DOCKER_PORTS := 17002
DOCKER_TIMELIMIT := 30

# Only the binary is available for download
PUBLISH_BUILD := $(TARGET)

# `pwnmake check`: run the exploit and verify it prints the flag
$(call ctf_check,$(DIR),$(DOCKER_PORTS),python3 exploit.py)
