# -*- coding: utf-8 -*-
import leveldb
import hashlib
import time
from uuid import *
from blockchain.protobuf import tx_pb2
from blockchain.enum import *

class Tx:
    tx_pool=dict()
    def __init__(self):
        pass
    def create(self,txtype,circle,message):
        pb2=tx_pb2.Tx()
        pb2.circle=circle
        pb2.timestamp=int(time.time())
        pb2.type=txtype
        pb2.value=message
        pb2.version=1
        pb2.txhash=""
        temp=pb2.SerializeToString()
        pb2.txhash=hashlib.sha256(temp).hexdigest()
        self.tx_serialize=pb2.SerializeToString()
        Tx.tx_pool[pb2.txhash]=self
    @staticmethod
    def findhash(hashvalue):
        return Tx.tx_pool.has_key(hashvalue)
    @staticmethod
    def checkhash(serialize):
        pb2=tx_pb2.Tx()
        pb2.ParseFromString(serialize)
        hashvalue,pb2.txhash=pb2.txhash,""
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
    def addTx(self,serialize):
        pb2=tx_pb2.Tx()
        pb2.ParseFromString(serialize)
        if Tx.findhash(pb2.txhash):
            return False
        if not Tx.checkhash(serialize):
            return False
        self.tx_serialize=serialize
        Tx.tx_pool[pb2.txhash]=self
        return True
    @staticmethod
    def getTx(txhash):
        tx=Tx.tx_pool[txhash]
        pb2=tx_pb2.Tx()
        pb2.ParseFromString(tx.tx_serialize)
        return pb2
    @staticmethod
    def getTxPool():
        return Tx.tx_pool.keys()