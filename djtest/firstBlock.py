#coding:utf-8
from blockchain.enum import *
import hashlib
import time
import random
from blockchain.protobuf import block_pb2
from blockchain.protobuf import tx_pb2


firstTx=tx_pb2.Tx()
firstTx.circle="management_circel"
firstTx.version=1
firstTx.type=TX_TYPE_CREATE_CIRCLE
firstTx.timestamp=time.time()
firstTx.value="台灣 盧瑞山教授區塊鏈實驗室 之 研究員：唐林竩，所開發之Bitweb"
firstTx.previoushash="GENESIS TX"
temp=firstTx.SerializeToString()
firstTx.hash=hashlib.sha256(temp).hexdigest()

firstBlock=block_pb2.Block()
firstBlock.height='0'
firstBlock.version=1
firstBlock.circle="management_circel"
firstBlock.txhashs.append(firstTx.hash)
firstBlock.previoushash="GENESIS BLOCK"
firstBlock.blockhash=""
firstBlock.nexthash=""
firstBlock.packagehash=""
temp=firstBlock.SerializeToString()
firstBlock.blockhash=hashlib.sha256(temp).hexdigest()

firstPackage=block_pb2.Package()
firstPackage.version=1
firstPackage.timestamp=time.time()
firstPackage.difficulty='18300af8c0a601a29f2d093d54f716a1a5ef947367b6977ba07605ae227412e18ff1742e501ec3fdf89a3c8174707750f65c569f8be186e33b817cb3375'
firstPackage.blockhashs.append(firstBlock.blockhash)

firstPackage.packagehash=""
start=time.time()
while True:
    firstPackage.answer=str(random.random())
    time1m=firstPackage.SerializeToString()
    out=hashlib.sha256(time1m).hexdigest()
    if int(out,16) < int(firstPackage.difficulty,16):
        break
end=time.time()
print out
print firstPackage.answer
firstPackage.packagehash=out
print("end",end-start)
firstBlock.packagehash=firstPackage.packagehash