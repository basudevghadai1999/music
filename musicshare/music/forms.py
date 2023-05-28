from django.forms import ModelForm
from .models import Song
from .models import Credential

class CredentialForm(ModelForm):
    class Meta:
        model = Credential
        fields = "__all__"

class SongForm(ModelForm):
    class Meta:
        model = Song
        fields = "__all__"