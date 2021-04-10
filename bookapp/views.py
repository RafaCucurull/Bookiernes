# Create your views here.
from django.shortcuts import render

def homepage(request):
    return render(request, 'home.html')

def areaedicio(request):
    return render(request, 'area_edicio.html')