TARGET := alternative_solution

BITS := 32
UBUNTU_VERSION := 16.04

DOCKER_IMAGE := sun17-alternative_solution
DOCKER_PORTS := 17101
DOCKER_TIMELIMIT := 30

# Only publish the executable
PUBLISH_BUILD := $(TARGET)

# `pwnmake check`: run the solver and verify it prints the flag
$(call ctf_check,$(DIR),$(DOCKER_PORTS),python3 solve.py)
