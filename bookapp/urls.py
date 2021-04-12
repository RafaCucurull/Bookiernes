from django.urls import path

from bookapp import views
from bookapp.models import Llibre

urlpatterns = [
    path('', views.homePage, name="home"),
    path('escriptori', views.Escriptori, name="escriptori"),
    path('afegirllibre', views.afegirLlibre, name="afegirllibre"),
    path("area_edicio/<int:pk>", views.areaedicio, name='areaedicio'),
]