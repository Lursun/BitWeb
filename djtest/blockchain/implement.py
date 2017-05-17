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
    def isHash(self):
        return
    
    @abstractmethod
    def computeHash(self):
        return

    @abstractmethod
    def checkHash(self):
        return

class Chain:
    __metaclass__ = ABCMeta
    @abstractmethod
    def create(self):
        return

class Block(Protobuf):
    __metaclass__ = ABCMeta
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
    
class Tx(Protobuf):
    __metaclass__ = ABCMeta
    @abstractmethod
    def getTx(self, input):
        """Retrieve data from the input source and return an object."""
        return

class Message(Protobuf):
    __metaclass__ = ABCMeta
    @abstractmethod
    def getMessage(self, input):
        """Retrieve data from the input source and return an object."""
        return

class AidBlock(Protobuf):
    __metaclass__ = ABCMeta

