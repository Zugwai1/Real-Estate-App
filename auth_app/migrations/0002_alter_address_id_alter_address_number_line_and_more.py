# Generated by Django 4.0.5 on 2022-07-07 12:54

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='id',
            field=models.UUIDField(default=uuid.UUID('15b77a50-4440-443c-976e-5a0f68c5dfc3'), primary_key=True, serialize=False, verbose_name='Models id'),
        ),
        migrations.AlterField(
            model_name='address',
            name='number_line',
            field=models.TextField(verbose_name='Address Number Line'),
        ),
        migrations.AlterField(
            model_name='address',
            name='postal_code',
            field=models.TextField(verbose_name='Postal code'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.UUID('15b77a50-4440-443c-976e-5a0f68c5dfc3'), primary_key=True, serialize=False, verbose_name='Models id'),
        ),
    ]
