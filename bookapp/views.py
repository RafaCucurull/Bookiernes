from django.shortcuts import render, redirect
from bookapp.forms import AfegirLlibreForm
from bookapp.models import Llibre
from users.models import CustomUser


def homePage(request):
    return render(request, "home.html")


def Escriptori(request):
    usuari = CustomUser.objects.get(email=request.user)
    if not usuari.is_Treballador:
        return render(request, "home.html")
    else:
        if usuari.is_Escriptor:
            return render(request, "escriptori_escriptor.html")
        if usuari.is_Editor:
            return render(request, "escriptori_editor.html")


def afegirLlibre(request):
    if request.method == 'POST':
        form = AfegirLlibreForm(request.POST)
        if form.is_valid():
            obj = form.save()
            obj.escriptor = request.user
            obj.save()
            return redirect('afegirllibre')
    else:
        form = AfegirLlibreForm()
    return render(request, "afegirllibre.html", {'form': form})


def areaedicio(request):
    return render(request, 'area_edicio.html')


def infollibre(request):
    usuari = CustomUser.objects.get(email=request.user)
    llibres = Llibre.objects.filter(editor=usuari)
    llibreshtml = {
        "object_list": llibres
    }
    return render(request, 'escriptori_editor.html', llibreshtml)
