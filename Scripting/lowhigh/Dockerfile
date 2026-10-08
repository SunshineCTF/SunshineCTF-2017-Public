# Ubuntu 18.04 still ships python2 ("python") and socat, matching the original
# 2017 python2 service.
FROM ubuntu:18.04

RUN apt-get update && \
	apt-get install -y python socat && \
	rm -rf /var/lib/apt/lists/*

WORKDIR /challenge

COPY run.sh server.py flag.txt ./

EXPOSE 30002
CMD ["./run.sh"]
