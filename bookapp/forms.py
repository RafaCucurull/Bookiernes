from django.forms import ModelForm, Textarea, CheckboxSelectMultiple

from bookapp.models import Llibre, solicitudImatges, solicitudMaquetacio

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
        fields = ('nom',)


class SolicitarMaquetacioForm(ModelForm):
    class Meta:
        model = solicitudMaquetacio
        fields = ('anotacions',)


class cercaImatgeBDD(forms.Form):
    nom_imatge = forms.TextInput()
