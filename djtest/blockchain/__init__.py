#coding:utf-8
from blockchain.enum import *
import hashlib
import time
import random
from blockchain.protobuf import block_pb2
from blockchain.protobuf import package_pb2
from blockchain.protobuf import tx_pb2
from blockchain.circle import circle
from blockchain.block import block
from blockchain.transaction import transaction


firstTx=tx_pb2.Tx()
firstTx.circle="management_circel"
firstTx.version=1
firstTx.type=TX_TYPE_CREATE_CIRCLE
firstTx.timestamp=0.0
firstTx.value="Bitweb:台灣 盧瑞山教授區塊鏈實驗室 之 研究員：唐林竩，所開發"
firstTx.previoushash="GENESIS TX"
firstTx.txhash=""
temp=firstTx.SerializeToString()
firstTx.txhash=hashlib.sha256(temp).hexdigest()
tx_serialize=firstTx.SerializeToString()

transaction.Tx().addTx(tx_serialize)

firstBlock=block_pb2.Block()
firstBlock.height='0'
firstBlock.version=1
firstBlock.circle="management_circel"
firstBlock.txhashs.append(firstTx.txhash)
firstBlock.previoushash="GENESIS BLOCK"
firstBlock.blockhash=""
firstBlock.nexthash=""
firstBlock.packagehash=""
temp=firstBlock.SerializeToString()
firstBlock.blockhash=hashlib.sha256(temp).hexdigest()
block_serialize=firstBlock.SerializeToString()

blocks=block.Blocks()
blocks.addBlock(block_serialize)
circle.Circles("management_circle",blocks)


firstPackage=package_pb2.Package()
firstPackage.version=1
firstPackage.timestamp=0
firstPackage.difficulty='ffff4269747765620ae9968be799bcefbc9ae59490e69e97e7aba9284c696e2d59692054616e672920206c757273756e39313430313340676d61696c2e636f6d'
firstPackage.blockhashs.append(firstBlock.blockhash)

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
print "GENESIS BLOCK:",firstBlock.blockhash
print "GENESIS Tx:",firstTx.txhash