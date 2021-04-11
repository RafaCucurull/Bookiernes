from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.homepage, name='home'),
    path('area_edicio', views.areaedicio, name='areaedicio'),
    path('escriptorieditor', views.escriptorieditor, name='escriptorieditor'),
    path('escriptoriescriptor', views.escriptoriescriptor, name='escriptoriescriptor')
]