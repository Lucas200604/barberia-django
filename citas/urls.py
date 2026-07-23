from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='inicio'),
    path('reservar/', views.reservar, name='reservar'),
    path("exito/", views.exito, name='exito'),
    path("contacto/", views.contacto, name='contacto'),
    path("servicios/", views.servicios, name='servicios'),
    path("barberos/", views.mostrar_barberos, name='barberos'),
]
