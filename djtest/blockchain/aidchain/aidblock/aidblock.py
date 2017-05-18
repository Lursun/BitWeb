#coding:utf-8
from blockchain.protobuf import aidblock_pb2
from blockchain import implement
import time
from blockchain import method
from blockchain.enum import *
from blockchain.aidchain.guess import guess
AidChain=dict();
firstBlock=NOTFOUND
def setFirstAidBlock(aidblockhash):
    firstBlock=aidblockhash

def getFirstAidBlock(aidblockhash):
    return firstBlock


def getLastAidBlock():
    block=getFirstAidBlock()
    if block != NOTFOUND:
        while block.isNext():
            block=self.getBlock(block.next())
        return block
    return NOTFOUND

def getDifficulty(self):
    if len(Package.packages)<100:
        return 'ffff4269747765620ae9968be799bcefbc9ae59490e69e97e7aba9284c696e2d59692054616e672920206c757273756e39313430313340676d61696c2e636f6d'
    else:
        """
        需更改
        """
        return '4269747765620ae9968be799bcefbc9ae59490e69e97e7aba9284c696e2d59692054616e672920206c757273756e39313430313340676d61696c2e636f6d'

class AidBlock(implement.AidBlock):
    
    def __init__(self):
        pass
    def create(self):
        self.__height=self.getHeight()
        self.__version=1
        self.__timestamp=str(time.time())
        self.__guessers=[]
        self.__difficulty=""
        self.__answer=""
        self.__previoushash=getLastAidBlock()
        self.__blockhash=""
        self.__nexthash=""
    def toString(self):
        pb2=aidblock_pb2.Aidblock()
        pb2.height=self.__height
        pb2.version=self.__version
        pb2.timestamp=self.__timestamp
        pb2.guessers.extend(self.__guessers)
        pb2.difficulty=self.__difficulty
        pb2.answer=self.__answer
        pb2.previoushash=self.__previoushash
        pb2.blockhash=self.__blockhash
        pb2.nexthash=self.__nexthash
        return pb2.SerializeToString()
    def stringToObject(self,serialize):
        pb2=aidblock_pb2.Aidblock()
        pb2.ParseFromString(serialize)
        self.__height=pb2.height
        self.__version=pb2.version
        self.__timestamp=pb2.timestamp
        self.__guessers.extend(pb2.guessers)
        self.__difficulty=pb2.difficulty
        self.__answer=pb2.answer
        self.__previoushash=pb2.previoushash
        self.__blockhash=pb2.blockhash
        self.__nexthash=pb2.nexthash

    def checkHash(self):
        temp1=pb2.blockhash
        pb2=aidblock_pb2.Aidblock()
        pb2.height=self.__height
        pb2.version=self.__version
        pb2.timestamp=self.__timestamp
        pb2.guessers.extend(self.__guessers)
        pb2.difficulty=self.__difficulty
        pb2.answer=self.__answer
        pb2.previoushash=self.__previoushash
        pb2.blockhash=""
        pb2.nexthash=""
        if temp1==method.hash(pb2.SerializeToString()):
            return True
        return False
    def computeHash(self):
        pb2=aidblock_pb2.Aidblock()
        pb2.height=self.__height
        pb2.version=self.__version
        pb2.timestamp=self.__timestamp
        pb2.guessers.extend(self.__guessers)
        pb2.difficulty=self.__difficulty
        pb2.answer=self.__answer
        pb2.previoushash=self.__previoushash
        pb2.blockhash=""
        pb2.nexthash=""
        return method.hash(pb2.SerializeToString())

    def bale(self):
        block=getLastAidBlock()
        self.__guessers.extend(guess.Guess.getGuessPool())
        
    def getHeight(self):
        return len(AidChain)