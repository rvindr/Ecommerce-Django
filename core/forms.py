from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2')

    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder':'Your username',
        'class':'px-2 rounded-5'
    }))
    email = forms.CharField(widget=forms.EmailInput(attrs={
        'placeholder':'Your email address',
        'class':'px-2 rounded-5'
    }))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Your password',
        'class':'px-2 rounded-5'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder':'Repeat password',
        'class':'px-2 rounded-5'
    }))
    