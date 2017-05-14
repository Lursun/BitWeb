from blockchain.enum import *
from blockchain.package import package
from blockchain.chain import chain
from blockchain.block import blocks
from blockchain.transaction import transaction
from blockchain.protobuf import block_pb2
from blockchain.protobuf import package_pb2
from blockchain.protobuf import tx_pb2
import time

REMINING=False
def mining():
    REMINING=False
    while True
        start=time.time()
        firstPackage.version=1
        firstPackage.timestamp=time.time()
        while not REMINING:
            Package.answer=str(random.random())
            time1m=firstPackage.SerializeToString()
            out=hashlib.sha512(time1m).hexdigest()
            if int(out,16) < int(firstPackage.difficulty,16):
                break
        end=time.time()
        print out
        print firstPackage.answer
        firstPackage.packagehash=out
        print("end",end-start)
        firstBlock.packagehash=firstPackage.packagehash
    