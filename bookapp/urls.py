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
    path('area_edicio/<int:pk>/dirbateriaimatges/solicitudimatges', views.solicitudImatges, name='solicitudimatges'),
    path('area_edicio/<int:pk>/dirbateriaimatges/galeriaimatges', views.galeriaImatges, name='galeriaimatges'),
    path('area_edicio/<int:pk>/dirmaquetacions', views.dirmaquetacions, name='dirmaquetacions'),
    path('area_edicio/<int:pk>/dirmaquetacions/galeriamaquetacions', views.galeriaMaquetacions, name='galeriamaquetacions'),
    path('area_edicio/<int:pk>/dirmaquetacions/galeriamaquetacions/eliminarimatge/<int:pkimatge>', views.eliminarimatge, name='eliminarimatge'),
    path('area_edicio/<int:pk>/dirmaquetacions/galeriamaquetacions/descargar/<int:pkimatge>', views.download_image, name='descargarimatge'),
    path('area_edicio/<int:pk>/dirmaquetacions/solicitudmaquetacio', views.solicitudmaquetacio, name='solicitudmaquetacio'),
    path('area_edicio/<int:pk>/solicitudpublicacio', views.solicitudpublicacio, name='solicitudpublicacio'),
    path('area_edicio/<int:pk>/dirtraduccions', views.dirtraduccions, name='dirtraduccions'),
    path('area_edicio/<int:pk>/dirtraduccions/solicitudtraduccio', views.solicitudTraduccio, name='solicitudtraduccio'),
    path('area_escriptor/<int:pk>/comments', views.comments, name='comments'),
    path('area_it/<int:pk>/publicarllibre', views.publicarllibre, name='publicarllibre'),
    path('area_dismaq/<int:pk>', views.areaDisssenyiMaquetacio, name='areadismaq'),
    path('area_dismaq/<int:pk>/solicitudsimg/enviarbat', views.enviarbat, name='enviarbat'),
    path('area_dismaq/<int:pk>/solicitudsimg', views.veuresolicitudsImatge, name='solicitudsimg'),
    path('area_dismaq/<int:pk>/solicitudsmaq', views.veuresolicitudsMaquetacio, name='solicitudsmaq'),
    path('area_dismaq/<int:pk>/solicitudsmaq/enviarmaq', views.enviarMaquetacio, name='enviarmaq'),

]
