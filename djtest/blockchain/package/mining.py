from blockchain.enum import *
from blockchain.package import package
from blockchain.chain import chain
from blockchain.block import blocks
from blockchain.transaction import transaction
from blockchain.protobuf import block_pb2
from blockchain.protobuf import package_pb2
from blockchain.protobuf import tx_pb2
import time
import random
import hashlib
REMINING=False
def mining():
    
    while True:
        newPackage=package.Package()
        newPackage.bale()
        start=time.time()
        while not REMINING:
            newPackage.setAnswer(str(random.random()))
            time1m=newPackage.ToSerialize()
            out=hashlib.sha512(time1m).hexdigest()
            if int(out,16) < int(newPackage.difficulty,16):
                break
        end=time.time()
        print out
        print newPackage.answer
        newPackage.setPackageHash(out)
        newPackage.ToSerialize()
        package.Package.packages.append(newPackage)
        print("end",end-start)
    