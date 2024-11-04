from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.contrib.auth import models, forms
from django.urls import reverse_lazy


class UsersView(ListView):
    queryset = models.User.objects.all()
    template_name = 'users.html'


class SignUpView(CreateView):
    form_class = forms.UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
