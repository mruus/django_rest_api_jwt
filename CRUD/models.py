from django.db import models

# Create your models here.


class Accounts(models.Model):
    Name = models.CharField(max_length=500)
    Email = models.EmailField(max_length=500)
    Phone = models.CharField(max_length=500)
    Username = models.CharField(max_length=500)
    Password = models.CharField(max_length=500)

    def __str__(self):
        self.Name
