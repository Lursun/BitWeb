import os
MESSAGE_REQUEST_HEIGHT=1001
MESSAGE_REQUEST_BLOCK=1002
MESSAGE_REQUEST_TX=1003
MESSAGE_REQUEST_PEERS=1004

MESSAGE_RESPONSE_HEIGHT=2001
MESSAGE_RESPONSE_BLOCK=2002
MESSAGE_RESPONSE_TX=2003
MESSAGE_RESPONSE_PEERS=2004


TX_TYPE_TEST=0
TX_TYPE_SEND_FILE=1
TX_TYPE_CREATE_CHAIN=2
TX_TYPE_REG_MEMBER=3
TX_TYPE_GENERAL=4

NOTFOUND="NOTFUND"
FOUND="FOUND"

PROJECTDIR=os.path.dirname(__file__)+"/../../"