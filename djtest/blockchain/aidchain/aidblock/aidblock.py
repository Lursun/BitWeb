#coding:utf-8
from blockchain.protobuf import aidblock_pb2
from blockchain import implement
from blockchain import method
from blockchain.enum import *
from blockchain.aidchain.guess import guess
from fractions import Fraction
from blockchain.message import message
import random
import time
AidChain=dict();
firstBlockHash=NOTFOUND

heightWillReach=None

def addAidChain(aidblock):
    AidChain[aidblock.getBlockHash()]=aidblock

def setFirstAidBlockHash(aidblockhash):
    global firstBlockHash
    firstBlockHash=aidblockhash

def getFirstAidBlockHash():
    return firstBlockHash
    
def getBlockFromHash(aidblockhash):
    return AidChain[aidblockhash]

def getBlockFromHeight(height):
    blockhash=getFirstAidBlockHash()
    while height > 0: 
        block=getBlockFromHash(blockhash)
        if block.isNextHash():
            blockhash=block.getNextHash()
            height-=1
        else:
            break
    return AidChain[aidblockhash]

def getHeight():
        blockhash=getFirstAidBlockHash()
        if blockhash != NOTFOUND:
            block=getBlockFromHash(blockhash)
            i=1
            while block.isNextHash():
                i+=1
                block=getBlockFromHash(block.getNextHash())
            return i
        return 0

def getDifficulty():
    h=getHeight()
    if h<100:
        return "ffff4269747765620ae9968be799bcefbc9ae59490e69e97e7aba9284c696e2d59692054616e672920206c757273756e39313430313340676d61696c2e636f6d"
    i=h-h%100
    blockhash=getFirstAidBlockHash()
    temp=[]
    block=getBlockFromHash(blockhash)
    
    #演算法尚可優化
    while True:
        temp.append(block.getTimestamp())
        if i>100:
            temp.pop(0)
        if i <= 1:
            break
        block=getBlockFromHash(block.getNextHash())
        i-=1
    j=total=0

    while j<99:
        sub=temp[j+1]-temp[j]
        if sub<0 or sub>=86400:
            sub=60
        total+=sub
        j+=1
    diff=block.theBlockDifficulty()
    return format(int(int(diff,16)*Fraction(total)/6000),"x")

def setHeightTarget(heightTarget):
    global heightWillReach
    heightWillReach=heightTarget

def recv(serialize):
    aidblock=AidBlock()
    aidblock.stringToObject(serialize)
    if aidblock.checkHash():
        currentHeight=getHeight()
        if aidblock.theBlockHeight()-currentHeight==1:
            if getLastAidBlock().getBlockHash()==aidblock.getPreviousHash():
                getLastAidBlock().setNextHash( aidblock.getBlockHash() )
                if getHeight() <= currentHeight:
                    raise Exception('Impossible at getNewBlock')
                return True
        if heightWillReach is None and aidblock.theBlockHeight()-currentHeight>=2:
            setHeightTarget(currentHeight+1)
            requestHeight(currentHeight+1)
        elif aidblock.theBlockHeight()==heightWillReach :
            if getLastAidBlock().getBlockHash()==aidblock.getPreviousHash():
                getLastAidBlock().setNextHash( aidblock.getBlockHash() )
                if getHeight() <= currentHeight:
                    raise Exception('Impossible Error getNewBlock')
                setHeightTarget(currentHeight+1)
                requestHeight(currentHeight+1)
                print "getOldBlock\n and I want Block %d" % heightWillReach+1
                return True
            else:
                if heightWillReach !=1:
                    setHeightTarget(heightWillReach-1)
                    requestHeight(heightWillReach-1)
                    print "I want Block %d" % heightWillReach-1
                    return True
                else:
                    raise Exception('Impossible Error getOldBlock')



def getLastAidBlock():
    blockhash=getFirstAidBlockHash()
    if blockhash != NOTFOUND:
        block=getBlockFromHash(blockhash)
        while block.isNextHash():
            block=getBlockFromHash(block.getNextHash())
        return block
    return NOTFOUND


class AidBlock(implement.AidBlock):
    
    def __init__(self):
        self.__guessers=[]
        pass
    def create(self):
        self.__height=str(self.getHeight())
        self.__version=1
        self.__timestamp=time.time()
        self.__random=random.randrange(0,2**64)
        self.__difficulty=getDifficulty()
        self.__answer=""
        block=getLastAidBlock()
        if block==NOTFOUND:
            self.__previoushash="First AidBlock"
        else:
            self.__previoushash=block.getBlockHash()
        self.__blockhash=""
        self.__nexthash=""
    def toString(self):
        pb2=aidblock_pb2.Aidblock()
        pb2.height=self.__height
        pb2.version=self.__version
        pb2.timestamp=self.__timestamp
        pb2.guessers.extend(self.__guessers)
        pb2.random=self.__random
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
        self.__random=pb2.random
        self.__difficulty=pb2.difficulty
        self.__answer=pb2.answer
        self.__previoushash=pb2.previoushash
        self.__blockhash=pb2.blockhash
        self.__nexthash=pb2.nexthash

    def checkHash(self):
        temp1=self.__blockhash
        pb2=aidblock_pb2.Aidblock()
        pb2.height=self.__height
        pb2.version=self.__version
        pb2.timestamp=self.__timestamp
        pb2.guessers.extend(self.__guessers)
        pb2.random=self.__random
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
        pb2.random=self.__random
        pb2.difficulty=self.__difficulty
        pb2.answer=self.__answer
        pb2.previoushash=self.__previoushash
        pb2.blockhash=""
        pb2.nexthash=""
        return method.hash(pb2.SerializeToString())
    def computeSha512(self):
        pb2=aidblock_pb2.Aidblock()
        pb2.height=self.__height
        pb2.version=self.__version
        pb2.timestamp=self.__timestamp
        pb2.guessers.extend(self.__guessers)
        pb2.random=self.__random
        pb2.difficulty=self.__difficulty
        pb2.answer=self.__answer
        pb2.previoushash=self.__previoushash
        pb2.blockhash=""
        pb2.nexthash=""
        return method.sha512(pb2.SerializeToString())

    def bale(self):
        self.setGuess()
        
    
    def getPreviousHash(self):
        if self.__previoushash!=NOTFOUND:
            return self.__previoushash
        return NOTFOUND
    
    def isBlockHash(self):
        if self.__blockhash != "":
            return True
        return False

    def setNextHash(self,nexthash):
        if self.isNextHash():
            raise Exception
        self.__nexthash=nexthash

    def isNextHash(self):
        if self.__nexthash != "":
            return True
        return False

    def getNextHash(self):
        return self.__nexthash
    
    def getBlockHash(self):
        return self.__blockhash

    def setBlockHash(self,blockhash):
        self.__blockhash=blockhash
    
    def getHeight(self):
        return getHeight()

    def theBlockHeight(self):
        return self.__height

    def getGuess(self):
        return self.__guessers
    
    def setGuess(self):
        self.__guessers.extend( guess.Guess.getGuessPool() )
    
    def setAnswer(self,answer):
        self.__answer=answer

    def getAnswer(self):
        return self.__answer
    
    def getDifficulty(self):
        return getDifficulty()

    def theBlockDifficulty(self):
        return self.__difficulty
        
    def getTimestamp(self):
        return self.__timestamp
    
    def send(self):
        data=self.toString()
        message.Message.send(MESSAGE_RESPONSE_AIDBLOCK,data)
        
    
    def firstBlock(self):
        self.__height=str(0)
        self.__version=1
        self.__timestamp=0.0
        self.__guessers=[]
        self.__random=0
        self.__difficulty=getDifficulty()
        self.__answer=""
        block=getLastAidBlock()
        if block==NOTFOUND:
            self.__previoushash="First AidBlock"
        else:
            self.__previoushash=block.getBlockHash()
        self.__blockhash=""
        self.__nexthash=""