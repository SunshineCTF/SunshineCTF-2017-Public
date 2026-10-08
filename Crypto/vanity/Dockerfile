FROM python:2.7

# Buster is EOL; point apt at the Debian archive so socat can still be installed.
RUN printf 'deb http://archive.debian.org/debian buster main\ndeb http://archive.debian.org/debian-security buster/updates main\n' > /etc/apt/sources.list && \
	apt-get -o Acquire::Check-Valid-Until=false update && \
	apt-get install -y socat && \
	rm -rf /var/lib/apt/lists/*
RUN pip install pybitcoin

WORKDIR /chall
COPY chall.py flag.txt run.sh ./

EXPOSE 40001
CMD ["./run.sh"]
