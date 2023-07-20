from rest_framework import serializers
from ..models.models import CreateUserModel

class UpdatePasswordSerializer(serializers.Serializer):
    class Meta:
        model = CreateUserModel
        fields = ['password']
