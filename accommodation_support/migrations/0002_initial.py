# Generated by Django 4.0.5 on 2022-06-11 14:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth_app', '0001_initial'),
        ('accommodation_support', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='address',
            field=models.OneToOneField(on_delete=django.db.models.deletion.RESTRICT, to='auth_app.address'),
        ),
        migrations.AddField(
            model_name='property',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
