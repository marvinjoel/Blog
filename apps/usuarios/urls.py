from django.contrib import admin
from django.urls import path, include

from apps.usuarios.views import InicioView


app_name = 'inicio'

urlpatterns = [
    path('', InicioView.as_view(), name='inicio'),
]
