from django import forms
from django.core import validators
from django.contrib.auth.models import User


def name_not_exists(value):
    try:
        User.objects.get(username=value)
        raise forms.ValidationError('User with that username already exists.')
    except User.DoesNotExist:
        pass


def email_not_exists(value):
    try:
        User.objects.get(email=value)
        raise forms.ValidationError('That email is already registered.')
    except User.DoesNotExist:
        pass


class RegisterForm(forms.Form):
    username = forms.CharField(
        validators=[validators.MinLengthValidator(2), name_not_exists]
    )
    email = forms.EmailField(validators=[email_not_exists])
    password = forms.CharField(
        widget=forms.PasswordInput(),
        validators=[validators.MinLengthValidator(6)]
    )
    password2 = forms.CharField(
        label="Please verify your password",
        widget=forms.PasswordInput(),
    )
    pooh = forms.CharField(
        required=False,
        widget=forms.HiddenInput(),
        label='Leave empty.',
        validators=[validators.MaxLengthValidator(0)]
    )

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get('password')
        verify = cleaned_data.get('password2')

        if password != verify:
            raise forms.ValidationError('Passwords must match')


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())
