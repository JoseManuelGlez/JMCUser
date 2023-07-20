from django.contrib import admin
from django.urls import path
from apps.views.CreateUserView import CreateUserView
from apps.views.LoginUserView import LoginUserView
from apps.views.UpdatePasswordView import UpdatePasswordView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', CreateUserView.as_view(), name = 'create'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('user/<int:user_id>/', UpdatePasswordView.as_view(), name='update-password'),
]
