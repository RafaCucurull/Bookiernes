from django.contrib import admin

from bookapp.models import Llibre, TematiquesLlibre, Tematica, Consulta, Comentari, Notificacio, Imatge, \
    solicitudImatges, solicitudMaquetacio, Maquetacio, solicitudTraduccio, Traduccio, Missatge


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

class ImatgeAdmin(admin.ModelAdmin):
    pass

class solimgAdmin(admin.ModelAdmin):
    pass

class solmaqAdmin(admin.ModelAdmin):
    pass

class maqAdmin(admin.ModelAdmin):
    pass

class missatgeAdmin(admin.ModelAdmin):
    pass

class soltradAdmin(admin.ModelAdmin):
    pass

class tradAdmin(admin.ModelAdmin):
    pass

admin.site.register(Llibre, LlibreAdmin)
admin.site.register(Tematica, TematicaAdmin)
admin.site.register(TematiquesLlibre, TematiquesLlibreAdmin)
admin.site.register(Consulta, ConsultaAdmin)
admin.site.register(Comentari, ComentariAdmin)
admin.site.register(Notificacio, NotificacioAdmin)
admin.site.register(Imatge, ImatgeAdmin)
admin.site.register(solicitudImatges, solimgAdmin)
admin.site.register(solicitudMaquetacio, solmaqAdmin)
admin.site.register(Maquetacio, maqAdmin)

admin.site.register(Missatge, missatgeAdmin)

admin.site.register(solicitudTraduccio, soltradAdmin)
admin.site.register(Traduccio, tradAdmin)
