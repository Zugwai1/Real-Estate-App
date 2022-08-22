# Generated by Django 4.0.5 on 2022-08-03 02:05

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0002_alter_address_id_alter_address_number_line_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='Models id'),
        ),
        migrations.AlterField(
            model_name='user',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, verbose_name='Models id'),
        ),
    ]