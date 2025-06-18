from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    emails = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'emails', 'password1', 'password2']