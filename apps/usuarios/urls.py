from django.contrib import admin
from django.urls import path, include


from apps.usuarios.views import InicioView, Create_post, eliminar_post

app_name = 'inicio'

urlpatterns = [
    path('', InicioView.as_view(), name='inicio'),
    path('post/crear/', Create_post.as_view(), name='crear'),
    path('post/eliminar/<int:post_id>/', eliminar_post, name='eliminar'),
]
