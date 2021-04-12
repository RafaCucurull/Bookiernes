from django.contrib import admin

from bookapp.models import Llibre, TematiquesLlibre, Tematica, Consulta, Comentari, Notificacio


class LlibreAdmin(admin.ModelAdmin):
    pass


class TematicaAdmin(admin.ModelAdmin):
    pass


class TematiquesLlibreAdmin(admin.ModelAdmin):
    pass


class ConsultaAdmin(admin.ModelAdmin):
    pass


class ComentariAdmin(admin.ModelAdmin):
    pass

class NotificacioAdmin(admin.ModelAdmin):
    pass



admin.site.register(Llibre, LlibreAdmin)
admin.site.register(Tematica, TematicaAdmin)
admin.site.register(TematiquesLlibre, TematiquesLlibreAdmin)
admin.site.register(Consulta, ConsultaAdmin)
admin.site.register(Comentari, ComentariAdmin)
admin.site.register(Notificacio, NotificacioAdmin)
