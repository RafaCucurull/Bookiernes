from django.urls import path

from bookapp import views

urlpatterns = [
    path('', views.homePage, name="home"),
    path('escriptori', views.Escriptori, name="escriptori"),
    path('afegirllibre', views.afegirLlibre, name="afegirllibre"),
    path('area_edicio/<int:pk>', views.areaedicio, name='areaedicio'),
    path('area_escriptor/<int:pk>', views.areaescriptor, name='areaescriptor'),
    path('area_escriptor/<int:pk>/enviarnovaversio', views.enviarnovaversio, name='enviarnovaversio'),
    path('area_edicio/<int:pk>/canviardocument', views.canviardocument, name='canviardocument'),
    path('notificacions', views.notificacions, name='notificacions'),
    path('area_edicio/<int:pk>/commentseditor', views.commentseditor, name='commentseditor'),
    path('area_escriptor/<int:pk>/comments', views.comments, name='comments'),
]
