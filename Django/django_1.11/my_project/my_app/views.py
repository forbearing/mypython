from django.shortcuts import render

# Create your views here.
from django.http import HttpReponse

def index(request):
    return HttpReponse('Hello Django')
