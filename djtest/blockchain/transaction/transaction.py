import leveldb
import hashlib
import time
from blockchain.protobuf import tx_pb2
from blockchain.enum import *

class Tx:
    tx_pool=set()
    def __init__(self):
        pass
    def create(self,message):
        pb2=tx_pb2.Tx()
        pb2.channel="admin_channel"
        pb2.timestamp=int(time.time())
        pb2.type=TX_TYPE_TEST
        pb2.value=message
        pb2.version=1
        pb2.hash=""
        temp=pb2.SerializeToString()
        pb2.hash=hashlib.sha256(temp).hexdigest()
        self.tx_serialize=pb2.SerializeToString()
    @staticmethod
    def findhash(hashvalue):
        try:
            return hashvalue in Tx.tx_pool
        except:
            return -1
    @staticmethod
    def checkhash(serialize):
        pb2=tx_pb2.Tx()
        pb2.ParseFromString(serialize)
        hashvalue,pb2.hash=pb2.hash,""
        temp=pb2.SerializeToString()
        if hashvalue==hashlib.sha256(temp).hexdigest():
            return True
        else:
            return False
        pass
    def getTx(self,serialize):
        pb2=tx_pb2.Tx()
        pb2.ParseFromString(serialize)
        if Tx.findhash(pb2.hash):
            return False
        if not Tx.checkhash(serialize):
            return False
        self.tx_serialize=serialize
        Tx.tx_pool.add(pb2.hash)
        return True