# Generated by Django 4.1.4 on 2023-01-12 22:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0007_account_password'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='is_admin',
        ),
    ]
