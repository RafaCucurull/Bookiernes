from django.forms import ModelForm, Textarea, CheckboxSelectMultiple, TextInput

from bookapp.models import Llibre, solicitudImatges, solicitudMaquetacio, Maquetacio, Imatge

from django import forms


class AfegirLlibreForm(ModelForm):
    class Meta:
        model = Llibre
        fields = ('pdf', 'nom_llibre', 'tematiques', 'sinopsis', 'coleccio', 'num_pagines')
        widgets = {'nom_llibre': Textarea(attrs={'cols': 45, 'rows': 1}),
                   'sinopsis': Textarea(attrs={'cols': 50, 'rows': 6}),
                   'tematiques': CheckboxSelectMultiple,
                   'coleccio': Textarea(attrs={'cols': 45, 'rows': 1}),
                   'num_pagines': Textarea(attrs={'cols': 45, 'rows': 1}),
                   }


class SolicitarImatgesForm(ModelForm):
    class Meta:
        model = solicitudImatges
        fields = ('nom', 'context')
        widgets = {
            'nom': TextInput(attrs={
                'class': "form-control",
                'style': 'width: 100%;background-color: linen;font-size: 30px',
                'placeholder': 'Nom de la imatge...'
            }),
            'context': TextInput(attrs={
                'class': "form-control",
                'style': 'width: 100%;background-color: linen;font-size: 30px',
                'placeholder': 'Context de la imatge...'
            }),
        }

class pujarImatge(ModelForm):
    class Meta:
        model = Imatge
        fields = ('image',)

class SolicitarMaquetacioForm(ModelForm):
    class Meta:
        model = solicitudMaquetacio
        fields = ('anotacions',)


class PujarMaquetacio(ModelForm):
    class Meta:
        model = Maquetacio
        fields = ('pdf_maquetat', 'anotacions', 'portada', 'contraportada')
