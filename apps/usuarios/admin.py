from django.contrib import admin

from apps.usuarios.models import CategoriaModel, PostModel

admin.site.register(CategoriaModel)
admin.site.register(PostModel)
