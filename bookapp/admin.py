from django.contrib import admin

from bookapp.models import Llibre, Escriptor, Editor


class LlibreAdmin(admin.ModelAdmin):
    pass


class EscriptorAdmin(admin.ModelAdmin):
    pass


class EditorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Llibre, LlibreAdmin)
admin.site.register(Escriptor, EscriptorAdmin)
admin.site.register(Editor, EditorAdmin)
