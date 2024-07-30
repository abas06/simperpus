from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.
def beranda(request):
    return render (request, 'index.html')