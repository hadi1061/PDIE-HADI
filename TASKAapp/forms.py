from django import forms
from .models import CHILD

class childForm(forms.ModelForm):
    class Meta:
        model = CHILD
        fields = [
            'mykadnum',
            'ICNUM',
            'username',
            'STICNUM',
            'cname',
            'age',
            'salinanmykid',
            'salinanICparent',
            'salinansuratberanak',
            'salinanimunisasianak',
            'interfacebukukesihatan'
        ]
