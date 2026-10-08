# [Pwn] Notetorious

An interactive note-taking service that players connect to with netcat.

## Deployment

`./deploy.sh`

## Maintenance

I tried to setup the permissions in such a way that players cannot interfere with anything critical. If something breaks, simply redeploy the Docker container by running `./deploy.sh` again. This will erase all data.

See [writeup.md](writeup.md) for the solution.
