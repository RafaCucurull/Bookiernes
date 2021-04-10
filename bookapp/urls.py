from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('area_edicio', views.areaedicio, name='areaedicio')
]