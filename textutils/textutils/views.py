# This file is created by Uday
# This module always return the responses
"""
-> We can pass 3 arguments into render method 1) request 2) .html file name 3) params as dict

"""
from django.http import HttpResponse
from django.shortcuts import render


def index(request):       # It must take the at least one argument
    params = {"name": "uday", "role": "Python Dev"}
    return render(request, 'index.html', params)
    # return HttpResponse("Home")


def removepunc(request):
    return HttpResponse("remove the punctuations")


def capfirst(request):
    return HttpResponse("capitalize the first letter")


def newlineremove(request):
    return HttpResponse("newline-remove")


def spaceremover(request):
    return HttpResponse("space remover")


def charcount(request):
    return HttpResponse("char-count")