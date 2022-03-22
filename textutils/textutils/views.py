# This file is created by Uday
# This module always return the responses
from django.http import HttpResponse


def index(request):       # It must take the at least one argument
    return HttpResponse("Home")


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