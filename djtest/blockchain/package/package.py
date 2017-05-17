#coding:utf-8
from blockchain.enum import *
import time
import random
from blockchain.protobuf import block_pb2
from blockchain.protobuf import package_pb2
from blockchain.protobuf import tx_pb2
from blockchain.transaction import transaction
from blockchain.block import block
from blockchain.chain import chain

class Package :
    packages=[]
    def __init__(self):
        self.answer=""
        self.nexthash=""
        self.version=1
        self.timestamp=time.time()
        self.difficulty=self.getDifficulty()
        self.blockhashs=[]
        self.packageHash=""
        self.nextHash=""
    def ToSerialize(self):
        pb2=package_pb2.Package()
        pb2.version=self.version
        pb2.timestamp=self.timestamp
        pb2.difficulty=self.difficulty
        pb2.packagehash=self.packageHash
        pb2.answer=self.answer
        pb2.nexthash=""
        return pb2.SerializeToString()
    def setPackageHash(self,packageHash):

        self.packageHash=packageHash
    def setAnswer(self,answer):

        self.answer=answer
    def getDifficulty(self):
        if len(Package.packages)<100:
            return 'ffff4269747765620ae9968be799bcefbc9ae59490e69e97e7aba9284c696e2d59692054616e672920206c757273756e39313430313340676d61696c2e636f6d'
        else:
            """
            需更改
            """
            return '4269747765620ae9968be799bcefbc9ae59490e69e97e7aba9284c696e2d59692054616e672920206c757273756e39313430313340676d61696c2e636f6d'
    def bale(self):
        newBlock=block.Block()
        newBlock.create("management_chain")
        newBlock.putTxs(transaction.Tx.getTxPool())
        transaction.Tx.clearTxPool()
        newBlock.SerializeOfbale()
        nowChain=chain.Chains.getChain("management_chain")
        if newBlock.getHeight()>1:
            nowChain.getLast().setNextHash( newBlock.getBlockHash() )
        nowChain.addBlock(newBlock)
        self.blockhashs.append(newBlock.blockHash)

