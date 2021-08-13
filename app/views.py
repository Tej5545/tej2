from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def hai(request):
    return HttpResponse('hello')
def hey(request):
    return HttpResponse('soumya')

