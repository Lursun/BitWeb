#coding:utf-8
from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
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