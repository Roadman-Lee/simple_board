from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.


def board(request):
    return HttpResponse("hello world")



