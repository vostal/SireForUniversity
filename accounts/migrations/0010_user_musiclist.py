# Generated by Django 4.2.2 on 2023-07-31 10:40

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_remove_session_login_session_id_session_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='musiclist',
            field=models.CharField(default='', max_length=1024, validators=[django.core.validators.int_list_validator]),
        ),
    ]
