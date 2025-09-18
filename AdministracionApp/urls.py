from .views import paginaIndex, ventas, iniciarsesion, cerrarSesion
from django.urls import path

urlpatterns = [
    path('', paginaIndex, name='inicio'),
    path('iniciarsesion', iniciarsesion, name='iniciarsesion'),
    path('ventas', ventas, name='ventas'),
    path('cerrarsesion', cerrarSesion, name='cerrarsesion'),
]
