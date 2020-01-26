from django .forms import forms
from pages.models import usercreation
from django .forms import ModelForm
from django import forms
class userForm(forms.Form):
    first_name=forms.CharField(max_length=64,
                               widget=forms.TextInput(attrs={
                                   'class':'form-control'
                               }))

    last_name = forms.CharField(max_length=64,
                                 widget=forms.TextInput(attrs={
                                     'class': 'form-control'
                                 }))
    email = forms.EmailInput(
                                 widget=forms.EmailInput(attrs={
                                     'class': 'form-control'
                                 }))
        # model=usercreation
        # fields=['first_name','last_name','email','password1','password2','checkbox']