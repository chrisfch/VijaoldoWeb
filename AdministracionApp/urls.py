from .views import inicio
from django.urls import path

urlpatterns = [
    path('', inicio, name='inicio'),
]
