from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm

from .forms import CustomUserCreationForm, CustomAuthenticationForm


class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


class MyLoginView(LoginView):
    form_class = CustomAuthenticationForm
    template_name = "registration/login.html"
