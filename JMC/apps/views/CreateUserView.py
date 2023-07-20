from django.contrib.auth.models import Permission
from rest_framework import generics
from ..serializers.CreateUserSerializer import CreateUserSerializer
from django.contrib.auth import authenticate, login

class CreateUserView(generics.CreateAPIView):
    serializer_class = CreateUserSerializer

    def perform_create(self, serializer):
        user = serializer.save()
        
        # Asignar permisos al usuario
        change_createusermodel_permission = Permission.objects.get(codename='change_createusermodel')
        user.permissions.add(change_createusermodel_permission)
        user.save()
