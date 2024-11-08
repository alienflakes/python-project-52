from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.translation import gettext as _
from django.views.generic import (ListView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from django.contrib.auth.models import User
from django.contrib.auth.mixins import UserPassesTestMixin
from . import forms


class UsersView(ListView):
    model = User
    template_name = 'users.html'


class SignUpView(CreateView):

    form_class = forms.CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class UserPermissionMixin(UserPassesTestMixin):

    def test_func(self):
        return self.request.user.id == self.kwargs['pk']

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            messages.error(self.request,
                           _("You can only mess with your own data!!!"))
            return redirect(reverse_lazy('index'))
        else:
            messages.warning(self.request,
                             _("Log in to mess with profile data!!!"))
            return redirect(reverse_lazy('login'))


class CustomUpdateView(UserPermissionMixin, UpdateView):

    model = User
    form_class = forms.CustomUserChangeForm
    success_url = reverse_lazy('users')
    template_name = 'registration/update.html'


class DeleteView(UserPermissionMixin, DeleteView):

    model = User
    template_name = 'registration/delete.html'
    success_url = reverse_lazy('users')
