from django.shortcuts import render
from django.template import loader


def home(request):
    return render(request, 'home.html')


def store(request):
    return render(request, 'store.html')


def login(request):
    return render(request, 'login.html')


def signup(request):
    return render(request, 'signup.html')
