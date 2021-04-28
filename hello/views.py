from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
    return HttpResponse("Hi This is my first web app!")
