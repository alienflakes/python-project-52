from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.db.models import ProtectedError
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _
from django.views.generic import (ListView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from .models import Status
from django.contrib.auth.mixins import LoginRequiredMixin


SUCCESS_URL = reverse_lazy('st_list')


class FlashedLoginRequiredMixin(LoginRequiredMixin):

    def handle_no_permission(self):
        messages.error(self.request, _("You are not authorized! Please log in."))
        return super().handle_no_permission()


class StatusListView(FlashedLoginRequiredMixin,
                     ListView):

    model = Status
    template_name_suffix = '_list'


class StatusCreateView(FlashedLoginRequiredMixin,
                       SuccessMessageMixin, CreateView):

    model = Status
    fields = ['name']
    template_name_suffix = '_create'
    success_url = SUCCESS_URL
    success_message = _('Status created successfully')


class StatusUpdateView(FlashedLoginRequiredMixin,
                       SuccessMessageMixin, UpdateView):

    model = Status
    fields = ['name']
    template_name_suffix = '_update'
    success_url = SUCCESS_URL
    success_message = _('Status updated successfully')


class StatusDeleteView(FlashedLoginRequiredMixin,
                       SuccessMessageMixin, DeleteView):

    model = Status
    template_name_suffix = '_delete'
    success_url = SUCCESS_URL
    success_message = _('Status deleted successfully')

    def post(self, request, *args, **kwargs):
        obj = self.get_object()
        try:
            obj.delete()
        except ProtectedError:
            messages.error(self.request, _("Status can't be deleted as long as it's in use"))
        return redirect(self.success_url)
