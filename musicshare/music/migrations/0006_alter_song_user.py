# Generated by Django 4.2.1 on 2023-05-27 11:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('music', '0005_song_authorized_emails_song_user_song_visibility'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
