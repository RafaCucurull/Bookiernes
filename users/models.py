from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('Email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    #Funcions laborals de l'empresa
    is_Treballador = models.BooleanField(default=False)
    is_Escriptor = models.BooleanField(default=False)
    is_Editor = models.BooleanField(default=False)
    is_Maquetacio = models.BooleanField(default=False)
    is_IT = models.BooleanField(default=False)
    lliure = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email
