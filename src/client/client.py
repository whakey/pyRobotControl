#!/usr/bin/python3

import argparse
import socket
import xinput

parser = argparse.ArgumentParser()
parser.add_argument("ip")
parser.add_argument("port")
args = parser.parse_args()

HOST, PORT = args.ip, int(args.port)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:

    joysticks = XInputJoystick.enumerate_devices()
    device_numbers = list(map(attrgetter('device_number'), joysticks))
    j = joysticks[0]

    sock.connect((HOST, PORT))
    while True:
        data = input("Data to send\n")
        sock.sendall(bytes(data, "utf-8"))
        received = str(sock.recv(1024))
        print("Received: {}".format(received))
        if (data == "exit"):
            break

finally:
    sock.close()

