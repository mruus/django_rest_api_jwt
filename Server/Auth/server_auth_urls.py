from django.urls import path
from . import views

urlpatterns = [
    path('AuthLogin', views.AuthLogin, name="AuthLogin"),
    path('AuthRegister', views.AuthRegister, name="AuthRegister"),
]
