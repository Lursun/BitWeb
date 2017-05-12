rm djtest/blockchain/protobuf/*_pb2.py
protoc --python_out=./ djtest/blockchain/protobuf/*.proto
