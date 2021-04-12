from django.db import models
from django.urls import reverse


class Llibre(models.Model):
    nom_llibre = models.CharField(max_length=70)
    escriptor = models.ForeignKey('users.CustomUser', related_name="escriptor", on_delete=models.CASCADE)
    editor = models.ForeignKey('users.CustomUser', related_name="editor", on_delete=models.CASCADE)
    portada = models.CharField(max_length=100)
    sinopsis = models.TextField(max_length=300)
    tematiques = models.ManyToManyField('Tematica', related_name='tematiques', blank=True, through='TematiquesLlibre')
    pdf = models.FileField(upload_to='pdf')
    coleccio = models.CharField(max_length=100, blank=True)
    num_pagines = models.IntegerField()

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

