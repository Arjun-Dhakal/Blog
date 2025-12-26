from django import forms
from main.models import Category, Blog, About_us, Social_link




class Categoryform(forms.ModelForm):
    class Meta:
        model=Category
        fields= '__all__'

class Blogform(forms.ModelForm):
    class Meta:
        model=Blog
        fields= '__all__'

class AboutusForm(forms.ModelForm):
    class Meta:
        model = About_us
        fields = ['title', 'descretion']


class SociallinkForm(forms.ModelForm):
    class Meta:
        model = Social_link
        fields = ['facebook', 'twitter', 'instagram', 'linkedin']