# -*- coding: utf-8 -*-
import leveldb
import time
from uuid import *
from blockchain.protobuf import guess_pb2
from blockchain.enum import *
from blockchain.member import member
from blockchain import method
from blockchain import implement
class Guess(implement.Guess):
    guessPool=dict()
    def __init__(self):
        self.__chainids=[]

    def create(self,userID,chainids):
        pb2=guess_pb2.Guesser()
        self.__userid=userID
        self.__version="1"
        self.__chainids.extend(chainids)
        self.__guessvalue=method.hash(str(time.time()))
        self.__sign=member.Member.private.sign(self.__guessvalue)
        Guess.guessPool[method.hash(sign)]=self
        return self

    def toString(self):
        Guess.guessPool[hashvalue]
        pb2=guess_pb2.Guesser()
        pb2.userid=self.__userid
        pb2.version=self.__version
        pb2.chainids.extend(self.__chainids.extend)
        pb2.guessvalue(self.__guessvalue)
        pb2.sign=self.__sign
        return pb2.SerializeToString()

    def stringToObject(self,serialize):
        pb2=guess_pb2.Guesser()
        pb2.ParseFromString(serialize)
        self.__userid=pb2.userid
        self.__version=pb2.version
        self.__chainids.extend(pb2.chainids)
        self.__guessvalue=pb2.guessvalue
        self.__sign=pb2.sign
        if self.checkSign():
            Guess.guessPool[method.hash(sign)]=self
            return True
        return False

    def findHash(signvalue):
        return Guess.guessPool.has_key(signvalue)

    def checkHash(serialize):
        raise NotImplementedError
    
    def checkSign(self):
        return member.Member.private.verdify(self.__userid,self.__guessvalue,self.__sign)


    @staticmethod
    def getGuessPool():
        return Guess.guessPool

    @staticmethod
    def clearTxPool():
        Guess.guessPool=dict()