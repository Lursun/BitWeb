from blockchain.enum import *
from blockchain import method
import time
import random

REMINING=False
def mining():
    i=5
    while i>0:
        i-=1
        newPackage=package.Package()
        newPackage.bale()
        start=time.time()
        while not REMINING:
            newPackage.setAnswer(str(random.random()))
            time1m=newPackage.ToSerialize()
            out=method.hash(time1m)
            if int(out,16) < int(newPackage.difficulty,16):
                break
        end=time.time()
        print out
        print newPackage.answer
        newPackage.setPackageHash(out)
        newPackage.ToSerialize()
        package.Package.packages.append(newPackage)
        print("end",end-start)
    