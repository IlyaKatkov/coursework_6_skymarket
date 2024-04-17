from rest_framework import serializers
from djoser.serializers import UserCreateSerializer as BaseUserRegistrationSerializer

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserRegistrationSerializer(BaseUserRegistrationSerializer):
    class Meta(BaseUserRegistrationSerializer.Meta):
        fields = ('url', 'id', 'email', 'first_name', 'last_name', 'phone', 'password', )
