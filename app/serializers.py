from rest_framework import serializers
from .models import AuthUser

class AuthUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuthUser
        fields = ['id', 'password', 'username', 'first_name', 'last_name', 'email', 'is_active']