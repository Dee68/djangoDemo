# from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def saySomething(request):
    return HttpResponse('<h1 style="color:green">What is wrong with the leaders of today?</h1>')