# Generated by Django 4.2.1 on 2023-05-27 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0003_remove_song_uploaded_by_alter_song_artist_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='artist',
            field=models.CharField(max_length=200),
        ),
    ]
