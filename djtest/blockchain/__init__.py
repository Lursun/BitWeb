#coding:utf-8
from blockchain.enum import *
import time
import random
from blockchain.protobuf import block_pb2
from blockchain.protobuf import package_pb2
from blockchain.protobuf import tx_pb2
from blockchain.chain import chain
from blockchain.block import block
from blockchain.transaction import transaction
from blockchain.package import mining
from blockchain.package import package
from blockchain.member import member
from blockchain.aidchain.guess import guess
from blockchain.aidchain.aidblock import aidblock
from blockchain.aidchain.mining import mining
lursun=member.Member()
lursun.signUp("Lursun","最強的工程師：唐林竩")

firstTx=transaction.Tx()
firstTx.create(TX_TYPE_CREATE_CHAIN,"management_chain","Bitweb:台灣 盧瑞山教授區塊鏈實驗室 之 研究員：唐林竩，所開發")

chain.Chains.addChain("management_chain")
guess.Guess()

Block=aidblock.AidBlock()
Block.create()
Block.firstBlock()
start=time.time()
diff=Block.theBlockDifficulty()
while not True:
    Block.setAnswer(str(random.random()))
    _blockhash=Block.computeSha512()
    if int(_blockhash,16) < int(diff,16):
        break
end=time.time()
_blockhash=Block.computeHash()
Block.setBlockHash(_blockhash)
aidblock.setFirstAidBlockHash(Block.getBlockHash())
aidblock.addAidChain(Block)
print "First Hash:"+_blockhash
# print "GENESIS PACKAGE"
# #start=time.time()
# print "WAIT GENESIS PACKAGE"
# mining.mining()
# #end=time.time()


# management_chain=chain.Chains.getChain("management_chain")
# print "GENESIS PACKAGE:", package.Package.packages[0].packageHash
# print "GENESIS BLOCK:",management_chain.getLast().blockHash
# print "GENESIS Tx:",firstTx.txHash