# Generated by Django 4.1.6 on 2023-02-12 11:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='EmailModel',
            new_name='Email',
        ),
    ]