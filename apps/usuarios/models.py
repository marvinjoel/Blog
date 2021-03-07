import os

from django.contrib.auth.models import User
from django.db import models


class CategoriaModel(models.Model):
    nombre = models.CharField(max_length=100, null=False, unique=True, verbose_name='Nombre')

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name='Categoria'
        verbose_name_plural = 'Categorias'
        ordering = ['id']


class PostModel(models.Model):
    autor = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    categoria = models.ForeignKey(CategoriaModel, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100, unique=True, null=True, verbose_name='Título')
    contenido = models.TextField(null=True, verbose_name='Contenido del post')
    imagen = models.ImageField(upload_to='post/%Y/%m/%d', null=True, blank=True, verbose_name='Imagen del post')
    fecha_alta = models.DateTimeField(auto_now_add=True, verbose_name='Fecha alta')
    fecha_actualizacion = models.DateTimeField(verbose_name='Fecha actualización', auto_now_add=True)


    # eliminacion de archivos que se guardan en la carpeta

    def delete(self, *args,**kwargs):
        if os.path.isfile(self.imagen.path):
            os.remove(self.imagen.path)
        super(PostModel, self).delete(*args,**kwargs)



    def __str__(self):
        return self.titulo

    class Meta:
        verbose_name='Post'
        verbose_name_plural = 'Posts'
        ordering = ['id']
