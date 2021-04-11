from django.db import models


class Llibre(models.Model):
    nom_llibre = models.CharField(max_length=70)
    escriptor = models.ForeignKey('users.CustomUser', related_name="escriptor", on_delete=models.CASCADE)
    editor = models.ForeignKey('users.CustomUser', related_name="editor", on_delete=models.CASCADE)
    portada = models.CharField(max_length=100)
    sinopsis = models.TextField(max_length=300)
    tematiques = models.ManyToManyField('Tematica', related_name='tematiques', blank=True, through='TematiquesLlibre')
    pdf = models.FileField(upload_to='pdf')

    def __str__(self):
        return self.nom_llibre


class Tematica(models.Model):
    nom_tematica = models.CharField(max_length=20)
    descripcio_tematica = models.CharField(max_length=100)

    def __str__(self):
        return self.nom_tematica


class TematiquesLlibre(models.Model):
    llibre = models.ForeignKey('Llibre', on_delete=models.CASCADE)
    tematica = models.ForeignKey('Tematica', on_delete=models.CASCADE)


class Consulta(models.Model):
    usuari = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    assumpte = models.CharField(max_length=100)
    cos = models.TextField()


class Comentari(models.Model):
    usuari = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    titol = models.CharField(max_length=100)
    descripcio = models.TextField()
    llibre = models.ForeignKey('Llibre', on_delete=models.CASCADE)
