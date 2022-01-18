from rest_framework.serializers import ModelSerializer
from Auth.models import AuthUsers


class AuthUsersSerializer(ModelSerializer):
    class Meta:
        model = AuthUsers
        fields = '__all__'