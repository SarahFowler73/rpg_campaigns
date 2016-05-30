from django.shortcuts import render

from . import forms

def index(request):
    return render(request, 'index.html')

def register(request):
    form = forms.RegisterForm()
    return render(request, 'register.html', {'form': form})
