# docker-compose web challenge; `pwnmake check` starts it, runs the solver, and
# tears it down.
$(call ctf_check_web,$(DIR),17302,easy2.ctf.hackucf.org,bash solve.sh)
