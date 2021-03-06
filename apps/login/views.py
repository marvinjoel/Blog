from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LogoutView, LoginView
from django.shortcuts import render, redirect
from django.views import View




class RegistroView(View):

    #Vista del formulario de registro de usuarios
    def get(self, request):
        template = 'registro.html'
        form = UserCreationForm
        return render(request, template, {'form':form})

    #registro de usurios
    def post(self, request):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            usuario = form.save()
            nombre_usuario = form.cleaned_data.get('username')
            messages.success(request, f'Bienvenid@ a la plataforma {nombre_usuario}')
            login(request, usuario)
            return redirect('inicio:inicio')

        else:
            for msg in form.error_messages:
                messages.error(request, form.error_messages[msg])
            return render(request,'registro.html', {'form':form} )



class AccederView(LoginView):
    template_name = 'login.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

