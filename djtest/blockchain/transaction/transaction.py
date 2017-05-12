# -*- coding: utf-8 -*-
import leveldb
import hashlib
import time
from uuid import *
from blockchain.protobuf import tx_pb2
from blockchain.enum import *

class Tx:
    tx_pool=set()
    def __init__(self):
        pass
    def create(self,txtype,circle,message):
        pb2=tx_pb2.Tx()
        pb2.uuid=str(uuid1())
        pb2.circle=circle
        pb2.timestamp=int(time.time())
        pb2.type=txtype
        pb2.value=message
        pb2.version=1
        pb2.hash=""
        temp=pb2.SerializeToString()
        pb2.hash=hashlib.sha256(temp).hexdigest()
        Tx.tx_pool.add(pb2.hash)
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
    ####待做
    def checksign(self):
        return 2 #返回成功簽名數
    def sign(self):
        pass
    ####
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
    @staticmethod
    def getTxPool():
        ret_tx_pool=Tx.tx_pool
        tx_pool=set()
        for tx in ret_tx_pool:
            if not Tx.checkhash(tx):
                ret_tx_pool.remove(tx)
            if not (tx.checksign>1):
                tx_pool.add(tx)
                ret_tx_pool.remove(tx)
        #####待做
        
        return ret_tx_pool