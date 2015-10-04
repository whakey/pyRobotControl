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

    @j.event
    def on_axis(axis, value):
        left_speed = 0
        right_speed = 0

        print('axis', axis, value)
        if axis == "left_trigger":
            left_speed = value
        elif axis == "right_trigger":
            right_speed = value
        j.set_vibration(left_speed, right_speed)

    sock.connect((HOST, PORT))
    while True:
        j.dispatch_events()
        time.sleep(.01)
        data = "mockdata"
        sock.sendall(bytes(data, "utf-8"))
        if (data == "exit"):
            break

finally:
    sock.close()

