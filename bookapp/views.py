from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from bookapp import models
from bookapp.forms import AfegirLlibreForm, SolicitarImatgesForm, SolicitarMaquetacioForm, PujarMaquetacio, pujarImatge, \
    SolicitarPublicacioForm, SolicitarTraduccioForm
from bookapp.models import Llibre, TematiquesLlibre, Comentari, Notificacio, Tematica, Imatge
from users.models import CustomUser
from django.core.files.storage import FileSystemStorage
from datetime import datetime
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfFileMerger
import PyPDF2
from translate import Translator
from fpdf import FPDF
import os
from django.http import FileResponse, Http404


def homePage(request):
    return render(request, "home.html")


def Escriptori(request):
    global llibres
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
        llibres = Llibre.objects.filter(it=usuari)
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
        return render(request, "escriptori_maquetador_dissenyador.html", llibreshtml)
    if usuari.is_Maquetacio:
        return render(request, "escriptori_maquetador_dissenyador.html", llibreshtml)
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
    llibre = Llibre.objects.get(pk=pk)
    context = {
        "llibre": llibre,
    }
    return render(request, 'directori_imatges.html', context)


def dirmaquetacions(request, pk):
    llibre = Llibre.objects.get(pk=pk)
    context = {
        "llibre": llibre,
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
    queryset = Llibre.objects.all()
    tematiques = Tematica.objects.all()
    escriptor = CustomUser.objects.filter(is_Escriptor=True)
    titol = request.GET.get('titol')
    autor = request.GET.get('autor')
    colleccio = request.GET.get('collecio')
    min_pagines = request.GET.get('pagines_min')
    max_pagines = request.GET.get('pagines_max')
    tematica = request.GET.get('tematica')

    if is_valid(titol):
        queryset = queryset.filter(nom_llibre__icontains=titol)
    if is_valid(autor):
        queryset = queryset.filter(escriptor__nom__icontains=autor)
    if is_valid(colleccio):
        queryset = queryset.filter(coleccio__icontains=colleccio)
    if is_valid(min_pagines):
        queryset = queryset.filter(num_pagines__gte=min_pagines)
    if is_valid(max_pagines):
        queryset = queryset.filter(num_pagines__lt=max_pagines)
    if is_valid(tematica) and tematica != 'Tria...':
        queryset = queryset.filter(tematiques__nom_tematica=tematica)

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
        notificarEditorPublicat(llibre)
        notificarITPublicat(llibre)
        return redirect('/escriptori')

    return render(request, "publicarllibre.html", llibreshtml)


def notificarEditorPublicat(llibre):
    editor = llibre.editor
    notificacio = Notificacio()
    notificacio.missatge = "El llibre que has estat editant ja ha estat publicat a la Web"
    notificacio.usuari = editor
    data = datetime.now()
    notificacio.data = data
    notificacio.llibre = llibre
    notificacio.save()


def notificarITPublicat(llibre):
    it = llibre.it
    notificacio = Notificacio()
    notificacio.missatge = "El llibre que tenies assignat ja ha estat publicat a la Web"
    notificacio.usuari = it
    data = datetime.now()
    notificacio.data = data
    notificacio.llibre = llibre
    notificacio.save()


def galeriaImatges(request, pk):
    llibre = Llibre.objects.get(pk=pk)
    context = {
        'imatges': llibre.imatges.all(),
        'llibre': llibre,
    }
    return render(request, "galeria_imatges.html", context)


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
    return render(request, "solicitud_imatges.html", context)


def seleccionar_dissenyador(solicitud, llibre):
    dissenyadors_lliures = CustomUser.objects.filter(is_Dissenyador=True, lliure=True)
    dissenyadoraux = dissenyadors_lliures[0]
    llibre.dissenyador = dissenyadoraux
    llibre.save()
    solicitud.dissenyador = dissenyadoraux
    dissenyador = CustomUser.objects.get(email=dissenyadoraux)
    dissenyador.lliure = False
    dissenyador.save()
    notificacio = Notificacio()
    notificacio.missatge = "Tens un nova sol·licitud d'imatges assignada"
    notificacio.usuari = dissenyadoraux
    data = datetime.now()
    notificacio.data = data
    notificacio.llibre = llibre
    notificacio.save()


def galeriaMaquetacions(request, pk):
    llibre = Llibre.objects.get(pk=pk)
    maquetacions = llibre.maquetacio.maquetacio.all()
    print(maquetacions)
    context = {
        "llibre": llibre,
        "maquetacions": maquetacions
    }
    return render(request, "galeria_maquetacions.html", context)


def solicitudmaquetacio(request, pk):
    llibre = Llibre.objects.get(pk=pk)
    if request.method == 'POST':
        form = SolicitarMaquetacioForm(request.POST)
        if form.is_valid():
            obj = form.save()
            obj.llibre = llibre
            obj.editor = request.user
            seleccionar_maquetador(obj, llibre)
            obj.save()
            return redirect(request.path_info)
    else:
        form = SolicitarMaquetacioForm()
    return render(request, "enviar_llibre_maquetar.html", {'form': form})


def seleccionar_maquetador(solicitud, llibre):
    maquetador_lliures = CustomUser.objects.filter(is_Maquetacio=True, lliure=True)
    maquetadoraux = maquetador_lliures[0]
    llibre.maquetador = maquetadoraux
    llibre.save()
    solicitud.maquetador = maquetadoraux
    maquetador = CustomUser.objects.get(email=maquetadoraux)
    maquetador.lliure = False
    maquetador.save()
    notificacio = Notificacio()
    notificacio.missatge = "Tens un nova sol·licitud de maquetació assignada"
    notificacio.usuari = maquetadoraux
    data = datetime.now()
    notificacio.data = data
    notificacio.llibre = llibre
    notificacio.save()


def areaDisssenyiMaquetacio(request, pk):
    llibre = Llibre.objects.get(pk=pk)
    context = {
        "llibre": llibre
    }
    return render(request, 'area_disseny_i_maquetacio.html', context)


def veuresolicitudsImatge(request, pk):
    llibre = Llibre.objects.get(pk=pk)
    solicituds_disseny = models.solicitudImatges.objects.filter(llibre=llibre)
    context = {
        'llista_solicituds': solicituds_disseny,
        'llibre': llibre
    }
    return render(request, 'solicituds_imatges_disseny.html', context)


def enviarbat(request, pk):
    llibre = Llibre.objects.get(pk=pk)
    if request.method == 'POST':
        form = pujarImatge(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            obj.save()
            llibre.imatges.add(obj)
            llibre.save()
            notificarEditorImatges(llibre)
            return redirect(request.path_info)
    else:
        form = pujarImatge()
    return render(request, 'enviar_imatges.html', {'form': form, 'llibre': llibre})


def notificarEditorImatges(llibre):
    editor = llibre.editor
    notificacio = Notificacio()
    notificacio.missatge = "Tens disponible la bateria d'imatges que vas sol·licitar per l'obra"
    notificacio.usuari = editor
    data = datetime.now()
    notificacio.data = data
    notificacio.llibre = llibre
    notificacio.save()


def notificarEditorMaquetacio(llibre):
    editor = llibre.editor
    notificacio = Notificacio()
    notificacio.missatge = "Tens disponible el llibre maquetat que vas sol·licitar"
    notificacio.usuari = editor
    data = datetime.now()
    notificacio.data = data
    notificacio.llibre = llibre
    notificacio.save()


def veuresolicitudsMaquetacio(request, pk):
    llibre = Llibre.objects.get(pk=pk)
    solicituds_maquetacio = models.solicitudMaquetacio.objects.filter(llibre=llibre)
    context = {
        'llista_solicituds': solicituds_maquetacio,
        'llibre': llibre
    }
    return render(request, 'solicituds_maquetacio_disseny.html', context)


def enviarMaquetacio(request, pk):
    llibre = Llibre.objects.get(pk=pk)
    if request.method == 'POST':
        form = PujarMaquetacio(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            obj.save()
            llibre.maquetacio = obj
            llibre.save()
            notificarEditorMaquetacio(llibre)
            return redirect(request.path_info)
    else:
        form = PujarMaquetacio()
    return render(request, 'enviar_maquetat.html', {'form': form, 'llibre': llibre})


def eliminarimatge(request, pk, pkimatge):
    llibre = Llibre.objects.get(pk=pk)
    imatge = Imatge.objects.get(pk=pkimatge)
    llibre.imatges.remove(imatge)
    llibre.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def download_image(request, pk, pkimatge):
    image = Imatge.objects.get(pk=pkimatge)
    filename = image.image.file.name.split('/')[-1]
    response = HttpResponse(image.image.file, content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=%s' % filename

    return response


def solicitudpublicacio(request, pk):
    llibre = Llibre.objects.get(pk=pk)
    if request.method == 'POST':
        form = SolicitarPublicacioForm(request.POST)
        if form.is_valid():
            obj = form.save()
            obj.llibre = llibre
            obj.editor = request.user
            seleccionar_it(obj, llibre)
            obj.save()
            return redirect(request.path_info)
    else:
        form = SolicitarMaquetacioForm()
    return render(request, "enviar_llibre_publicar.html", {'form': form})


def seleccionar_it(solicitud, llibre):
    it_lliures = CustomUser.objects.filter(is_IT=True, lliure=True)
    it_aux = it_lliures[0]
    llibre.it = it_aux
    llibre.save()
    solicitud.it = it_aux
    it = CustomUser.objects.get(email=it_aux)
    it.lliure = False
    it.save()
    notificacio = Notificacio()
    notificacio.missatge = "Tens un nova sol·licitud de publicació assignada"
    notificacio.usuari = it_aux
    data = datetime.now()
    notificacio.data = data
    notificacio.llibre = llibre
    notificacio.save()


def solicitudTraduccio(request, pk):
    llibre = Llibre.objects.get(pk=pk)
    if request.method == 'POST':
        form = SolicitarTraduccioForm(request.POST)
        if form.is_valid():
            obj = form.save()
            obj.llibre = llibre
            obj.editor = request.user
            idioma = obj.idioma
            obj.save()
            traduirLlibre(llibre, idioma)
            # notificarEditorTraduccio(llibre)
            return redirect(request.path_info)
    else:
        form = SolicitarTraduccioForm()
    return render(request, 'solicitud_traduccio.html', {'form': form, 'llibre': llibre})


def traduirLlibre(llibre, idioma):

    pdf = llibre.pdf.path
    txt = llibre.txt.path
    traduccio = llibre.traduccio.path

    with open(pdf, 'rb') as pdf_file, open(txt, 'w') as txt_file:
        read_pdf = PyPDF2.PdfFileReader(pdf_file)
        number_of_pages = read_pdf.getNumPages()
        for page_number in range(number_of_pages):
            page = read_pdf.getPage(page_number)
            page_content = page.extractText()
            txt_file.write(page_content)

    translator = Translator(to_lang=idioma)

    with open(txt, 'r') as textOriginal:
        data = textOriginal.read()
    to_translate = data[:500]
    translation = translator.translate(to_translate)

    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('arial', size=12)
    pdf.multi_cell(190, 10, txt=translation)
    pdf.output(traduccio)


    # with open(llibre.traduccio, "wb") as llibreTraduccioStream:
    #    translation.write(llibreTraduccioStream)


def dirtraduccions(request, pk):
    llibre = Llibre.objects.get(pk=pk)
    context = {
        "llibre": llibre,
    }
    return render(request, 'directori_traduccions.html', context)


def retallarobra(llibre):
    obra = PdfFileReader(llibre.pdf)
    retall = PdfFileWriter()
    for i in range(15):
        retall.addPage(obra.getPage(i))
        with open(llibre.retall, "wb") as retall_stream:
            retall.write(retall_stream)
    # FALCA
    falca = PdfFileReader("/static/altres/falca.pdf")
    retallfalcat = PdfFileMerger()
    retallfalcat.append(retall)
    retallfalcat.append(falca)
    with open(llibre.falcat, "wb") as retallfalcat_stream:
        retallfalcat.write(retallfalcat_stream)
    llibre.save()


def retallarobra(llibre):
    obra = PdfFileReader(llibre.pdf)
    falca = PdfFileReader("/static/altres/falca.pdf")

    retallfalcat = PdfFileWriter()

    retallfalcat.addPage(obra.getPage(range(15)))
    retallfalcat.addPage(falca)

    with open(llibre.retallfalcat, "wb") as retallfalcatStream:
        retallfalcat.write(retallfalcatStream)

    llibre.save()
