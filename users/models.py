from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('Email address'), unique=True)
    nom = models.CharField(max_length=70, default="")
    edat= models.CharField(max_length=70, default="")
    sexe = models.CharField(max_length=70, default="")
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    # Funcions laborals de l'empresa
    is_Treballador = models.BooleanField(default=False)
    is_Escriptor = models.BooleanField(default=False)
    is_Editor = models.BooleanField(default=False)
    is_Dissenyador = models.BooleanField(default=False)
    is_Maquetacio = models.BooleanField(default=False)
    is_IT = models.BooleanField(default=False)
    lliure = models.BooleanField(default=True)
    # Lectors
    is_Subscrit = models.BooleanField(default=False)
    is_NoSubscrit = models.BooleanField(default=False)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
