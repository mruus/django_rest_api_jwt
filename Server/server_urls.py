from django.urls import path, include


urlpatterns = [
    path('Auth/', include('Server.Auth.server_auth_urls')),
    path('CRUD/', include('Server.CRUD.server_crud_urls'))
]
