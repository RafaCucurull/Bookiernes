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
    path('area_edicio/<int:pk>/dirbateriaimatges', views.dirbateriaimatges, name='dirbateriaimatges'),
    path('area_edicio/<int:pk>/galeriaimatges', views.galeriaimatges, name='galeriaimatges'),
    path('area_edicio/<int:pk>/dirmaquetacions', views.dirmaquetacions, name='dirmaquetacions'),
    path('area_edicio/<int:pk>/galeriamaquetacions', views.galeriamaquetacions, name='galeriamaquetacions'),
    path('area_escriptor/<int:pk>/comments', views.comments, name='comments'),
    path('area_it/<int:pk>/publicarllibre', views.publicarllibre, name='publicarllibre'),
    path('area_edicio/<int:pk>/solicitudimatges', views.solicitudImatges, name='solicitudimatges'),
    path('area_edicio/<int:pk>/maquetacio/solicitud', views.solicitudImatges, name='solicitudmaquetaciollibre'),
    path('area_dismaq/<int:pk>', views.areaDisssenyiMaquetacio, name='areadismaq'),
]
