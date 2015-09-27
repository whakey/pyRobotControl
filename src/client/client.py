#!/usr/bin/python3

import argparse
import socket
import sys

parser = argparse.ArgumentParser()
parser.add_argument("ip")
parser.add_argument("port")
args = parser.parse_args()

HOST, PORT = args.ip, int(args.port)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    sock.connect((HOST, PORT))
    sock.sendall(bytes("testdata"), "utf-8")
    received = str(sock.recv(1024))
finally:
    sock.close()

print("Sent:     {}".format(data))
print("Received: {}".format(received))

