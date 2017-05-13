from blockchain.protobuf import block_pb2
class Blocks :
    def __init__(self):
        self.blocklist=dict()
    def addBlock(self,block):
        pb2=block_pb2.Block()
        pb2.ParseFromString(block)
        self.blocklist[pb2.blockhash]=block
    def getBlock(self,blockhash):
        block=self.blocklist[blockhash]
        pb2=block_pb2.Block()
        pb2.ParseFromString(block)
        return pb2

        