# Generated by Django 3.1.1 on 2021-04-03 03:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='account_image',
        ),
    ]
