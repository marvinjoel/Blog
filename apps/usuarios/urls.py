from django.urls import path

from apps.usuarios.views import InicioView

urlpatterns = [
    path('', InicioView.as_view(), name='inicio'),
]