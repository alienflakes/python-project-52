from django.views.generic import ListView, CreateView
from django.contrib.auth import models
from django.urls import reverse_lazy
from . import forms


class UsersView(ListView):
    queryset = models.User.objects.all()
    template_name = 'users.html'


class SignUpView(CreateView):
    form_class = forms.CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'
