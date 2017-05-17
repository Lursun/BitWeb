# -*- coding: utf-8 -*-
import leveldb
import hashlib
import time
from uuid import *
from blockchain.protobuf import guess_pb2
from blockchain.enum import *
from blockchain.member import member
from blockchain import method
class Guess:
    guessPool=dict()
    def __init__(self):
        self.chainids=[]
        pass
    def create(self,chainids):
        pb2=guess_pb2.Guesser()
        self.userid="Lursun"
        self.version="1"
        self.chainids.extend(chainids)
        self.guessvalue=method.hash(str(time.time()))
        self.sign=member.Member.private.sign(self.guessvalue)
        Guess.guessPool[method.hash(sign)]=self
        return self
    def getSerialize(hashvalue):
        Guess.guessPool[hashvalue]
        pb2=guess_pb2.Guesser()
        pb2.userid=self.userid
        pb2.version=self.version
        pb2.chainids.extend(self.chainids.extend)
        pb2.guessvalue(self.guessvalue)
        pb2.sign=self.sign
        return self.tx_serialize
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