from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth

from . import forms

def index(request):
    return render(request, 'index.html')


def login(request):
    form = auth.forms.AuthenticationForm(request)
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST.get('username'),
                                 password=request.POST.get('password'))
        if user is not None:
            auth.login(request, user)
            messages.add_message(request, messages.SUCCESS,
                "You've successfully logged in!")
            return HttpResponseRedirect(reverse('index'))
        else:
            messages.add_message(request, messages.ERROR,
                'Your email or password do not match. Try again.'
            )
    return render(request, 'login.html', {'form': form})


def register(request):
    form = forms.RegisterForm()
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=form.cleaned_data['password']
            )
            messages.add_message(request, messages.SUCCESS,
                "Registration complete!")
            return HttpResponseRedirect(reverse('index'))
    return render(request, 'register.html', {'form': form})


@login_required
def logout(request):
    auth.logout(request)
    messages.add_message(request, messages.SUCCESS,
        "You've been logged out. Come back soon! :'( ")
    return HttpResponseRedirect(reverse('index'))
