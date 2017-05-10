rm djtest/blockchain/protobuf/*.py
protoc --python_out=./ djtest/blockchain/protobuf/*.proto
