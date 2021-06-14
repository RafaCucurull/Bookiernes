from django.core.exceptions import ValidationError
from django.forms import ModelForm, Textarea, CheckboxSelectMultiple, TextInput

from bookapp.models import Llibre, solicitudImatges, solicitudMaquetacio, Maquetacio, Imatge, solicitudPublicacio, \
    Missatge, solicitudTraduccio


class AfegirLlibreForm(ModelForm):
    class Meta:
        model = Llibre
        fields = ('pdf', 'nom_llibre', 'tematiques', 'sinopsis', 'num_pagines')
        widgets = {'nom_llibre': Textarea(attrs={'cols': 45, 'rows': 1}),
                   'sinopsis': Textarea(attrs={'cols': 50, 'rows': 6}),
                   'tematiques': CheckboxSelectMultiple,
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
        fields = ('pdf_maquetat', 'anotacions')
        widgets = {'anotacions': Textarea(attrs={'cols': 50, 'rows': 6})}


class SolicitarPublicacioForm(ModelForm):
    class Meta:
        model = solicitudPublicacio
        fields = ('anotacions',)


class EnviarMissatgeForm(ModelForm):
    class Meta:
        model = Missatge
        fields = ('cos_missatge', 'destinatari', )
        widgets = {'cos_missatge': Textarea(attrs={'cols': 70, 'rows': 6})}


class SolicitarTraduccioForm(ModelForm):
    class Meta:
        model = solicitudTraduccio
        fields = ('idioma',)
        widgets = {
            'idioma': TextInput(attrs={
                'class': "form-control",
                'style': 'width: 80%;background-color: linen;font-size: 30px; margin: auto;>',
                'placeholder': 'Codi del idioma...'
            }),
        }

    # this function will be used for the validation
    def clean(self):
        super(SolicitarTraduccioForm, self).clean()

        idioma = self.cleaned_data.get('idioma')

        # Si el codi no és de 2 caràcters
        if len(idioma) <= 1:
            raise ValidationError("El codi ha de ser de 2 caràcters")
        if any(chr.isdigit() for chr in idioma):
            raise ValidationError("El codi ha de ser de 2 caràcters alfabètics")
        if idioma != "en" and idioma != "es" and idioma != "pt" and idioma != "zh":
            raise ValidationError("El codi no correspon a ningun de la taula")

        return self.cleaned_data
