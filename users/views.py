from django.shortcuts import render
from django.views.generic import View, ListView
from django.contrib.auth import models


class UsersView(ListView):
    queryset = models.User.objects.all()
    template_name = 'users.html'
