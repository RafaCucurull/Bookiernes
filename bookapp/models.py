from django.db import models
from django.urls import reverse


class Llibre(models.Model):
    nom_llibre = models.CharField(max_length=70)
    escriptor = models.ForeignKey('users.CustomUser', related_name="escriptor", on_delete=models.CASCADE, blank=True,
                                  null=True)
    editor = models.ForeignKey('users.CustomUser', related_name="editor", on_delete=models.CASCADE, blank=True,
                               null=True)
    it = models.ForeignKey('users.CustomUser', related_name="it", on_delete=models.CASCADE, blank=True, null=True)
    dissenyador = models.ForeignKey('users.CustomUser', related_name="dissenyador", on_delete=models.CASCADE,
                                    blank=True,
                                    null=True)
    maquetador = models.ForeignKey('users.CustomUser', related_name="maquetador", on_delete=models.CASCADE, blank=True,
                                   null=True)
    sinopsis = models.TextField(max_length=3000)
    tematiques = models.ManyToManyField('Tematica', related_name='tematiques', blank=True, through='TematiquesLlibre')
    pdf = models.FileField()
    pdf_retall = models.FileField(blank=True, null=True)
    textPla = models.FileField(blank=True, null=True)
    es = models.FileField(blank=True, null=True)
    es_retall = models.FileField(blank=True, null=True)
    en = models.FileField(blank=True, null=True)
    en_retall = models.FileField(blank=True, null=True)
    pt = models.FileField(blank=True, null=True)
    pt_retall = models.FileField(blank=True, null=True)
    zh = models.FileField(blank=True, null=True)
    zh_retall = models.FileField(blank=True, null=True)
    coleccio = models.CharField(max_length=100, blank=True, null=True)
    num_pagines = models.IntegerField()
    comentari_it = models.TextField(max_length=3000, blank=True)
    publicat = models.BooleanField(default=False)
    imatges = models.ManyToManyField('Imatge', related_name='imatgesassociades', blank=True)
    maquetacio = models.ForeignKey('Maquetacio', related_name='maquetacio', null=True, blank=True,
                                   on_delete=models.CASCADE)
    def __str__(self):
        return self.nom_llibre

    def get_absolute_url(self):
        return reverse("areaedicio", args=[str(self.pk)])


class Tematica(models.Model):
    nom_tematica = models.CharField(max_length=20)
    descripcio_tematica = models.CharField(max_length=100)

    def __str__(self):
        return self.nom_tematica


class TematiquesLlibre(models.Model):
    llibre = models.ForeignKey('Llibre', on_delete=models.CASCADE)
    tematica = models.ForeignKey('Tematica', on_delete=models.CASCADE)

    def __str__(self):
        return self.tematica.nom_tematica


class Consulta(models.Model):
    usuari = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    assumpte = models.CharField(max_length=100)
    cos = models.TextField()


class Comentari(models.Model):
    usuari = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    titol = models.CharField(max_length=100)
    descripcio = models.TextField()
    llibre = models.ForeignKey('Llibre', on_delete=models.CASCADE)


class Notificacio(models.Model):
    usuari = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    missatge = models.CharField(max_length=100)
    data = models.DateTimeField(auto_now=True, blank=True, null=True)
    llibre = models.ForeignKey('Llibre', on_delete=models.CASCADE)


class solicitudImatges(models.Model):
    nom = models.CharField(max_length=70, null=True, blank=True)
    context = models.CharField(max_length=70, null=True, blank=True)
    llibre = models.ForeignKey('Llibre', on_delete=models.CASCADE, null=True, blank=True)
    editor = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name='editorbateria', null=True,
                               blank=True)
    dissenyador = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name='dissenyadorimatge',
                                    null=True,
                                    blank=True)


class Imatge(models.Model):
    nom = models.CharField(max_length=70, null=True, blank=True)
    image = models.ImageField()


class solicitudMaquetacio(models.Model):
    anotacions = models.CharField(max_length=70)
    llibre = models.ForeignKey('Llibre', on_delete=models.CASCADE, null=True, blank=True)
    editor = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name='editormaquetacio', null=True,
                               blank=True)
    maquetador = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name='maquetadorsolicitud',
                                   null=True,
                                   blank=True)


class Maquetacio(models.Model):
    pdf_maquetat = models.FileField(null=True, blank=True)
    anotacions = models.CharField(max_length=70, null=True, blank=True)
    portada = models.ImageField(null=True, blank=True)
    contraportada = models.ImageField(null=True, blank=True)


class solicitudPublicacio(models.Model):
    anotacions = models.CharField(max_length=70)
    llibre = models.ForeignKey('Llibre', on_delete=models.CASCADE, null=True, blank=True)
    editor = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name='editorpublicacio', null=True,
                               blank=True)
    IT = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name='itsolicitud', null=True,
                           blank=True)


class Publicacio(models.Model):
    pdf_a_publicar = models.FileField(null=True, blank=True)
    anotacions = models.CharField(max_length=70, null=True, blank=True)
    portada = models.ImageField(null=True, blank=True)
    contraportada = models.ImageField(null=True, blank=True)


class Missatge(models.Model):
    autor = models.ForeignKey('users.CustomUser', related_name="autormissatge", on_delete=models.CASCADE, blank=True, null=True)
    cos_missatge = models.CharField(max_length=70, null=True, blank=True)
    destinatari = models.ForeignKey('users.CustomUser', related_name="destmissatge", on_delete=models.CASCADE, blank=True, null=True)


class solicitudTraduccio(models.Model):
    idioma = models.CharField(max_length=2, null=True, blank=True)
    llibre = models.ForeignKey('Llibre', on_delete=models.CASCADE, null=True, blank=True)
    editor = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name='editortraduccio',
                               null=True,
                               blank=True)


class Traduccio(models.Model):
    idioma = models.CharField(max_length=2, null=True, blank=True)
    pdf_traduit = models.FileField(null=True, blank=True)
