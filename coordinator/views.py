from django.shortcuts import render
from django.http import HttpResponse


def meu_ovo(request):
    return render(request,'index.html')
