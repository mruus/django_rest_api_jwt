from django.urls import path
from . import views

urlpatterns = [
    path('login/' , views.LoginPage , name="Login"),
    path('register/' , views.RegisterPage , name="Register"),
    path('home/' , views.HomePage , name="Home"),
]