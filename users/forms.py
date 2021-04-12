from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser
from django import forms


class CustomUserCreationForm(UserCreationForm):
    email = forms.CharField(help_text="Introdueix un format correcte de correu electrònic (p.ex. example@gmail.com)")
    password1 = forms.CharField(
        help_text=["La teva contrassenya no pot ser similar a l'altra informació personal teva.",
                   "La teva contrassenya ha de tenir almenys 8 caràcters.",
                   "La teva contrassenya no pot ser una comunment usada.",
                   "La teva contrassenya no pot ser completament numèrica."])
    password2 = forms.CharField(help_text="Introdueix la mateixa contrassenya que anteriorment, per verificació.")

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email', 'is_Editor', 'is_Escriptor', 'is_Maquetacio', 'is_IT', 'password1', 'password2')


class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = CustomUser
        fields = ('email',)
