from django .forms import forms
from pages.models import usercreation, jobform
from django .forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib .auth.models import User
from .models import Personal_info
class userForm(forms.Form):
    first_name=forms.CharField(max_length=64,
                               widget=forms.TextInput(attrs={
                                   'class':'form-control'
                               }))

    last_name = forms.CharField(max_length=64,
                                 widget=forms.TextInput(attrs={
                                     'class': 'form-control'
                                 }))
    # email = forms.EmailInput(widget=forms.EmailInput(attrs={
    #                                  'class': 'form-control'
    #                              }))
    #     # model=usercreation
    #     # fields=['first_name','last_name','email','password1','password2','checkbox']


class ProfileEditForm(UserChangeForm):

    first_name=forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
    }
    ))
    last_name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))

    email = forms.EmailField(widget=forms.TextInput(
        attrs={
            'class': 'form-control',
        }
    ))




    class Meta:


        model=User
        fields = ('email',
                'first_name',
                'last_name',
                  'last_login',
                  'password')



class vacancyForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-control', 'placeholder ': 'Documented Name : '
        }
    ))
    email= forms.EmailField(widget=forms.TextInput(
        attrs={
            'class': 'form-control', 'placeholder ': 'xyz@gmail.com : '
        }
    ))

    message = forms.Textarea( attrs={
        'class':'class',
    })


    class Meta:
        model=jobform

        fields=(
            'name',
            'email',
            'message',
            'image'


        )


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Personal_info
        fields = ('father_name', 'description', 'date_of_birth','Cnic','whattsapp','phone')