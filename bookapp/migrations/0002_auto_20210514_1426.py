# Generated by Django 3.1.7 on 2021-05-14 12:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='solicitudmaquetacio',
            name='editor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='editormaquetacio', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='solicitudmaquetacio',
            name='llibre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bookapp.llibre'),
        ),
        migrations.AddField(
            model_name='solicitudmaquetacio',
            name='maquetador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='maquetadorsolicitud', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='solicitudimatges',
            name='dissenyador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dissenyadorimatge', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='solicitudimatges',
            name='editor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='editorbateria', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='solicitudimatges',
            name='llibre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bookapp.llibre'),
        ),
        migrations.AddField(
            model_name='notificacio',
            name='llibre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookapp.llibre'),
        ),
        migrations.AddField(
            model_name='notificacio',
            name='usuari',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='llibre',
            name='dissenyador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dissenyador', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='llibre',
            name='editor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='editor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='llibre',
            name='escriptor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='escriptor', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='llibre',
            name='imatges',
            field=models.ManyToManyField(blank=True, related_name='imatgesassociades', to='bookapp.Imatge'),
        ),
        migrations.AddField(
            model_name='llibre',
            name='it',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='it', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='llibre',
            name='maquetacio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='maquetacio', to='bookapp.maquetacio'),
        ),
        migrations.AddField(
            model_name='llibre',
            name='maquetador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='maquetador', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='llibre',
            name='tematiques',
            field=models.ManyToManyField(blank=True, related_name='tematiques', through='bookapp.TematiquesLlibre', to='bookapp.Tematica'),
        ),
        migrations.AddField(
            model_name='consulta',
            name='usuari',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comentari',
            name='llibre',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookapp.llibre'),
        ),
        migrations.AddField(
            model_name='comentari',
            name='usuari',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]