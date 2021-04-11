from django.shortcuts import render, redirect
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
            obj = form.save()
            obj.escriptor = request.user
            obj.save()
            return redirect('afegirllibre')
    else:
        form = AfegirLlibreForm()
    return render(request, "afegirllibre.html", {'form': form})


def areaedicio(request):
    return render(request, 'area_edicio.html')

def areaescriptor(request):
    return render(request, 'area_escriptor.html')

def escriptoriescriptor(request):
    return render(request, 'escriptori_escriptor.html')

def enviarnovaversio(request):
    return render(request, 'enviar_nova_versio.html')
