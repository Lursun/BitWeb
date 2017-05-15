#coding:utf-8
u"""

"""
from blockchain.protobuf import block_pb2
from blockchain.chain import chain
import hashlib

class Block :
    def __init__(self):
        self.txs=dict()
        self.txhashs=[]
        
    def create(self,chainid):
        selfChain=chain.Chains.getChain(chainid)
        height=selfChain.getHeight()
        self.height=height+1
        self.version=1
        self.chainid=chainid
        self.txhashs=[]
        lastBlock=selfChain.getLast()
        
        if lastBlock!=False:
            self.previousHash=lastBlock.blockHash
        else:
            self.previousHash="GENESIS BLOCK"
        
        self.blockHash=""
        self.nextHash=""
        self.packageHash=""
        return self
    def putTxs(self, txs):
        for tx in txs:
            self.txhashs.append(tx)
        self.txs=txs
        return self
    def SerializeOfbale(self):
        pb2=block_pb2.Block()
        pb2.height=hex(self.height)
        pb2.version=self.version
        pb2.chainid=self.chainid
        pb2.txhashs.extend(self.txs)
        pb2.previoushash=self.previousHash
        pb2.blockhash=""
        pb2.nexthash=""
        pb2.packagehash=""
        temp=pb2.SerializeToString()
        pb2.blockhash=hashlib.sha256(temp).hexdigest()
        self.blockHash=pb2.blockhash
        return pb2.SerializeToString()
    def isNext(self):
        """
        nexthash isset
        """
        if self.nextHash != "":
            return True
        else:
            return False
    def next(self):
        """
        get nexthash
        """
        return self.nextHash
    def setNextHash(self,nexthash):
        self.nextHash=nexthash

    def getHeight(self):
        return self.height

    def getPreviousHash(self):
        return self.previousHash

    def getBlockHash(self):
        return self.blockHash

    def getChainID(self):
        return self.chainid

    def getNextHash(self):
        return self.nextHash
    
    def getTxHashs(self):
        return self.txhashs