# /testproject/myapp/views.py
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request, id):
    return HttpResponse('Hello World Id=' + str(id))
    
'''
def article(request, year):
    return HttpResponse('Article year='+ str(year))
'''

def article(request, year, slug):
    return HttpResponse('Article year='+ str(year) +' Slug='+slug)
