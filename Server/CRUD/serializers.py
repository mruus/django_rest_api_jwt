from rest_framework.serializers import ModelSerializer
from CRUD import models


class AccountSerializer(ModelSerializer):
    class Meta:
        model = models.Accounts
        fields = '__all__'