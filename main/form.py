from django import forms
from .models import About_us, Social_link


class AboutusForm(forms.ModelForm):
    class Meta:
        model = About_us
        fields = ['title', 'descretion']



class Sociallink(forms.ModelForm):
    class Meta:
        model = Social_link
        fields = ['facebook', 'twitter', 'instagram', 'linkedin']