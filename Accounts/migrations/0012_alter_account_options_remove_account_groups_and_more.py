# Generated by Django 4.1.4 on 2023-01-13 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Accounts', '0011_alter_account_options_account_groups_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={},
        ),
        migrations.RemoveField(
            model_name='account',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='account',
            name='is_superuser',
        ),
        migrations.RemoveField(
            model_name='account',
            name='last_login',
        ),
        migrations.RemoveField(
            model_name='account',
            name='user_permissions',
        ),
    ]
