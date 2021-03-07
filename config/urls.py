from django.contrib import admin
from django.urls import path, include

#Configuracion para que se vea la imagen en el administrador
from django.conf.urls.static import static
from config import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.login.urls')),
    path('', include('apps.usuarios.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
