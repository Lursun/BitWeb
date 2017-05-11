import SocketServer 
import socket
import threading
import thread
import time
from blockchain.enum import *
from struct import *
from pprint import pprint
from blockchain.message import message as message_module

class P2PScoket:
    sockets=[]
    s=[]
    @staticmethod
    def checkAlive():
        while True:
            for sock in P2PScoket.s:
                try:
                    pass #sock.send("Are you still alive?")
                except:
                    sock.delsocket()
            time.sleep(3);
    @staticmethod
    def broadcast(message):
        for socket in P2PScoket.s:
            socket.send(message)
    def passBroadcast(self,message):
        for socket in P2PScoket.s:
            if not self==socket:
                socket.send(message)

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
        P2PScoket.sockets.append(self.socket)
        P2PScoket.s.append(self)
        recvThread=threading.Thread(target=self.recv,name="recv Thread")
        recvThread.start()
        print 'connect'
    def recv(self):
        while True:
            message_module.Message.recv(self)
            

    def send(self,message):
        self.socket.send(message)

    def delsocket(self):
        self.socket.close()
        P2PScoket.s.remove(self)
        P2PScoket.sockets.remove(self.server)

class SocketHandle(SocketServer.BaseRequestHandler):
    def handle(self):
        client_address = self.client_address
        server = self.server
        socket = self.request
        ServerThread = threading.Thread(target=P2PScoket,name="Socket",args=(socket,server,client_address,))

        ServerThread.start()
        while True:
            time.sleep(1)
    @staticmethod
    def joinNetwork(sock):
        client_address=["No","No"]
        server=["No"]
        socket=sock
        ClientThread=threading.Thread(target=P2PScoket,name="Client",args=(socket,server,client_address,))

        ClientThread.start()
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

    server_thread.start()
    checkAlive = threading.Thread(target=P2PScoket.checkAlive,name="checkAlive")

    checkAlive.start()


def P2PJoinStart(node):
    sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect(node)

    ClientThread=threading.Thread(target=SocketHandle.joinNetwork,args=(sock,))
    ClientThread.start()
    