TARGET := wasteland

# Challenge states it is "really an x86 binary"
BITS := 32
UBUNTU_VERSION := 16.04

# Docker configuration
DOCKER_IMAGE := sun17-wasteland
DOCKER_PORTS := 17102
DOCKER_TIMELIMIT := 30

# `pwnmake check`: run the solver and verify it prints the flag
$(call ctf_check,$(DIR),$(DOCKER_PORTS),python3 solve.py)
