# Generated by Django 4.2.1 on 2023-05-27 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0008_credential'),
    ]

    operations = [
        migrations.RenameField(
            model_name='credential',
            old_name='artist',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='credential',
            old_name='title',
            new_name='psw',
        ),
    ]