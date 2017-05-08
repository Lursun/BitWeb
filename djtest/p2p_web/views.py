#coding:utf-8
import os
from django.shortcuts import render
from django.http import HttpResponse
from blockchain.p2p import p2p
from blockchain.enum import *
import threading
port=node=""
try:
    node=os.environ["P2P_CONNECT"]
except:
    pass
try:
    port=os.environ["P2P_PORT"]
except:
    port=8001
print port

p2pServer=p2p.P2PScoketListen(port)
p2pServer.start()


def index(request):
    p2p.P2PScoket.printf()
    return HttpResponse(u"欢迎光临 自强学堂!")
    
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