from django.shortcuts import render, redirect
from bookapp.forms import AfegirLlibreForm
from bookapp.models import Llibre, TematiquesLlibre, Comentari, Notificacio
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
    comptador = Counter()
    if not usuari.is_Treballador:
        return render(request, "home.html")
    if usuari.is_Editor:
        llibres = Llibre.objects.filter(editor=usuari)
    if usuari.is_Escriptor:
        llibres = Llibre.objects.filter(escriptor=usuari)
    tematiques = list()
    for llibre in llibres:
        tematiques.append(TematiquesLlibre.objects.filter(llibre=llibre))
    mylist = zip(llibres, tematiques)
    llibreshtml = {
        "object_list": llibres,
        "counter": comptador,
        "mylist": mylist
    }
    if usuari.is_Escriptor:
        return render(request, "escriptori_escriptor.html", llibreshtml)
    if usuari.is_Editor:
        return render(request, "escriptori_editor.html", llibreshtml)


def afegirLlibre(request):
    if request.method == 'POST':
        form = AfegirLlibreForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            seleccionar_editor(obj)
            obj.escriptor = request.user
            obj.save()
            return redirect('afegirllibre')
    else:
        form = AfegirLlibreForm()
    return render(request, "afegirllibre.html", {'form': form})


def seleccionar_editor(llibre):
    editors_lliures = CustomUser.objects.filter(is_Editor=True, lliure=True)
    editoraux = editors_lliures[0]
    llibre.editor = editoraux
    editor = CustomUser.objects.get(email=editoraux)
    editor.lliure = False
    editor.save()
    print(editor.lliure)
    notificacio = Notificacio()
    notificacio.missatge = "Tens un nou llibre assignat"
    notificacio.usuari = editoraux
    notificacio.save()


def areaedicio(request, pk):
    llibre = Llibre.objects.get(pk=pk)
    context = {
        "llibre": llibre
    }
    return render(request, 'area_edicio.html', context)


def areaescriptor(request, pk):
    llibre = Llibre.objects.get(pk=pk)
    context = {
        "llibre": llibre
    }
    return render(request, 'area_escriptor.html', context)


def enviarnovaversio(request):
    return render(request, 'enviar_nova_versio.html')


def commentseditor(request, pk):
    llibre = Llibre.objects.filter(pk=pk)
    usuari = CustomUser.objects.filter(email=request.user)
    comentaris = Comentari.objects.filter(usuari__in=usuari, llibre__in=llibre)
    context = {
        "llibre": llibre,
        "usuari": usuari,
        "comentaris": comentaris
    }
    if request.method == "POST":
        titol = request.POST.get('titol')

        descripcio = request.POST.get('descripcio')

        nou_comentari = Comentari()
        nou_comentari.usuari = request.user
        nou_comentari.titol = titol
        nou_comentari.descripcio = descripcio
        nou_comentari.llibre = Llibre.objects.get(pk=pk)
        nou_comentari.save()
    return render(request, 'comments_editor.html', context)


def canviardocument(request):
    return render(request, 'canviar_document.html')

def notificacions(request):
    notificacions = Notificacio.objects.filter(usuari=request.user)
    context = {
        "object_list": notificacions
    }
    return render(request, "notificacions.html", context)

def comments(request, pk):
    llibre = Llibre.objects.filter(pk=pk)
    usuari = CustomUser.objects.filter(email=request.user)
    comentaris = Comentari.objects.filter(usuari__in=usuari, llibre__in=llibre)
    context = {
        "llibre": llibre,
        "usuari": usuari,
        "comentaris": comentaris
    }
    return render(request, 'comments.html', context)

