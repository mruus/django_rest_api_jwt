from django.db import models

# Create your models here.
class AuthUsers(models.Model):
    name = models.CharField(max_length=500)
    email = models.EmailField(max_length=500 , unique=True)
    password = models.CharField(max_length=500)

    def __str__(self):
        self.name