from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.views import View
from django.views.generic import TemplateView


class InicioView(TemplateView):
    template_name = 'inicio.html'
