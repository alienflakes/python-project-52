from django.urls import reverse_lazy
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import gettext_lazy as _
from django.views.generic import (ListView,
                                  DetailView,
                                  CreateView,
                                  UpdateView,
                                  DeleteView)
from .models import Task
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


SUCCESS_URL = reverse_lazy('task_list')


class FlashedLoginRequiredMixin(LoginRequiredMixin):

    def handle_no_permission(self):
        messages.error(self.request, _("You are not authorized! Please log in."))
        return super().handle_no_permission()


class TaskListView(FlashedLoginRequiredMixin,
                   ListView):

    model = Task
    template_name_suffix = '_list'


class TaskView(FlashedLoginRequiredMixin,
               DetailView):

    model = Task
    template_name_suffix = '_view'


class TaskCreateView(FlashedLoginRequiredMixin,
                     SuccessMessageMixin, CreateView):

    model = Task
    fields = ['name', 'description', 'status', 'doer', 'labels']
    template_name_suffix = '_create'
    success_url = SUCCESS_URL
    success_message = _('Task created successfully')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class TaskUpdateView(FlashedLoginRequiredMixin,
                     SuccessMessageMixin, UpdateView):

    model = Task
    fields = ['name', 'description', 'status', 'doer', 'labels']
    template_name_suffix = '_update'
    success_url = SUCCESS_URL
    success_message = _('Task updated successfully')


class TaskDeleteView(FlashedLoginRequiredMixin,
                     UserPassesTestMixin,
                     SuccessMessageMixin, DeleteView):

    def test_func(self):
        return self.request.user == self.get_object().creator

    def handle_no_permission(self):
        messages.error(self.request, _("Task can be deleted only by it's creator"))
        return redirect(SUCCESS_URL)

    model = Task
    template_name_suffix = '_delete'
    success_url = SUCCESS_URL
    success_message = _('Task deleted successfully')
