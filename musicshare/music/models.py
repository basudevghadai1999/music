from django.db import models
from django.contrib.auth.models import User

class Credential(models.Model):
    email = models.CharField(max_length=200)
    psw = models.CharField(max_length=200)


class Song(models.Model):
    VISIBILITY_CHOICES = (
        ('public', 'Public'),
        ('private', 'Private'),
        ('protected', 'Protected'),
    )

    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    audio_file = models.FileField(upload_to='songs/')
    visibility = models.CharField(max_length=10, choices=VISIBILITY_CHOICES, default='public')
    authorized_emails = models.TextField(blank=True)

    def can_access_song(self, email):
        if self.visibility == 'public':
            return True
        elif self.visibility == 'private':
            return self.user.email == email
        elif self.visibility == 'protected':
            authorized_emails = self.authorized_emails
            return authorized_emails


    def __str__(self):
        return self.title


