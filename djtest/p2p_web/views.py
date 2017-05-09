#coding:utf-8
import os
from django.shortcuts import render
from django.http import HttpResponse
from blockchain.p2p import p2p
from blockchain.enum import *
##reload ROOT_URLCONF
import sys
from django.conf import settings






p2p.P2PNetworkStart()

def reload_urls(request, urlconf=None):
    if urlconf is None:
        urlconf = settings.ROOT_URLCONF
    if urlconf in sys.modules:
        reload(sys.modules[urlconf])
    return HttpResponse('urlconf reloaded')

def Tx(request):
    return HttpResponse("")
def Query(request):
    return HttpResponse("")
def QueryNode(request):
    print (request.body)
    return HttpResponse(p2p.P2PScoket.getClient())
def index(request):
    print (request.body)
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