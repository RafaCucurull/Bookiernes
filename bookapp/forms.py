from django.forms import ModelForm, Textarea, CheckboxSelectMultiple

from bookapp.models import Llibre


class AfegirLlibreForm(ModelForm):

    class Meta:
        model = Llibre
        fields = ('pdf','nom_llibre','tematiques', 'sinopsis')
        widgets = {'nom_llibre': Textarea(attrs={'cols': 45, 'rows': 1}),
                   'sinopsis': Textarea(attrs={'cols': 50, 'rows': 10}),
                   'tematiques': CheckboxSelectMultiple}