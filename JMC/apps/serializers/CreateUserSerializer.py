from rest_framework import serializers
from ..models.models import CreateUserModel

class CreateUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CreateUserModel
        fields = ['username', 'email', 'password']
