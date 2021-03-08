from django.forms import ModelForm

from apps.usuarios.models import PostModel


class PostForms(ModelForm):

    class Meta:
        model = PostModel
        fields = ('categoria','titulo','contenido','imagen')