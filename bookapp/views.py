from django.shortcuts import render, redirect
from django.views.generic import DetailView

from bookapp.forms import AfegirLlibreForm
from bookapp.models import Llibre
from users.models import CustomUser


class Counter:
    counter = 0

    def increment(self):
        self.counter += 1
        return ''

    def mes3(self):
        if self.counter > 3:
            self.counter == 0
            return True

def homePage(request):
    return render(request, "home.html")


def Escriptori(request):
    usuari = CustomUser.objects.get(email=request.user)
    llibres = Llibre.objects.filter(editor=usuari)
    comptador = Counter()
    llibreshtml = {
        "object_list": llibres,
        "counter": comptador
    }
    if not usuari.is_Treballador:
        return render(request, "home.html")
    else:
        if usuari.is_Escriptor:
            return render(request, "escriptori_escriptor.html", llibreshtml)
        if usuari.is_Editor:
            return render(request, "escriptori_editor.html", llibreshtml)


def afegirLlibre(request):
    if request.method == 'POST':
        form = AfegirLlibreForm(request.POST)
        if form.is_valid():
            print("hola")
            obj = form.save()
            obj.escriptor = request.user
            obj.save()
            return redirect('afegirllibre')
    else:
        form = AfegirLlibreForm()
    return render(request, "afegirllibre.html", {'form': form})


def areaedicio(request, pk):
    llibre = Llibre.objects.get(pk=pk)
    context = {
        "llibrehtml": llibre
    }
    return render(request, 'area_edicio.html', context)


def areaescriptor(request, pk):
    llibre = Llibre.objects.get(pk=pk)
    context = {
        "llibrehtml": llibre
    }
    return render(request, 'area_escriptor.html', context)

def enviarnovaversio(request):
    return render(request, 'enviar_nova_versio.html')


def commentseditor(request):
    return render(request, 'comments_editor.html')


def canviardocument(request):
    return render(request, 'canviar_document.html')


def comments(request):
    return render(request, "comments.html")
