from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic




class SignUp(generic.CreateView):
    form_class = UserCreationForm
    # use reverse_lazy to redirect the user to the login page upon successful registration.
    success_url = reverse_lazy('login')

    template_name = 'signup.html'
