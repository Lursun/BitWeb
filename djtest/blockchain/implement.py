from abc import ABCMeta ,abstractmethod
class Protobuf:
    __metaclass__ = ABCMeta
    @abstractmethod
    def create(self):
        return

    @abstractmethod
    def toString(self):
        return
    
    @abstractmethod
    def stringToObject(self):
        return
    
    @abstractmethod
    def isHash(self):
        return
    
    @abstractmethod
    def computeHash(self):
        return

    @abstractmethod
    def checkHash(self):
        return

class Block(Protobuf):
    @abstractmethod
    def getBlock(self):
        """Retrieve data from the input source and return an object."""
        return
    
    @abstractmethod
    def isNext(self):
        return
    
    @abstractmethod
    def next(self):
        return

    @abstractmethod
    def setNextHash(self,nexthash): 
        return

    @abstractmethod
    def getHeight(self):
        return 

    @abstractmethod
    def getPreviousHash(self):
        return 

    @abstractmethod
    def getBlockHash(self):
        return 

    @abstractmethod
    def getChainID(self):
        return 

    @abstractmethod
    def getNextHash(self):
        return 

    @abstractmethod
    def getTxHashs(self):
        return 



class Tx(Protobuf):
    @abstractmethod
    def sign(self):
        return

    @abstractmethod
    def checkSign(self):
        return

    @abstractmethod
    def setHash(self):
        return

class Message(Protobuf):
    @abstractmethod
    def send(self):
        return

    @abstractmethod
    def recv(self):
        return

    @abstractmethod
    def getType(self):
        return

    @abstractmethod
    def processing_message(self):
        return

class AidBlock(Protobuf):
    pass
    
class Guess(Protobuf):
    pass





class Chain:
    __metaclass__ = ABCMeta
    @abstractmethod
    def create(self):
        return

class Member:
    __metaclass__ = ABCMeta
    @abstractmethod
    def signUp(self):
        return
    @abstractmethod
    def decrypto():
        return
    @abstractmethod
    def encrypto():
        return
    