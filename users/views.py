from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.contrib import messages
from django.views.generic import (ListView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from django.contrib.auth.models import User
from django.contrib.auth.mixins import UserPassesTestMixin
from . import forms


class UsersView(ListView):
    queryset = User.objects.all()
    template_name = 'users.html'


class SignUpView(CreateView):
    form_class = forms.CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'


class UserPermissionMixin(UserPassesTestMixin):

    def test_func(self):
        return self.request.user.id == self.kwargs['id']

    def handle_no_permission(self):
        if self.request.user.is_authenticated:
            messages.error(self.request,
                           "You can only mess with your own data!!!")
            return redirect(reverse_lazy('index'))
        else:
            messages.warning(self.request,
                             "Log in to mess with profile data!!!")
            return redirect(reverse_lazy('login'))


class CustomUpdateView(UserPermissionMixin, UpdateView):

    model = User
    pk_url_kwarg = 'id'
    form_class = forms.CustomUserChangeForm
    success_url = reverse_lazy('users')
    template_name = 'registration/update.html'

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'YAY updated')
            return redirect(self.success_url)
        else:
            for error in form.errors:
                messages.error(request, form.errors[error])
            return redirect('index')


class DeleteView(UserPermissionMixin, DeleteView):

    model = User
    pk_url_kwarg = 'id'
    template_name = 'registration/delete.html'
    success_url = reverse_lazy('users')

    def post(self, request, *args, **kwargs):
        request.user.delete()
        return redirect(self.success_url)
