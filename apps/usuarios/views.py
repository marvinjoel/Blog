from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import TemplateView, DeleteView

from apps.usuarios.forms import PostForms
from apps.usuarios.models import PostModel




class InicioView(View):
    def get(self, request):
        template = 'inicio.html'
        lista_posts = PostModel.objects.all()
        #por defecto tiene Django su paginador
        paginator = Paginator(lista_posts, 3)
        pagina = request.GET.get('page') or 1
        post = paginator.get_page(pagina)
        pagina_actual = int(pagina)
        paginas = range(1, post.paginator.num_pages + 1)
        #fin paginador
        return render(request, template, {'post':post, 'paginas':paginas, 'pagina_actual':pagina_actual})



class Create_post(View):

    def get(self, request):
        template = 'npost.html'
        form = PostForms
        return render(request, template, {'form':form})

    def post(self, request):
        form = PostForms(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor_id = request.user.id
            post.save()
            titulo = form.cleaned_data.get('titulo')
            messages.success(request, f'El post {titulo} se ha creado correctamente')
            return redirect('inicio:inicio')
        else:
            for msg in form.error.messages:
                messages.error(request, form.error.messages[msg])



def eliminar_post(request, post_id):
    try:
        post = PostModel.objects.get(pk=post_id)
    except PostModel.DoesNotExist:
        messages.error(request, 'Elpost que quiere eliminar no existe')
        return redirect('inicio:inicio')

    if  post.autor != request.user:
        messages.error(request, 'No eres el autor de este post')

    post.delete()
    messages.success(request, f'El post {post.titulo} ha sido eliminado')
    return redirect('inicio:inicio')

