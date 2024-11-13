from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _
from django.views.generic import (ListView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from .models import Label
from django.contrib.auth.mixins import LoginRequiredMixin


SUCCESS_URL = reverse_lazy('label_list')


class FlashedLoginRequiredMixin(LoginRequiredMixin):

    def handle_no_permission(self):
        messages.error(self.request, _("You are not authorized! Please log in."))
        return super().handle_no_permission()


class LabelListView(FlashedLoginRequiredMixin,
                    ListView):

    model = Label
    template_name_suffix = '_list'


class LabelCreateView(FlashedLoginRequiredMixin,
                      SuccessMessageMixin, CreateView):

    model = Label
    fields = ['name']
    template_name_suffix = '_create'
    success_url = SUCCESS_URL
    success_message = _('Label created successfully')


class LabelUpdateView(FlashedLoginRequiredMixin,
                      SuccessMessageMixin, UpdateView):

    model = Label
    fields = ['name']
    template_name_suffix = '_update'
    success_url = SUCCESS_URL
    success_message = _('Label updated successfully')


class LabelDeleteView(FlashedLoginRequiredMixin,
                      SuccessMessageMixin, DeleteView):

    model = Label
    template_name_suffix = '_delete'
    success_url = SUCCESS_URL
    success_message = _('Label deleted successfully')

    def post(self, request, *args, **kwargs):
        label = self.get_object()
        if label.task_set.all():
            messages.error(self.request, _("Label can't be deleted as long as it's in use"))
        else:
            label.delete()
        return redirect(self.success_url)
