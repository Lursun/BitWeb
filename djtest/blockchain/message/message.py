from blockchain.protobuf import message_pb2
from blockchain.protobuf import tx_pb2
from blockchain.enum import *
import blockchain.p2p as p2p_module
from blockchain.transaction import transaction

class Message:
    @staticmethod
    def recv(sock):
        data=sock.socket.recv(1024)
        try:
            msg=message_pb2.Message()
            msg.ParseFromString(data) 
            print msg.body
            if msg.type == MESSAGE_RESPONSE_TX :
                tx=transaction.Tx()
                if tx.addTx(msg.body):
                    print "GET new Tx"
                    sock.passBroadcast(data)
                else:
                    print ":)"
        except Exception as e:
            print e

    
    @staticmethod
    def send(msg_type,body):
        pb2=message_pb2.Message()
        pb2.version=1
        pb2.type=msg_type
        pb2.body=body
        message=pb2.SerializeToString()
        p2p_module.p2p.P2PScoket.broadcast(message)
        