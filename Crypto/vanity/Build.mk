# docker-compose challenge; `pwnmake check` starts it, runs the solver, and tears it down.
# The solver is slow, so it needs longer.
CHECK_TIMEOUT := 300
$(call ctf_check_tcp_slow,$(DIR),17401,python3 solve.py)
