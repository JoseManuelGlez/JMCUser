from django.db import models
from django.contrib.auth.models import Permission

class CreateUserModel(models.Model):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField()
    password = models.CharField(max_length=100)
    permissions = models.ManyToManyField(Permission)

    class Meta:
        db_table = 'users'

    def __str__(self):
        return self.email

    def check_password(self, raw_password):
        return self.password == raw_password

    def update_password(self, new_password):
        self.password = new_password
        self.save()

    def check_password(self, raw_password):
        return self.password == raw_password
