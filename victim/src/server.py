from pwn import *
import os

ENVIRONMENT = os.environ.copy()
HELP = """
USAGE:
    r               reset the env
    d               display the env
    [KEY]=[VALUE]   create an environment variable named KEY with the value VALUE
    python          start a python process with the custom environment
    perl            start a perl process with the custom environment
"""


def handle_message(client: listen, message: bytes) -> None:
    global ENVIRONMENT
    print("DEBUG: ", message)

    if message == b"r\n":
        ENVIRONMENT = os.environ.copy()
        client.send("Environment reset\n")
    elif b"=" in message:
        msg_str = message.decode()
        arr = msg_str.split("=")
        key = arr[0]
        val = arr[1]
        ENVIRONMENT[key] = val.strip()
    elif message == b"d\n":
        client.send(str(ENVIRONMENT) + "\n")
    elif message == b"python\n":
        process(["/usr/bin/python3", "do_nothing.py"], env=ENVIRONMENT)
        client.send("successfully ran python\n")
    elif message == b"perl\n":
        process(["/usr/bin/perl", "do_nothing.pl"], env=ENVIRONMENT)
        client.send("successfully ran perl\n")
    else:
        client.send(HELP)


def start_server(host="0.0.0.0", port=12345):
    server = listen(port, bindaddr=host)
    print(f"Server listening on {host}:{port}...")

    client = server.wait_for_connection()
    client_address = client.sock.getpeername()
    print(f"Connection from {client_address}")

    while True:
        data = client.recv()
        if not data:
            break
        handle_message(client, data)
        print(f"Received message: {data.decode('utf-8')}")

    client.close()
    print(f"Connection closed: {client_address}")


if __name__ == "__main__":
    start_server()
