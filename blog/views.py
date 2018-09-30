from django.shortcuts import render
from coding.models import read
from django import forms
# Create your views here.

def index(request):
    return render(request, 'index.html')

def article1(request):
    read1=read.objects.get(id=1)
    read1.increase()
    context = {
                'read_count': read1,
               }
    return render(request, 'article/1.html',context=context)
