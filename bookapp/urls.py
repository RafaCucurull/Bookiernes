from django.urls import path

from bookapp import views
from bookapp.models import Llibre

urlpatterns = [
    path('', views.homePage, name="home"),
    path('escriptori', views.Escriptori, name="escriptori"),
    path('afegirllibre', views.afegirLlibre, name="afegirllibre"),
    path("area_edicio/<int:pk>", views.areaedicio, name='areaedicio'),
    path('area_escriptor/<int:pk>', views.areaescriptor, name='areaescriptor'),
    path('enviarnovaversio', views.enviarnovaversio, name='enviarnovaversio'),
    path('canviardocument', views.canviardocument, name='canviardocument'),
    path('commentseditor', views.commentseditor, name='commentseditor'),
    path('comments', views.comments, name='comments'),
    path('notificacions', views.notificacions, name='notificacions')
]