# Generated by Django 4.2.2 on 2023-06-30 00:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_rename_name_createusermodel_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createusermodel',
            name='username',
            field=models.CharField(max_length=100, unique=True),
        ),
    ]
