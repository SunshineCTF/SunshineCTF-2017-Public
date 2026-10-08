# docker-compose challenge; `pwnmake check` starts it, runs the solver, and tears it down.
$(call ctf_check_tcp,$(DIR),17203,python3 solve.py)
