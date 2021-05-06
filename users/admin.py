from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('email', 'is_staff', 'is_active', 'is_Treballador', 'is_Escriptor', 'is_Editor', 'is_Dissenyador', 'is_Maquetacio', 'is_IT', 'lliure')
    list_filter = ('email', 'is_staff', 'is_active', 'is_Treballador', 'is_Escriptor', 'is_Editor', 'is_Dissenyador', 'is_Maquetacio', 'is_IT', 'lliure')
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_Treballador', 'is_Escriptor', 'is_Editor', 'is_Dissenyador', 'is_Maquetacio', 'is_IT', 'lliure')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email', 'password1', 'password2', 'is_staff', 'is_active', 'is_Treballador', 'is_Escriptor', 'is_Editor',
                'is_Maquetacio', 'is_Dissenyador',
                'is_IT', 'lliure')}
         ),
    )
    search_fields = ('email',)
    ordering = ('email',)


admin.site.register(CustomUser, CustomUserAdmin)
