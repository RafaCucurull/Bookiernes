from django.shortcuts import render, redirect
from bookapp.forms import AfegirLlibreForm
from bookapp.models import Llibre, TematiquesLlibre, Comentari, Notificacio, Tematica
from bookapp.forms import AfegirLlibreForm, SolicitarImatgesForm
from bookapp.models import Llibre, TematiquesLlibre, Comentari, Notificacio
from bookapp.forms import AfegirLlibreForm, SolicitarImatgesForm, SolicitarMaquetacioForm, PujarMaquetacio
from bookapp.models import Llibre, TematiquesLlibre, Comentari, Notificacio, solicitudMaquetacio, Imatge
from users.models import CustomUser
from django.core.files.storage import FileSystemStorage
from datetime import datetime

def homePage(request):
    return render(request, "home.html")


def Escriptori(request):
    usuari = CustomUser.objects.get(email=request.user)
    if not usuari.is_Treballador:
        return render(request, "home.html")
    if usuari.is_Editor:
        llibres = Llibre.objects.filter(editor=usuari)
    if usuari.is_Escriptor:
        llibres = Llibre.objects.filter(escriptor=usuari)
    if usuari.is_Dissenyador:
        llibres = Llibre.objects.filter(dissenyador=usuari)
    if usuari.is_Maquetacio:
        llibres = Llibre.objects.filter(maquetador=usuari)
    if usuari.is_IT:
        llibres = Llibre.objects.filter(IT=usuari)
    tematiques = list()
    for llibre in llibres:
        tematiques.append(TematiquesLlibre.objects.filter(llibre=llibre))
    mylist = zip(llibres, tematiques)
    llibreshtml = {
        "object_list": llibres,
        "mylist": mylist
    }
    if usuari.is_Escriptor:
        return render(request, "escriptori_escriptor.html", llibreshtml)
    if usuari.is_Editor:
        return render(request, "escriptori_editor.html", llibreshtml)
    if usuari.is_Dissenyador:
        return render(request, "area_disseny_i_maquetacio.html", llibreshtml)
    if usuari.is_Maquetacio:
        return render(request, "area_disseny_i_maquetacio.html", llibreshtml)
    if usuari.is_IT:
        return render(request, "escriptori_it.html", llibreshtml)

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
    data = datetime.now()
    notificacio.data = data
    notificacio.llibre = llibre
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

def areait(request, pk):
    llibre = Llibre.objects.get(pk=pk)
    context = {
        "llibre": llibre
    }
    return render(request, 'area_escriptor.html', context)


def enviarnovaversio(request, pk):
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
        notificarEscriptorComentari(Llibre.objects.get(pk=pk))
    return render(request, 'comments_editor.html', context)

def dirbateriaimatges(request, pk):
    llibre = Llibre.objects.filter(pk=pk)
    comentaris = Comentari.objects.filter(llibre__in=llibre)
    context = {
        "llibre": llibre,
        "comentaris": comentaris
    }
    return render(request, 'directori_imatges.html', context)

def galeriaimatges(request, pk):
    llibre = Llibre.objects.get(pk=pk)
    context = {
        "llibre": llibre
    }
    return render(request, 'galeria_imatges.html', context)

def galeriamaquetacions(request, pk):
    llibre = Llibre.objects.get(pk=pk)
    context = {
        "llibre": llibre
    }
    return render(request, 'galeria_maquetacions.html', context)

def dirmaquetacions(request, pk):
    llibre = Llibre.objects.filter(pk=pk)
    comentaris = Comentari.objects.filter(llibre__in=llibre)
    context = {
        "llibre": llibre,
        "comentaris": comentaris
    }
    return render(request, 'directori_maquetacions.html', context)


def notificarEscriptorComentari(llibre):
    notificacio = Notificacio()
    notificacio.missatge = "Tens un comentari pendent de revisar"
    notificacio.usuari = llibre.escriptor
    notificacio.llibre = llibre
    data = datetime.now()
    notificacio.data = data
    notificacio.save()


def canviardocument(request, pk):
    llibre = Llibre.objects.get(pk=pk)

    context = {
        "llibrehtml": llibre
    }
    if request.method == "POST" and request.FILES['pdf']:
        pdf = request.FILES['pdf']
        print(pdf)
        fs = FileSystemStorage()
        filename = fs.save(pdf.name, pdf)

        llibre.pdf = fs.url(filename)
        print(llibre.pdf)
        llibre.save()

    return render(request, 'canviar_document.html', context)


def notificacions(request):
    notificacions = Notificacio.objects.filter(usuari=request.user)
    context = {
        "object_list": notificacions
    }
    return render(request, "notificacions.html", context)


def comments(request, pk):
    llibre = Llibre.objects.filter(pk=pk)
    comentaris = Comentari.objects.filter(llibre__in=llibre)
    context = {
        "llibre": llibre,
        "comentaris": comentaris
    }
    return render(request, 'comments.html', context)


def cataleg(request):
    qs = filtrar(request)
    print(qs)
    for llibre in qs:
        print(llibre.nom_llibre)
    context = {
        'queryset': qs,
        'tematiques': Tematica.objects.all()
    }
    return render(request, "cataleg.html", context)

def filtrar(request):
    queryset=Llibre.objects.all()
    tematiques=Tematica.objects.all()
    escriptor=CustomUser.objects.filter(is_Escriptor=True)
    titol = request.GET.get('titol')
    autor = request.GET.get('autor')
    colleccio = request.GET.get('collecio')
    min_pagines = request.GET.get('pagines_min')
    max_pagines = request.GET.get('pagines_max')
    tematica = request.GET.get('tematica')


    if is_valid(titol):
        queryset=queryset.filter(nom_llibre__icontains=titol)
    if is_valid(autor):
        queryset=queryset.filter(escriptor__nom__icontains=autor)
    if is_valid(colleccio):
        queryset=queryset.filter(coleccio__icontains=colleccio)
    if is_valid(min_pagines):
        queryset=queryset.filter(num_pagines__gte=min_pagines)
    if is_valid(max_pagines):
        queryset=queryset.filter(num_pagines__lt=max_pagines)
    if is_valid(tematica) and tematica != 'Tria...':
        queryset=queryset.filter(tematiques__nom_tematica=tematica)

    return queryset

def is_valid(param):
    return param != '' and param is not None

def publicarllibre(request, pk):
    llibre = Llibre.objects.get(pk=pk)
    llibreshtml = {
        "llibre": llibre,
    }
    if request.method == "POST":
        llibre.publicat = True
        llibre.save()
    
    return render(request, "publicarllibre.html", llibreshtml)

def galeriaImatges(request, pk):
    llibre = Llibre.objects.get(pk=pk)
    imatges = llibre.imatges
    context = {
        'llistaimatges': imatges,
    }
    return render()


def solicitudImatges(request, pk):
    llibre = Llibre.objects.get(pk=pk)
    if request.method == 'POST':
        form = SolicitarImatgesForm(request.POST)
        if form.is_valid():
            obj = form.save()
            obj.llibre = llibre
            obj.editor = request.user
            seleccionar_dissenyador(obj, llibre)
            obj.save()
            return redirect(request.path_info)
    else:
        form = SolicitarImatgesForm()
    context = {
        'form': form
    }
    return render(request, "publicarllibre.html", context)


def seleccionar_dissenyador(solicitud, llibre):
    dissenyadors_lliures = CustomUser.objects.filter(is_Dissenyador=True, lliure=True)
    dissenyadoraux = dissenyadors_lliures[0]
    llibre.dissenyador = dissenyadoraux
    solicitud.dissenyador = dissenyadoraux
    dissenyador = CustomUser.objects.get(email=dissenyadoraux)
    dissenyador.lliure = False
    dissenyador.save()
    notificacio = Notificacio()
    notificacio.missatge = "Tens un nova sol·licitud d'imatges assignada"
    notificacio.usuari = dissenyadoraux
    notificacio.save()


def galeriaMaquetacions(request, pk):
    return render(request, "maquetacio.html")


def solicitudmaquetacio(request, pk):
    llibre = Llibre.objects.get(pk=pk)
    if request.method == 'POST':
        form = SolicitarImatgesForm(request.POST)
        if form.is_valid():
            obj = form.save()
            obj.llibre = llibre
            obj.editor = request.user
            seleccionar_maquetador(obj, llibre)
            obj.save()
            return redirect('solicitudimatges')
    else:
        form = SolicitarMaquetacioForm()
    return render(request, "solictudmaquetacio.html", {'form': form})


def seleccionar_maquetador(solicitud, llibre):
    maquetador_lliures = CustomUser.objects.filter(is_Maquetacio=True, lliure=True)
    maquetadoraux = maquetador_lliures[0]
    llibre.maquetador = maquetadoraux
    solicitud.maquetador = maquetadoraux
    maquetador = CustomUser.objects.get(email=maquetadoraux)
    maquetador.lliure = False
    maquetador.save()
    notificacio = Notificacio()
    notificacio.missatge = "Tens un nova sol·licitud de maquetació assignada"
    notificacio.usuari = maquetadoraux
    notificacio.save()


def areaDisssenyiMaquetacio(request, pk):
    llibre = Llibre.objects.get(pk=pk)


def solicitudsDisseny(request, pk):
    llibre = Llibre.objects.get(pk=pk)
    solicituds_disseny = solicitudImatges.objects.filter(llibre=llibre)
    solicituds = {
        'llista_solicituds': solicituds_disseny
    }
    return render()


def afegirBateriaImatges(request, pk):
    llibre = Llibre.objects.get(pk=pk)
    imatge = Imatge.objects.get()
    llibre.imatges.add(imatge)
    return render()


def solicitudsMaquetacio(request, pk):
    llibre = Llibre.objects.get(pk=pk)
    solicituds_maquetacio = solicitudMaquetacio.objects.filter(llibre=llibre)
    solicituds = {
        'llista_solicituds': solicituds_maquetacio
    }
    return render()


def afegirMaquetacio(request, pk):
    llibre = Llibre.objects.get(pk=pk)
    if request.method == 'POST':
        form = PujarMaquetacio(request.POST)
        if form.is_valid():
            obj = form.save()
            obj.save()
            llibre.maquetacio = obj
            return redirect('')
    else:
        form = PujarMaquetacio()
    return render()
