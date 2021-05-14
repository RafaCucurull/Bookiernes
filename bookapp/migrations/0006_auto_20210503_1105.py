# Generated by Django 3.1.7 on 2021-05-03 11:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bookapp', '0005_auto_20210503_1054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solicitudimatges',
            name='dissenyador',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='dissenyador', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='solicitudimatges',
            name='editor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='editorbateria', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='solicitudimatges',
            name='llibre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='bookapp.llibre'),
        ),
    ]