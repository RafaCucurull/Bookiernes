# Generated by Django 3.1.7 on 2021-05-04 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookapp', '0009_maquetacio'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='maquetacio',
            name='llibre',
        ),
        migrations.AddField(
            model_name='llibre',
            name='maquetacio',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='maquetacio', to='bookapp.maquetacio'),
        ),
        migrations.AddField(
            model_name='maquetacio',
            name='anotacions',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
        migrations.AddField(
            model_name='maquetacio',
            name='pdf_maquetat',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
