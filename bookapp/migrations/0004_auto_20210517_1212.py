# Generated by Django 3.1.7 on 2021-05-17 10:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0003_auto_20210514_1942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maquetacio',
            name='contraportada',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='maquetacio',
            name='portada',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
