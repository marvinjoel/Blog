from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


class InicioView(View):

    def get(self, request):
        template = 'registro.html'
        form = UserCreationForm
        return render(request, template, {'form':form})

    def post(self, request):
        pass

