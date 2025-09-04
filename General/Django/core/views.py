from django.shortcuts import render



def home(request):
    return render(request,'index.html')

def receta(request):
    return render(request,'receta.html')

def contacto(request):
    return render(request,'contacto.html')