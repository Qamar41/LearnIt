from django import forms
from django.forms import ModelForm
from .models import contact,Comment

class contactform(ModelForm):
    class Meta:
        model=contact
        fields=['name','email','subject','message']


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')