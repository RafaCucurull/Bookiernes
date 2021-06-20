from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from bookapp import models
from bookapp.forms import AfegirLlibreForm, SolicitarImatgesForm, SolicitarMaquetacioForm, PujarMaquetacio, pujarImatge,SolicitarPublicacioForm, EnviarMissatgeForm, SolicitarTraduccioForm
from bookapp.models import Llibre, TematiquesLlibre, Comentari, Notificacio, Tematica, Imatge, Missatge
from users.forms import ConfiguracioForm
from users.models import CustomUser
from django.core.files.storage import FileSystemStorage
from datetime import datetime
import PyPDF2
from translate import Translator
from fpdf import FPDF
from django.urls import reverse
from django.core.files.base import File


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
            afegirDocuments(obj)
            seleccionar_editor(obj)
            obj.escriptor = request.user
            obj.save()
            return redirect('/escriptori')
    else:
        form = AfegirLlibreForm()

    return render(request, "afegirllibre.html", {'form': form})


def afegirDocuments(llibre):
    with open('text.txt') as f:
        llibre.textPla.save('text', File(f))
    with open('text.txt') as f:
        llibre.pdf_retall.save('retall', File(f))

    with open('text.txt') as esdoc:
        llibre.es.save('es', File(esdoc))
    with open('text.txt') as g:
        llibre.es_retall.save('esRetall', File(g))

    with open('text.txt') as g:
        llibre.en.save('en', File(g))
    with open('text.txt') as h:
        llibre.en_retall.save('enRetall', File(h))

    with open('text.txt') as g:
        llibre.pt.save('pt', File(g))
    with open('text.txt') as h:
        llibre.pt_retall.save('ptRetall', File(h))

    with open('text.txt') as g:
        llibre.zh.save('zh', File(g))
    with open('text.txt') as h:
        llibre.zh_retall.save('zhRetall', File(h))


def seleccionar_editor(llibre):
    editors_lliures = CustomUser.objects.filter(is_Editor=True, lliure=True)
    editoraux = editors_lliures[0]
    llibre.editor = editoraux
    editor = CustomUser.objects.get(email=editoraux)
    #editor.lliure = False
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

def enviarmissatge(request):
    if request.method == 'POST':
        form = EnviarMissatgeForm(request.POST)
        if form.is_valid():
            obj = form.save()
            obj.autor = request.user
            obj.save()
            return redirect(request.path_info)
    else:
        form = EnviarMissatgeForm()
    context = {
        'form': form
    }
    return render(request, "missatge.html", context)



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
        return redirect(reverse('areaescriptor', kwargs={'pk': pk}))

    return render(request, 'enviar_nova_versio.html', context)


def commentseditor(request, pk):

    llibre = Llibre.objects.get(pk=pk)
    usuari = CustomUser.objects.get(email=request.user)
    comentaris = Comentari.objects.filter(usuari=usuari, llibre=llibre)
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
        "llibre": llibre
    }
    if request.method == "POST" and request.FILES['pdf']:
        pdf = request.FILES['pdf']
        print(pdf)
        fs = FileSystemStorage()
        filename = fs.save(pdf.name, pdf)

        llibre.pdf = fs.url(filename)
        print(llibre.pdf)
        llibre.save()
        return redirect(reverse('areaedicio', kwargs={'pk': pk}))

    return render(request, 'canviar_document.html', context)


def notificacions(request):
    notificacions = Notificacio.objects.filter(usuari=request.user)
    context = {
        "object_list": notificacions
    }
    return render(request, "notificacions.html", context)

def veuremissatge(request):
    missatges = Missatge.objects.filter(destinatari=request.user)
    context = {
        "object_list": missatges
    }
    return render(request, "veuremissatge.html", context)


def comments(request, pk):
    llibre = Llibre.objects.get(pk=pk)
    comentaris = Comentari.objects.filter(llibre=llibre)
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
            return redirect(reverse('areaedicio' , kwargs={'pk':pk}))
    else:
        form = SolicitarImatgesForm()
    context = {
        'llibre': llibre,
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
    #dissenyador.lliure = False
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
    maquetacio = llibre.maquetacio
    context = {
        "llibre": llibre,
        "maquetacio": maquetacio
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
            return redirect(reverse('areaedicio' , kwargs={'pk':pk}))
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
    #maquetador.lliure = False
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


def enviarbat(request, pk, pksol):
    llibre = Llibre.objects.get(pk=pk)
    solicitud = models.solicitudImatges.objects.filter(pk=pksol)
    if request.method == 'POST':
        form = pujarImatge(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            obj.save()
            llibre.imatges.add(obj)
            llibre.save()
            solicitud.delete()
            notificarEditorImatges(llibre)
            return redirect(reverse('areadismaq' , kwargs={'pk':pk}))
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


def enviarMaquetacio(request, pk, pksol):
    llibre = Llibre.objects.get(pk=pk)
    solicitud = models.solicitudMaquetacio.objects.filter(pk=pksol)
    if request.method == 'POST':
        form = PujarMaquetacio(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save()
            obj.save()
            llibre.maquetacio = obj
            llibre.save()
            solicitud.delete()
            notificarEditorMaquetacio(llibre)
            return redirect(reverse('areadismaq' , kwargs={'pk':pk}))
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


def eliminarnotificacio(request, pknotificacio):
    Notificacio.objects.filter(pk=pknotificacio).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def eliminarmissatge(request, pkmissatge):
    Missatge.objects.filter(pk=pkmissatge).delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


def solicitudpublicacio(request, pk):
    llibre = Llibre.objects.get(pk=pk)
    if request.method == 'POST':
        form = SolicitarPublicacioForm(request.POST)
        if form.is_valid():
            anotacions = request.POST.get('anotacions')
            obj = form.save()
            obj.llibre = llibre
            obj.editor = request.user
            llibre.comentari_it = anotacions
            seleccionar_it(obj, llibre)
            llibre.save()
            obj.save()
            return redirect(reverse('areaedicio' , kwargs={'pk':pk}))
    else:
        form = SolicitarMaquetacioForm()
    retallarobra(llibre)
    return render(request, "enviar_llibre_publicar.html", {'form': form})


def seleccionar_it(solicitud, llibre):
    it_lliures = CustomUser.objects.filter(is_IT=True, lliure=True)
    it_aux = it_lliures[0]
    llibre.it = it_aux
    llibre.save()
    solicitud.it = it_aux
    it = CustomUser.objects.get(email=it_aux)
    #it.lliure = False
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


def galeriaTraduccions(request, pk):
    llibre = Llibre.objects.get(pk=pk)
    context = {
        'llibre': llibre,
    }
    return render(request, "galeria_traduccions.html", context)


def traduirLlibre(llibre, idioma):
    pdf = llibre.pdf.path
    txt = llibre.textPla.path

    if (idioma == 'es'):
        traduccio = llibre.es.path

    if (idioma == 'en'):
        traduccio = llibre.en.path

    elif (idioma == 'pt'):
        traduccio = llibre.pt.path

    elif (idioma == 'zh'):
        traduccio = llibre.zh.path

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
    pdf.multi_cell(190, 12, txt=translation)
    pdf.output(traduccio+".pdf")

    # with open(llibre.traduccio, "wb") as llibreTraduccioStream:
    #    translation.write(llibreTraduccioStream)


def dirtraduccions(request, pk):
    llibre = Llibre.objects.get(pk=pk)
    context = {
        "llibre": llibre,
    }
    return render(request, 'directori_traduccions.html', context)


def retallarobra(llibre):
    # PDF

    retallPDF = FPDF()
    retallPDF.add_page()
    retallPDF.set_font("Arial", size=15)
    f = open(llibre.textPla.path, "r")
    for x in f:
        retallPDF.multi_cell(190, 10, txt=x, border=0, align='J', fill=False)
    retallPDF.cell(190, 10, txt="HEU ARRIBAT AL FINAL DEL FRAGMENT DE MOSTRA",
                   ln=1, align='C')
    retallPDF.cell(190, 10, txt="Per continuar gaudint del contigut del llibre, subscriviu-vos a Bookiernes",
                   ln=2, align='C')
    retallPDF.output(llibre.pdf_retall.path+".pdf")

    """
    # ES

    retallES = FPDF()
    retallES.add_page()
    retallES.set_font("Arial", size=15)

    es = open(llibre.textPla.path, "r")

    for x in es:
        retallES.multi_cell(200, 10, txt=x, border=0, align='J', fill=False)
    retallES.cell(200, 10, txt="HEU ARRIBAT AL FINAL DEL FRAGMENT DE MOSTRA",
                  ln=1, align='C')
    retallES.cell(200, 10, txt="Per continuar gaudint del contigut del llibre, subscriviu-vos a Bookiernes",
                  ln=2, align='C')
    retallES.output(llibre.es_retall.path)

    # EN

    retallEN = FPDF()
    retallEN.add_page()
    retallEN.set_font("Arial", size=15)
    en = open(llibre.en.path, "r")
    for x in en:
        retallEN.multi_cell(200, 10, txt=x, border=0, align='J', fill=False)
    retallEN.cell(200, 10, txt="HEU ARRIBAT AL FINAL DEL FRAGMENT DE MOSTRA",
                  ln=1, align='C')
    retallEN.cell(200, 10, txt="Per continuar gaudint del contigut del llibre, subscriviu-vos a Bookiernes",
                  ln=2, align='C')
    retallEN.output(llibre.en_retall.path)

    # PT

    retallPT = FPDF()
    retallPT.add_page()
    retallPT.set_font("Arial", size=15)
    pt = open(llibre.pt.path, "r")
    for x in pt:
        retallPT.multi_cell(200, 10, txt=x, border=0, align='J', fill=False)
    retallPT.cell(200, 10, txt="HEU ARRIBAT AL FINAL DEL FRAGMENT DE MOSTRA",
                  ln=1, align='C')
    retallPT.cell(200, 10, txt="Per continuar gaudint del contigut del llibre, subscriviu-vos a Bookiernes",
                  ln=2, align='C')
    retallPT.output(llibre.pt_retall.path)

    # ZH

    retallZH = FPDF()
    retallZH.add_page()
    retallZH.set_font("Arial", size=15)
    zh = open(llibre.zh.path, "r")
    for x in zh:
        retallZH.multi_cell(200, 10, txt=x, border=0, align='J', fill=False)
    retallZH.cell(200, 10, txt="HEU ARRIBAT AL FINAL DEL FRAGMENT DE MOSTRA",
                  ln=1, align='C')
    retallZH.cell(200, 10, txt="Per continuar gaudint del contigut del llibre, subscriviu-vos a Bookiernes",
                  ln=2, align='C')
    retallZH.output(llibre.zh_retall.path)

    """

    llibre.save()

def perfil(request, pkperfil):
    usuari = CustomUser.objects.get(email=request.user)
    llistallibres = list()
    if usuari.is_Editor:
        llistallibres = Llibre.objects.filter(editor=usuari)
    if usuari.is_Escriptor:
        llistallibres = Llibre.objects.filter(escriptor=usuari)
    if usuari.is_Dissenyador:
        llistallibres = Llibre.objects.filter(dissenyador=usuari)
    if usuari.is_Maquetacio:
        llistallibres = Llibre.objects.filter(maquetador=usuari)
    if usuari.is_IT:
        llistallibres = Llibre.objects.filter(it=usuari)
    context = {
        'llibres': llistallibres
    }
    return render(request, 'profile.html', context)

def configuracio(request, pkperfil):
    usuari = CustomUser.objects.get(pk=pkperfil)
    if request.method == 'POST':
        form = ConfiguracioForm(request.POST)
        if form.is_valid():
            usuari.nom = form.cleaned_data.get('nom')
            usuari.edat = form.cleaned_data.get('edat')
            usuari.sexe = form.cleaned_data.get('sexe')
            usuari.save()
            return redirect(reverse('perfil', kwargs={'pkperfil': pkperfil}))
    else:
        form = ConfiguracioForm()
    return render(request, 'configuracio_perfil.html', {'form': form})
