#coding:utf-8
from blockchain.enum import *
import hashlib
import time
import random
from blockchain.protobuf import block_pb2
from blockchain.protobuf import package_pb2
from blockchain.protobuf import tx_pb2
from blockchain.chain import chain
from blockchain.block import block
from blockchain.transaction import transaction

firstTx=transaction.Tx()
firstTx.create(TX_TYPE_CREATE_CHAIN,"management_chain","Bitweb:台灣 盧瑞山教授區塊鏈實驗室 之 研究員：唐林竩，所開發")

chain.Chains.setChain("management_chain",chain.Chain())

 
firstBlock=block.Block()
firstBlock.create("management_chain")
firstBlock.putTxs(transaction.Tx.getTxPool())


block_serialize=firstBlock.ToSerialize()




firstPackage=package_pb2.Package()
firstPackage.version=1
firstPackage.timestamp=0
firstPackage.difficulty='ffff4269747765620ae9968be799bcefbc9ae59490e69e97e7aba9284c696e2d59692054616e672920206c757273756e39313430313340676d61696c2e636f6d'
firstPackage.blockhashs.append(firstBlock.blockHash)

firstPackage.packagehash="GENESIS PACKAGE"
#start=time.time()
print "WAIT GENESIS PACKAGE"
while True:
    firstPackage.answer=str(random.random())
    time1m=firstPackage.SerializeToString()
    out=hashlib.sha512(time1m).hexdigest()
    if int(out,16) < int(firstPackage.difficulty,16):
        break
#end=time.time()
firstPackage.packagehash=out
firstBlock.packagehash=firstPackage.packagehash


print "GENESIS PACKAGE:",firstBlock.packagehash
print "GENESIS BLOCK:",firstBlock.blockHash
print "GENESIS Tx:",firstTx.txHash