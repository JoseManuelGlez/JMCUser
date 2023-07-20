import jwt
from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from ..models.models import CreateUserModel
from ..serializers import UpdatePasswordSerializer

class UpdatePasswordView(APIView):
    print("hola mundo")

    def put(self, request, user_id):
        try:
            user = CreateUserModel.objects.get(id=user_id)
        except CreateUserModel.DoesNotExist:
            return Response({'success': False, 'message': 'Usuario no encontrado'}, status=404)

        token = request.data.get('token')  # Obtener el token del cuerpo de la solicitud
        print("imprimiendo token")
        print(token)

        try:
            # Verificar y decodificar el token JWT
            decoded_token = jwt.decode(token, 'tu_clave_secreta_aqui', algorithms=['HS256'])
            user_id_from_token = decoded_token.get('id')

            # Verificar si el usuario autenticado es el propietario de la cuenta
            if user.id != user_id_from_token:
                return Response({'success': False, 'message': 'No tienes permiso para actualizar la contraseña'}, status=403)

            password = request.data.get('password')
            if password is not None:
                user.update_password(password)
                return Response({'success': True, 'message': 'Contraseña actualizada'}, status=200)
            return Response({'success': False, 'message': 'Error al actualizar contraseña', 'errors': UpdatePasswordSerializer.errors}, status=400)
        except jwt.ExpiredSignatureError:
            return Response({'success': False, 'message': 'Token expirado'}, status=401)
        except jwt.InvalidTokenError:
            return Response({'success': False, 'message': 'Token inválido'}, status=401)
