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
    def checkAlive():
        while True:
            for sock in P2PScoket.s:
                try:
                    sock.send("Are you still alive?")
                except:
                    sock.delsocket()
            time.sleep(3);
    @staticmethod
    def broadcast(message):
        for socket in P2PScoket.sockets:
            P2PScoket.send(socket,message)

    @staticmethod
    def getClient():
        output=''
        for sock in P2PScoket.s:
            try:
                output+=sock.client_address[0]+":"+ str(sock.client_address[1])+"\n"
            except:
                sock.delsocket()
        return output
        

    def __init__(self,socket,server,client_address):
        self.socket=socket
        self.server=server
        self.client_address=client_address
        P2PScoket.sockets.append(self.server)
        P2PScoket.s.append(self)
        recvThread=threading.Thread(target=self.recv,name="recv Thread")
        recvThread.daemon = True
        recvThread.start()
        print 'connect'
    def recv(self):
        while True:
            data=self.socket.recv(1024)

    def send(self,message):
        self.socket.send(message)
        
    
            

    def delsocket(self):
        self.socket.close()
        P2PScoket.s.remove(self)
        P2PScoket.sockets.remove(self.server)

class SocketHandle(SocketServer.BaseRequestHandler):
    def handle(self):
        client_address=self.client_address
        server=self.server
        socket=self.request
        threading.Thread(target=P2PScoket,name="Socket",args=(socket,server,client_address,)).start()
        while True:
            time.sleep(1)
        
class ThreadedTCPServer(SocketServer.ThreadingMixIn, SocketServer.TCPServer):
    pass
def P2PNetworkStart():
    PORT=Node=""
    try:
        PORT=os.environ["P2P_CONNECT"]
    except:
        pass
    try:
        PORT=os.environ["P2P_PORT"]
    except:
        PORT=8001
    print("p2p listen port:"+str(PORT))
    if type(PORT)==int:
        server=ThreadedTCPServer(("0.0.0.0",PORT),SocketHandle)
    if type(PORT)==str:
        server=ThreadedTCPServer(("0.0.0.0",int(PORT)),SocketHandle)
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()
    checkAlive = threading.Thread(target=P2PScoket.checkAlive,name="checkAlive")
    checkAlive.daemon = True
    checkAlive.start()

        
