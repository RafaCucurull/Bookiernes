# Generated by Django 3.1.7 on 2021-05-01 10:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comentari',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titol', models.CharField(max_length=100)),
                ('descripcio', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assumpte', models.CharField(max_length=100)),
                ('cos', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Llibre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_llibre', models.CharField(max_length=70)),
                ('portada', models.CharField(max_length=100)),
                ('sinopsis', models.TextField(max_length=3000)),
                ('pdf', models.FileField(upload_to='')),
                ('coleccio', models.CharField(blank=True, max_length=100)),
                ('num_pagines', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Tematica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_tematica', models.CharField(max_length=20)),
                ('descripcio_tematica', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='TematiquesLlibre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('llibre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookapp.llibre')),
                ('tematica', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookapp.tematica')),
            ],
        ),
        migrations.CreateModel(
            name='Notificacio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('missatge', models.CharField(max_length=100)),
                ('data', models.DateTimeField(blank=True, null=True)),
                ('llibre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bookapp.llibre')),
            ],
        ),
    ]
