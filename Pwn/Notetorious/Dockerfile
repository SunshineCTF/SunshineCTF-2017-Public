# Ubuntu 18.04 still ships python2 ("python"), socat, and sudo, matching the
# original 2017 python2 service.
FROM ubuntu:18.04
LABEL maintainer="C0deH4cker <c0deh4cker@gmail.com>"

# Install python2, socat, and sudo
RUN apt-get update && \
	apt-get install -y python socat sudo && \
	rm -rf /var/lib/apt/lists/*

# Create unprivileged notetorious user
RUN groupadd -r notetorious && \
	useradd -r -g notetorious notetorious

# Create semi-privileged notetorious_auth user
RUN groupadd -r notetorious_auth && \
	useradd -r -g notetorious_auth -G notetorious notetorious_auth
COPY notetorious_auth.sudoers /etc/sudoers.d/notetorious_auth

# Make directory structure
WORKDIR /notetorious/data/vputin

# Copy files to target locations
COPY start.sh login.py notetorious.py /notetorious/
COPY flag.txt /notetorious/data/vputin/nuclear_launch_codes
COPY russian_flag.txt /notetorious/data/vputin/flag

# Randomly generate vputin's password file
RUN dd if=/dev/urandom of=/notetorious/data/vputin.password bs=1 count=64

# Set ownership and permissions
RUN chmod 0755 /notetorious/start.sh /notetorious/login.py /notetorious/notetorious.py && \
	chown root:notetorious_auth /notetorious/data && \
	chmod 0775 /notetorious/data && \
	chown root:notetorious /notetorious/data/vputin && \
	chmod 0750 /notetorious/data/vputin && \
	chown root:notetorious_auth /notetorious/data/vputin.password && \
	chmod 0640 /notetorious/data/vputin.password && \
	chown root:notetorious /notetorious/data/vputin/flag && \
	chmod 0640 /notetorious/data/vputin/flag

# This challenge listens on the following port
EXPOSE 20003

# Run `start.sh` as root. It will drop privileges for connections
WORKDIR /notetorious
CMD ["/notetorious/start.sh"]
