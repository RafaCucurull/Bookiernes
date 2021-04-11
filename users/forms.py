from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser
from django import forms


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm):
        model = CustomUser
        fields = ('email',)


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('email',)

class SignUpForm(UserCreationForm):

    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    is_Escriptor = forms.BooleanField()
    is_Editor = forms.BooleanField()
    is_Maquetacio = forms.BooleanField()
    is_IT = forms.BooleanField()
    class Meta:
        model = CustomUser
        fields = ('email', 'is_Escriptor','is_Editor', 'is_Maquetacio', 'is_IT')