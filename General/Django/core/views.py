from django.shortcuts import render
from django.http import HttpResponse


def home(request):
    return HttpResponse("Creando mi primer hola mundo en Django")