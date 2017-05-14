
from blockchain.enum import *

class Chains :
    chainslist=dict()
    @staticmethod
    def setChain(chainid,chain):
        Chains.chainslist[chainid]=chain

    @staticmethod
    def getChain(chainid):
        return Chains.chainslist[chainid]

class Chain:
    def __init__(self):
        self.blocklist=dict()
        self.firstblock=NOTFOUND

    def addBlock(self,block):
        len(self.blocklist)==0 if self.setFirst(block) else False
        self.blocklist[block.blockHash]=block
        return self

    def getBlock(self,blockhash):
        return self.blocklist[blockhash]

    def getHeight(self):
        return len(self.blocklist)

    def setFirst(self,block):
        self.firstblock=block
        return self

    def getFirst(self):
        return self.firstblock
    
    def getLast(self):
        block=self.getFirst()
        if block != NOTFOUND:
            while block.isNext():
                block=self.getBlock(block.next())
            return block
        return NOTFOUND