# Generated by Django 4.2.1 on 2023-05-27 11:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('music', '0004_alter_song_artist'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='authorized_emails',
            field=models.TextField(blank=True),
        ),
        migrations.AddField(
            model_name='song',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='song',
            name='visibility',
            field=models.CharField(choices=[('public', 'Public'), ('private', 'Private'), ('protected', 'Protected')], default='public', max_length=10),
        ),
    ]