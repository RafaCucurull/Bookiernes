from django.urls import path

from bookapp import views

urlpatterns = [
    path('', views.afegirLlibre, name="afegirllibre"),
]