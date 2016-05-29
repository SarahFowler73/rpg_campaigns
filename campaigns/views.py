from django.shortcuts import render
from django.http import HttpResponse

def blah(request):
    return HttpResponse('Home Page')
