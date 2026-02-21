from django import forms
from .models import Mediacontent

class MediaContentForm(forms.ModelForm):
    class Meta:
        model = Mediacontent
        fields = ['title', 'description', 'image', 'video', 'audio']