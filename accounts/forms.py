from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from .models import Profile


class RegisterForm(UserCreationForm):

    class Meta:
        model = User

        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
        ]


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile

        fields = [
            'phone',
            'location',
        ]


class LoginForm(AuthenticationForm):

    username = forms.CharField()
    password = forms.CharField(
        widget=forms.PasswordInput
    )