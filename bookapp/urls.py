from django.urls import path

from bookapp import views

urlpatterns = [
    path('', views.homePage, name="home"),
    path('escriptori', views.Escriptori, name="escriptori"),
    path('afegirllibre', views.afegirLlibre, name="afegirllibre"),
    path('area_edicio', views.areaedicio, name='areaedicio'),
    path('area_escriptor', views.areaescriptor, name='areaescriptor'),
    path('escriptori_escriptor', views.escriptoriescriptor, name='escriptoriescriptor'),
    path('enviarnovaversio', views.enviarnovaversio, name='enviarnovaversio'),
    path('canviardocument', views.canviardocument, name='canviardocument'),
    path('commentseditor', views.commentseditor, name='commentseditor')
]