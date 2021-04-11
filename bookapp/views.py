# Create your views here.
from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')

def areaedicio(request):
    return render(request, 'area_edicio.html')

def escriptorieditor(request):
    return render(request, 'escriptori_editor.html')

def escriptoriescriptor(request):
    return render(request, 'escriptori_escriptor.html')

def infollibre(request):
    usuari=CustomUser.objects.get(email=request.user)
    llibres=Llibre.objects.filter(editor=usuari)
    llibreshtml={
        "object_list": llibres
    }
    return render(request, 'escriptori_editor.html', llibreshtml)


