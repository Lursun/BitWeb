from blockchain.enum import *
from blockchain import method
from blockchain.aidchain.aidblock import aidblock
from blockchain.aidchain.guess import guess
import time
import random

REMINING=False

def setRemining(boolean):
    global REMINING
    REMINING=boolean
def mine():
    global REMINING
    while True:
        Block=aidblock.AidBlock()
        Block.create()
        Block.bale()
        start=time.time()
        diff=Block.theBlockDifficulty()
        while not REMINING:
            Block.setAnswer(str(random.random()))
            _blockhash=Block.computeSha512()
            if int(_blockhash,16) < int(diff,16):
                break
        if REMINING:
            REMINING=False
            continue
        end=time.time()
        _blockhash=Block.computeHash()
        Block.setBlockHash(_blockhash)
        if Block.checkHash():
            guess.Guess.clearTxPool()
            previousBlock=aidblock.getBlockFromHash(Block.getPreviousHash())
            previousBlock.setNextHash(_blockhash)
            aidblock.addAidChain(Block)
            Block.send()
        print "Mining AidBlock : %s\n" % str(aidblock.getHeight())