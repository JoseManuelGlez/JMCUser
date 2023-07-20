from rest_framework import serializers
from ..models.models import CreateUserModel

class LoginUserSerealizer(serializers.ModelSerializer):
    class Meta:
        model = CreateUserModel
        fields = ['username', 'password']
