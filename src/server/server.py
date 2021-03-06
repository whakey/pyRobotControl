#!/usr/bin/python3

import argparse
import socketserver
import serial

parser = argparse.ArgumentParser()
parser.add_argument("port")
args = parser.parse_args()


class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        ser = serial.Serial('/dev/ttyACM0', 9600)
        self.data = self.request.recv(1024)
        while self.data.decode("utf-8") != "exit" or self.data.decode("utf-8") != "":
            print("{} wrote:".format(self.client_address[0]))
            print(self.data)
            self.data = self.request.recv(1024).strip()
            ser.write(bytes(str(self.data.decode("utf-8")), "utf-8"))

if __name__ == "__main__":
    HOST, PORT = "", int(args.port)
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()
