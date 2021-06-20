# Generated by Django 3.1.7 on 2021-06-20 09:09

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
            name='Imatge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(blank=True, max_length=70, null=True)),
                ('image', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Llibre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_llibre', models.CharField(max_length=70)),
                ('sinopsis', models.TextField(max_length=3000)),
                ('pdf', models.FileField(upload_to='')),
                ('pdf_retall', models.FileField(blank=True, null=True, upload_to='')),
                ('textPla', models.FileField(blank=True, null=True, upload_to='')),
                ('es', models.FileField(blank=True, null=True, upload_to='')),
                ('es_retall', models.FileField(blank=True, null=True, upload_to='')),
                ('en', models.FileField(blank=True, null=True, upload_to='')),
                ('en_retall', models.FileField(blank=True, null=True, upload_to='')),
                ('pt', models.FileField(blank=True, null=True, upload_to='')),
                ('pt_retall', models.FileField(blank=True, null=True, upload_to='')),
                ('zh', models.FileField(blank=True, null=True, upload_to='')),
                ('zh_retall', models.FileField(blank=True, null=True, upload_to='')),
                ('coleccio', models.CharField(blank=True, max_length=100, null=True)),
                ('num_pagines', models.IntegerField()),
                ('comentari_it', models.TextField(blank=True, max_length=3000)),
                ('publicat', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Maquetacio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf_maquetat', models.FileField(blank=True, null=True, upload_to='')),
                ('anotacions', models.CharField(blank=True, max_length=70, null=True)),
                ('portada', models.ImageField(blank=True, null=True, upload_to='')),
                ('contraportada', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Missatge',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cos_missatge', models.CharField(blank=True, max_length=70, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Notificacio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('missatge', models.CharField(max_length=100)),
                ('data', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Publicacio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pdf_a_publicar', models.FileField(blank=True, null=True, upload_to='')),
                ('anotacions', models.CharField(blank=True, max_length=70, null=True)),
                ('portada', models.ImageField(blank=True, null=True, upload_to='')),
                ('contraportada', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='solicitudImatges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(blank=True, max_length=70, null=True)),
                ('context', models.CharField(blank=True, max_length=70, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='solicitudMaquetacio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anotacions', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='solicitudPublicacio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('anotacions', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='solicitudTraduccio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idioma', models.CharField(blank=True, max_length=2, null=True)),
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
            name='Traduccio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idioma', models.CharField(blank=True, max_length=2, null=True)),
                ('pdf_traduit', models.FileField(blank=True, null=True, upload_to='')),
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
    ]
