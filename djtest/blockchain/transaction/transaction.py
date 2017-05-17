# -*- coding: utf-8 -*-
import leveldb
import time
from uuid import *
from blockchain.protobuf import tx_pb2
from blockchain.enum import *
from blockchain import method
from blockchain import implement

class Tx:
    tx_pool=dict()
    def __init__(self):
        self.checkers=[]
    def create(self,txtype,chainid,message):
        pb2=tx_pb2.Tx()
        self.chainid=pb2.chainid=chainid
        self.timestamp=pb2.timestamp=int(time.time())
        self.type=pb2.type=txtype
        self.value=pb2.value=message
        self.version=pb2.version=1
        pb2.txhash=""
        temp=pb2.SerializeToString()
        self.txHash=pb2.txhash=method.hash(temp)
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
        if hashvalue== method.hash(temp):
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

        self.chainid=pb2.chainid
        self.version=pb2.version
        self.type=pb2.type
        self.timestamp=pb2.timestamp
        self.value=pb2.value
        self.txHash=pb2.txhash
        self.checkers.extend(pb2.checkers)
        return True
    @staticmethod
    def getTx(txhash):
        return Tx.tx_pool[txhash]

    @staticmethod
    def getTxPool():
        return Tx.tx_pool

    @staticmethod
    def clearTxPool():
        Tx.tx_pool=dict()