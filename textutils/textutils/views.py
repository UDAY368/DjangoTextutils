# This file is created by Uday
# This module always return the responses
from django.http import HttpResponse


def index(request):       # It must take the at least one argument
    return HttpResponse("Hello World")


def about(request):
    return HttpResponse("This page is about Django Usage")