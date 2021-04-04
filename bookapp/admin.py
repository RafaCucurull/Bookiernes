from django.contrib import admin

from bookapp.models import Llibre, TematiquesLlibre, Tematica, Consulta


class LlibreAdmin(admin.ModelAdmin):
    pass


class TematicaAdmin(admin.ModelAdmin):
    pass


class TematiquesLlibreAdmin(admin.ModelAdmin):
    pass


class ConsultaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Llibre, LlibreAdmin)
admin.site.register(Tematica, TematicaAdmin)
admin.site.register(TematiquesLlibre, TematiquesLlibreAdmin)
admin.site.register(Consulta, ConsultaAdmin)

