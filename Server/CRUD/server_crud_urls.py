from django.urls import path
from . import views

urlpatterns = [
    path('crud_noid' , views.CRUD_NOID , name="CRUD_NOID"),
    path('crud_id/<int:pk>' , views.CRUD_ID , name="CRUD_ID"),
]