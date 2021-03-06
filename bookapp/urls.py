from django.contrib.auth.views import LoginView
from django.urls import path

from bookapp import views

urlpatterns = [
    path('', views.homePage, name="home"),
    path('login_lector/', LoginView.as_view(template_name='registration/login_lector.html'), name='login_lector'),
    path('escriptori', views.Escriptori, name="escriptori"),
    path('cataleg', views.cataleg, name="cataleg"),
    path('cataleg/<int:pk>', views.idiomes, name="idioma"),
    path('cataleg/<int:pk>/original', views.idiomes, name="pdfsencer"),
    path('cataleg/<int:pk>/original', views.idiomes, name="pdfretallat"),
    path('cataleg/<int:pk>/es', views.idiomes, name="es"),
    path('cataleg/<int:pk>/es', views.idiomes, name="es_retall"),
    path('cataleg/<int:pk>/en', views.idiomes, name="en"),
    path('cataleg/<int:pk>/en', views.idiomes, name="en_retall"),
    path('cataleg/<int:pk>/pt', views.idiomes, name="pt"),
    path('cataleg/<int:pk>/pt', views.idiomes, name="pt_retall"),
    path('cataleg/<int:pk>/zh', views.idiomes, name="zh"),
    path('cataleg/<int:pk>/zh', views.idiomes, name="zh_retall"),
    path('afegirllibre', views.afegirLlibre, name="afegirllibre"),
    path('area_edicio/<int:pk>', views.areaedicio, name='areaedicio'),
    path('area_edicio/enviarmissatge', views.enviarmissatge, name='enviarmissatge'),
    path('veuremissatge', views.veuremissatge, name='veuremissatge'),
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
    path('area_edicio/<int:pk>/dirbateriaimatges/galeriaimatges/eliminarimatge/<int:pkimatge>', views.eliminarimatge, name='eliminarimatge'),
    path('area_edicio/<int:pk>/dirmaquetacions/galeriamaquetacions/descargar/<int:pkimatge>', views.download_image, name='descargarimatge'),
    path('area_edicio/<int:pk>/dirmaquetacions/solicitudmaquetacio', views.solicitudmaquetacio, name='solicitudmaquetacio'),
    path('area_edicio/<int:pk>/solicitudpublicacio', views.solicitudpublicacio, name='solicitudpublicacio'),
    path('area_edicio/<int:pk>/dirtraduccions', views.dirtraduccions, name='dirtraduccions'),
    path('area_edicio/<int:pk>/dirtraduccions/solicitudtraduccio', views.solicitudTraduccio, name='solicitudtraduccio'),
    path('area_edicio/<int:pk>/dirtraduccions/galeriatraduccions', views.galeriaTraduccions, name='galeriatraduccions'),
    path('area_escriptor/<int:pk>/comments', views.comments, name='comments'),
    path('area_it/<int:pk>/publicarllibre', views.publicarllibre, name='publicarllibre'),
    path('area_dismaq/<int:pk>', views.areaDisssenyiMaquetacio, name='areadismaq'),
    path('area_dismaq/<int:pk>/solicitudsimg/enviarbat/<int:pksol>', views.enviarbat, name='enviarbat'),
    path('area_dismaq/<int:pk>/solicitudsimg', views.veuresolicitudsImatge, name='solicitudsimg'),
    path('area_dismaq/<int:pk>/solicitudsmaq', views.veuresolicitudsMaquetacio, name='solicitudsmaq'),
    path('area_dismaq/<int:pk>/solicitudsmaq/enviarmaq/<int:pksol>', views.enviarMaquetacio, name='enviarmaq'),
    path('notificacions/eliminarnotificacio/<int:pknotificacio>', views.eliminarnotificacio,
         name='eliminarnotificacio'),
    path('veuremissatge/eliminarmissatge/<int:pkmissatge>', views.eliminarmissatge,
         name='eliminarmissatge'),
    path('perfil/<int:pkperfil>', views.perfil,
         name='perfil'),
    path('perfil/<int:pkperfil>/configuracio', views.configuracio,
         name='configuracio'),
]
