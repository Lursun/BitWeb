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
lursun=member.Member()
lursun.signUp("Lursun","最強的工程師：唐林竩")

firstTx=transaction.Tx()
firstTx.create(TX_TYPE_CREATE_CHAIN,"management_chain","Bitweb:台灣 盧瑞山教授區塊鏈實驗室 之 研究員：唐林竩，所開發")

chain.Chains.addChain("management_chain")

guess.Guess()
aidblock.AidBlock()


# print "GENESIS PACKAGE"
# #start=time.time()
# print "WAIT GENESIS PACKAGE"
# mining.mining()
# #end=time.time()


# management_chain=chain.Chains.getChain("management_chain")
# print "GENESIS PACKAGE:", package.Package.packages[0].packageHash
# print "GENESIS BLOCK:",management_chain.getLast().blockHash
# print "GENESIS Tx:",firstTx.txHash