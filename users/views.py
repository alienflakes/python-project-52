from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.db.models import ProtectedError
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _
from django.views.generic import (ListView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from django.contrib.auth.models import User
from django.contrib.auth.mixins import UserPassesTestMixin
from . import forms


class UsersView(ListView):

    model = User
    template_name = 'users/user_list.html'


class UserPermissionMixin(UserPassesTestMixin):

    def test_func(self):
        return self.request.user.id == self.kwargs['pk']

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            messages.error(self.request,
                           _("You can't edit other user's profile."))
            return redirect(reverse_lazy('users'))
        else:
            messages.warning(self.request,
                             _("You are not authorized! Please log in."))
            return redirect(reverse_lazy('login'))


class SignUpView(SuccessMessageMixin, CreateView):

    form_class = forms.CustomUserCreationForm
    template_name = 'users/user_create.html'
    success_url = reverse_lazy('login')
    success_message = _('User created successfully')


class CustomUpdateView(UserPermissionMixin,
                       SuccessMessageMixin,
                       UpdateView):

    model = User
    form_class = forms.CustomUserChangeForm
    template_name = 'users/user_update.html'
    success_url = reverse_lazy('users')
    success_message = _('User updated successfully')


class DeleteView(UserPermissionMixin,
                 SuccessMessageMixin,
                 DeleteView):

    model = User
    template_name = 'users/user_delete.html'
    success_url = reverse_lazy('users')
    success_message = _('User deleted successfully')

    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        try:
            obj.delete()
        except ProtectedError:
            messages.error(self.request, _("User can't be deleted as long as they're involved in tasks"))
        return redirect(self.success_url)
