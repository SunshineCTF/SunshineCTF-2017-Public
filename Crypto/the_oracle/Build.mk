# docker-compose challenge; `pwnmake check` starts it, runs the solver, and tears it down.
# The solver makes many connections, so give it extra time.
CHECK_TIMEOUT := 300
$(call ctf_check_tcp_slow,$(DIR),17402,python3 solve.py)
