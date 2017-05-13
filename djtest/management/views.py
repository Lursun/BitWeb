#coding:utf-8
import os
from django.shortcuts import render
from django.http import HttpResponse
from blockchain.p2p import p2p
from blockchain.transaction import transaction
from blockchain.message import message as  message_module
from blockchain.enum import *
##reload ROOT_URLCONF
import sys
from django.conf import settings

from blockchain.circle import circle
from blockchain.block import block
from blockchain.transaction import transaction

#print open(os.path.dirname(__file__)+"/../circlelist").read()


def reload_urls(request, urlconf=None):
    if urlconf is None:
        urlconf = settings.ROOT_URLCONF
    if urlconf in sys.modules:
        reload(sys.modules[urlconf])
    return HttpResponse('urlconf reloaded')

def Tx(request):
    tx=transaction.Tx()
    tx.create(TX_TYPE_TEST,"management_circel",request.body)
    message_module.Message.send(MESSAGE_RESPONSE_TX,tx.tx_serialize)
    return HttpResponse(request.body)
def QueryPackage(request):
    return HttpResponse("")

def QueryCircles(request):
    circleid=request.GET.get("circleid","management_circle")
    return HttpResponse(circle.Circles.circleslist)

def QueryBlocks(request):
    circleid=request.GET.get("circleid","management_circle")
    return HttpResponse(circle.Circles.getCircle(circleid).blocklist)

def QueryBlock(request):
    circleid=request.GET.get("circleid","management_circle")
    blockhash=request.GET.get("blockhash","")
    return HttpResponse(circle.Circles.getCircle(circleid).getBlock(blockhash))

def QueryTxs(request):
    return HttpResponse(transaction.Tx.getTxPool())

def QueryTx(request):
    txhash=request.GET.get("txhash","")
    return HttpResponse(transaction.Tx.getTx(txhash))

def Query(request):
    return HttpResponse("")

def QueryNode(request):
    return HttpResponse(p2p.P2PScoket.getNode())

def JoinNode(request):
    p2p.P2PJoinStart((request.GET.get('ip','127.0.0.1'),int(request.GET.get('port','8001'))))
    return HttpResponse("addNode")

def index(request):
    return HttpResponse(p2p.P2PScoket.getClient())
    
def add(request):
    a=request.GET.get('a', 0) 
    b=request.GET.get('b', 0) 
    c = int(a)+int(b)
    return HttpResponse(str(c))

def add2(request, a, b):
    c = int(a) + int(b)
    return HttpResponse(str(c))

def test(request):
    string="OK"
    return render(request, 'home.html',{"string":string})