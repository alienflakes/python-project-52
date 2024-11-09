from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.utils.translation import gettext_lazy as _


class LoginView(SuccessMessageMixin, LoginView):

    success_message = _('You are logged in.')


class LogoutView(LogoutView):

    def post(self, request, *args, **kwargs):
        messages.info(request, _('You are logged out.'))
        return super().post(request, *args, **kwargs)
