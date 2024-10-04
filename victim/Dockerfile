FROM debian:latest

RUN apt-get update && \
    apt-get install -y perl python3 python3-pip python3-pwntools

WORKDIR /app

COPY src/* /app/

CMD ["/usr/bin/python3", "server.py"]
