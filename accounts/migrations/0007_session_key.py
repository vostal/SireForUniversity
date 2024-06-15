# Generated by Django 4.2.2 on 2023-07-23 11:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0006_user_confirmed'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='key',
            field=models.CharField(default=django.utils.timezone.now, max_length=4096),
            preserve_default=False,
        ),
    ]
