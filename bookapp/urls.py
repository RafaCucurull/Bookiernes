from django.urls import path

from bookapp import views

urlpatterns = [
    path('', views.homePage, name="home"),
    path('escriptori', views.Escriptori, name="escriptori"),
    path('cataleg', views.cataleg, name="cataleg"),
    path('afegirllibre', views.afegirLlibre, name="afegirllibre"),
    path('area_edicio/<int:pk>', views.areaedicio, name='areaedicio'),
    path('area_escriptor/<int:pk>', views.areaescriptor, name='areaescriptor'),
    path('area_escriptor/<int:pk>/enviarnovaversio', views.enviarnovaversio, name='enviarnovaversio'),
    path('area_edicio/<int:pk>/canviardocument', views.canviardocument, name='canviardocument'),
    path('notificacions', views.notificacions, name='notificacions'),
    path('area_edicio/<int:pk>/commentseditor', views.commentseditor, name='commentseditor'),
    path('area_escriptor/<int:pk>/comments', views.comments, name='comments'),
    path('area_it/<int:pk>/publicarllibre', views.publicarllibre, name='publicarllibre'),
    path('area_maquetacio/imatges', views.solicitudsimatges_maq, name='solicitudimatges'),
    path('area_maquetacio/maquetacio', views.solicitudsmaquetacio_maq, name='solicitudmaquetacio'),
]