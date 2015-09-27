#!/usr/bin/python3

import argparse
import socketserver

parser = argparse.ArgumentParser()
parser.add_argument("port")
args = parser.parse_args()

class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        self.request.sendall(self.data.upper())

if __name__ == "__main__":
    HOST, PORT = "", int(args.port)
    server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)
    server.serve_forever()
