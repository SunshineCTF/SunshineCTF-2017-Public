TARGET := prepared

# 32-bit challenge (originally shipped with libpwnableharness32.so)
BITS := 32

# Match the original 2017 runtime (PwnableHarness base was ubuntu:16.04)
UBUNTU_VERSION := 16.04

# Docker configuration
DOCKER_IMAGE := sun17-prepared
DOCKER_PORTS := 17001
DOCKER_TIMELIMIT := 30

# Only the binary is available for download
PUBLISH_BUILD := $(TARGET)

# `pwnmake check`: run the exploit and verify it prints the flag
$(call ctf_check,$(DIR),$(DOCKER_PORTS),python3 solve.py)
