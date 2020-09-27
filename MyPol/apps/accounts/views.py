from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
from django.views.generic import CreateView
from apps.accounts.forms import RegistroForm


class SignUpView(generic.CreateView):
    model = User
    form_class = RegistroForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


