# Generated by Django 4.2.2 on 2023-06-29 23:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='createusermodel',
            old_name='name',
            new_name='username',
        ),
    ]
