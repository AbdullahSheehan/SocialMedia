from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class CreateNewUser(UserCreationForm):
    email = forms.EmailField(label="", required=True, widget=forms.TextInput(attrs={
        'placeholder':'Your Email',
        'autofocus':True
    }))
    username = forms.CharField(required=True, label="", widget=forms.TextInput(attrs={
        'placeholder':'Your Username'
    }))
    password1 = forms.CharField(required=True, label="", widget=forms.PasswordInput(attrs={
        'placeholder':'Password'
    }))
    password2 = forms.CharField(required=True, label="", widget=forms.PasswordInput(attrs={
        'placeholder':'Confirm Password'
    }))
    class Meta:
        model = User
        fields = ('email', 'username', 'password1', 'password2')

class Profile(forms.ModelForm):
    dob = forms.DateField(widget=forms.TextInput(attrs={
        'type' : 'date'
    }))
    class Meta:
        model = UserProfile
        fields = "__all__"
        exclude = ('user', )