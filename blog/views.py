# from django.shortcuts import render
from django.http import HttpResponse


def saySomething(request):
    return HttpResponse('<h1 style="color:green">What is wrong with the leaders of today?</h1>')
