from django.urls import path

from apps.login.views import RegistroView, LogoutView, AccederView

app_name = 'login'

urlpatterns = [
    path('registro/', RegistroView.as_view(), name='registro'),
    path('login/', AccederView.as_view(), name='login'),
    path('salir/', LogoutView.as_view(next_page='login:login'), name='salir'),

]
