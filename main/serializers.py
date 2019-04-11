from rest_framework import serializers
from .models import User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    first_name = serializers.CharField(max_length=45)
    last_name = serializers.CharField(max_length=45)
    email = serializers.CharField(max_length=45)
    password = serializers.CharField(max_length=45)
    user_type = serializers.CharField(max_length=45)
    last_login = serializers.DateField()
    created = serializers.DateField()
    updated = serializers.DateField()
