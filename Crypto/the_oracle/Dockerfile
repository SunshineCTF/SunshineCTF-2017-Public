FROM python:2.7

# Buster is EOL; use the Debian archive so socat installs. pycrypto builds from
# source using the image's toolchain.
RUN printf 'deb http://archive.debian.org/debian buster main\ndeb http://archive.debian.org/debian-security buster/updates main\n' > /etc/apt/sources.list && \
	apt-get -o Acquire::Check-Valid-Until=false update && \
	apt-get install -y socat && \
	rm -rf /var/lib/apt/lists/* && \
	pip install pycrypto

RUN mkdir /chall
COPY src/ /chall
WORKDIR /chall
EXPOSE 40002
CMD ["./run.sh"]
