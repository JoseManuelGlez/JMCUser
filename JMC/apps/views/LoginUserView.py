from django.contrib.auth import authenticate
import json
import jwt
from django.conf import settings
from django.http import JsonResponse
from django.views import View
from datetime import datetime, timedelta
from django.conf import settings

class LoginUserView(View):
    def post(self, request):
        body = json.loads(request.body)
        email = body.get('email')
        password = body.get('password')

        user = authenticate(request=request, email=email, password=password, backend='apps.views.MyCustomAuthBackend')

        if user is not None:
            token = self.generate_token(user)

            print(token)
            return JsonResponse({'success': True, 'message': 'Inicio de sesión exitoso', 'token': token})
        else:
            return JsonResponse({'success': False, 'message': 'Credenciales incorrectas'})

    def generate_token(self, user):
        print(user)
        print(user.id)
        payload = {
            'id': user.id,
            'exp': datetime.utcnow() + timedelta(hours=3)  # Expire in 3 hours
        }

        token = jwt.encode(payload, 'tu_clave_secreta_aqui', algorithm = 'HS256')

        return token