# Generated by Django 4.0.2 on 2022-03-13 05:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0005_alter_user_user_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='role_id',
        ),
    ]