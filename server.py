__author__ = 'RB'
 
import argparse
import socketserver
 
from threading import Thread
 
PORT = 514
HOST = "0.0.0.0"
 
class MySocketServerHandler(socketserver.BaseRequestHandler):
 
    def handle(self):
        print(self.request.recv(1024).strip())
     
 
def start_udp():
    print("Starting UDP Server at port %s " % PORT)
    server_s = socketserver.UDPServer((HOST, PORT), MySocketServerHandler)
    server_s.serve_forever()
 
 
def start_tcp():
    print("Starting TCP Server at port %s " % PORT)
    server_s = socketserver.TCPServer((HOST, PORT), MySocketServerHandler)
    server_s.serve_forever()
 
 
if __name__ == "__main__":
    print("Starting server....")
 
    parser = argparse.ArgumentParser(description='Bugtower rsyslog server')
    parser.add_argument('--tcp', help='Start TCP server', action='store_true', default=False, required=False)
    parser.add_argument('--udp', help='Start UDP server', action='store_true', default=False, required=False)
    parser.add_argument('--port', help='Port for servers', default=514, required=False)
    args = parser.parse_args()
 
    PORT = int(args.port)
 
    if args.udp:
        t = Thread(target=start_udp)
        t.start()
    if args.tcp:
        t2 = Thread(target=start_tcp)
        t2.start()
