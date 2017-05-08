import SocketServer 
import socket
import threading
import thread
import time
from blockchain.enum import *
from struct import *
from pprint import pprint

class P2PScoket:
    sockets=[]
    s=[]
    
    @staticmethod
    def broadcast(message):
        for socket in P2PScoket.sockets:
            P2PScoket.send(socket,message)
    @staticmethod
    def printf():
        pprint(P2PScoket.s)
        pprint(P2PScoket.sockets)

    def __init__(self,socket,server,client_address):
        self.socket=socket
        self.server=server
        self.client_address=client_address
        P2PScoket.sockets.append(socket)
        P2PScoket.s.append(self)
        print 'connect'
        pass
    def send(self,socket,message):
        socket.send(message)
    def checkAlive(self):
        pass
    def delsocket(self):
        P2PScoket.sockets.remove(socket)
        pass

class SocketHandle(SocketServer.BaseRequestHandler):
    def handle(self):
        client_address=self.client_address
        server=self.server
        socket=self.request
        threading.Thread(target=P2PScoket,args=(socket,server,client_address,)).start()
        while True:
            time.sleep(1)
        
class P2PScoketListen(threading.Thread):
    def __init__(self,PORT):
        super(P2PScoketListen, self).__init__()
        print("p2p listen port:"+str(PORT))
        if type(PORT)==int:
            self.server=SocketServer.TCPServer(("0.0.0.0",PORT),SocketHandle)
        if type(PORT)==str:
            self.server=SocketServer.TCPServer(("0.0.0.0",int(PORT)),SocketHandle)
    def run(self):
        self.server.serve_forever()
