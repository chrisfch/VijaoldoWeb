from .views import paginaIndex, ventas, iniciarsesion
from django.urls import path

urlpatterns = [
    path('', paginaIndex, name='inicio'),
    path('iniciarsesion', iniciarsesion, name='iniciarsesion'),
    path('ventas', ventas, name='ventas'),
]
