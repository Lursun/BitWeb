# -*- coding: utf-8 -*-
import leveldb
import time
from uuid import *
from blockchain.protobuf import tx_pb2
from blockchain.enum import *
from blockchain import method
from blockchain import implement
from blockchain.member import member

class Tx(implement.Tx):
    tx_pool=dict()
    def __init__(self):
        pass

    def create(self,txtype,chainid,message):
        self.__chainid=chainid
        self.__version=1
        self.__type=txtype
        self.__timestamp=int(time.time())
        self.__value=message
        self.__txhash=""
        self.__checkers=[]

    def toString(self):
        pb2=tx_pb2.Tx()
        pb2.chainid=self.__chainid
        pb2.version=self.__version
        pb2.type=self.__type
        pb2.timestamp=self.__timestamp
        pb2.value=self.__value
        pb2.txhash=self.__txHash
        pb2.checkhash.extend(self.__checkers)
        return pb2.SerializeToString()

    def computeHash(self):
        pb2=tx_pb2.Tx()
        pb2.chainid=self.__chainid
        pb2.version=self.__version
        pb2.type=self.__type
        pb2.timestamp=self.__timestamp
        pb2.value=self.__value
        pb2.txhash=""
        temp=pb2.SerializeToString()
        return method.hash(temp)
    
    def checkHash(self):
        temp=self.__txhash
        pb2=tx_pb2.Tx()
        pb2.chainid=self.__chainid
        pb2.version=self.__version
        pb2.type=self.__type
        pb2.timestamp=self.__timestamp
        pb2.value=self.__value
        pb2.txhash=""
        temp2=pb2.SerializeToString()
        return method.hash(temp)==method.hash(temp2)
        
    @staticmethod
    def findhash(hashvalue):
        return Tx.tx_pool.has_key(hashvalue)

    ####待做
    def checkSign(self):
        return 2 #返回成功簽名數
    def sign(self):
        if self.checkHash():
            m=member.Member.private
            sign=m.sign(self.__txhash)
            pb2=tx_pb2.Sign()
            pb2.userid=m.userName
            pb2.sign=sign
            self.__checkers.append(pb2)
    ####
    def stringToObject(self,serialize):
        pb2=tx_pb2.Tx()
        pb2.ParseFromString(serialize)
        if Tx.findhash(pb2.txhash):
            return False
        self.__chainid=pb2.chainid
        self.__version=pb2.version
        self.__type=pb2.type
        self.__timestamp=pb2.timestamp
        self.__value=pb2.value
        self.__txHash=pb2.txhash
        self.__checkers.extend(pb2.checkers)

        if not self.checkHash(serialize):
            return False
        Tx.tx_pool[pb2.txhash]=self
        return True
    def isHash(self):
        pass
    def setHash(self,hashvalue):
        self.__txHash=hashvalue

    @staticmethod
    def getTx(txhash):
        return Tx.tx_pool[txhash]

    @staticmethod
    def getTxPool():
        return Tx.tx_pool

    @staticmethod
    def clearTxPool():
        Tx.tx_pool=dict()