
from blockchain.enum import *
from blockchain import implement
class Chains :
    chainslist=dict()
    @staticmethod
    def addChain(chainid):
        chain=Chain()
        chain.create(chainid)
        Chains.chainslist[chainid]=chain

    @staticmethod
    def getChain(chainid):
        return Chains.chainslist[chainid]

class Chain(implement.Chain):
    def __init__(self):
        self.__blocklist=dict()
        self.__firstblock=NOTFOUND
    def create(self,chainid):
        self.__chainid=chainid

    def appendBlock(self,block):
        if len(self.__blocklist)==0:
            self.setFirst(block)
        self.__blocklist[block.getBlockHash()]=block
        return self

    def getBlock(self,blockhash):
        return self.__blocklist[blockhash]

    def getHeight(self):
        return len(self.__blocklist)

    def setFirst(self,block):
        self.__firstblock=block
        return self

    def getFirst(self):
        return self.__firstblock
    
    def getLast(self):
        block=self.getFirst()
        if block != NOTFOUND:
            while block.isNext():
                block=self.getBlock(block.next())
            return block
        return NOTFOUND
    def getChainId(self):
        return self.__chainid