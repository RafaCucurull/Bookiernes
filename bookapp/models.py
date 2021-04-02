from django.db import models


class Llibre(models.Model):
    nom_llibre = models.CharField(max_length=70)
    escriptor = models.ForeignKey('Escriptor', on_delete=models.CASCADE)
    editor = models.ForeignKey('Editor', on_delete=models.CASCADE)
    portada = models.CharField(max_length=100)

    def __str__(self):
        return self.nom_llibre


class Escriptor(models.Model):
    nom_escriptor = models.CharField(max_length=20)
    primer_cognom_escriptor = models.CharField(max_length=20)
    segon_cognom_escriptor = models.CharField(max_length=20)

    def __str__(self):
        return self.nom_escriptor + " " + self.primer_cognom_escriptor + " " + self.segon_cognom_escriptor


class Editor(models.Model):
    nom_editor = models.CharField(max_length=20)
    primer_cognom_editor = models.CharField(max_length=20)
    segon_cognom_editor = models.CharField(max_length=20)

    def __str__(self):
        return self.nom_editor + " " + self.primer_cognom_editor + " " + self.segon_cognom_editor
