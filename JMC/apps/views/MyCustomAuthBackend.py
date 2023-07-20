from django.contrib.auth.backends import BaseBackend
from ..models.models import CreateUserModel

class MyCustomAuthBackend(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = CreateUserModel.objects.get(email=email)
            if user.check_password(password):
                return user
        except CreateUserModel.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return CreateUserModel.objects.get(pk=user_id)
        except CreateUserModel.DoesNotExist:
            return None