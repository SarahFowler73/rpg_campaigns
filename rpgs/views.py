from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User

from . import forms

def index(request):
    return render(request, 'index.html')

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
                "Registration complete!"
            )
            return HttpResponseRedirect(reverse('index'))
    return render(request, 'register.html', {'form': form})
