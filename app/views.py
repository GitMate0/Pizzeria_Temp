from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def startpage(request):
    page = loader.get_template('index.html')
    return HttpResponse(page.render())
