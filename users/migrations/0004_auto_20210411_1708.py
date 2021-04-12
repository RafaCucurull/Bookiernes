# Generated by Django 3.1.7 on 2021-04-11 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210411_1445'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Email address'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_Editor',
            field=models.BooleanField(default=False, verbose_name='Editor'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_Escriptor',
            field=models.BooleanField(default=False, verbose_name='Escriptor'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_IT',
            field=models.BooleanField(default=False, verbose_name='IT'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='is_Maquetacio',
            field=models.BooleanField(default=False, verbose_name='Maquetació'),
        ),
    ]