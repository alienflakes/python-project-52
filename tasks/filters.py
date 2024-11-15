import django_filters
from django import forms
from django.utils.translation import gettext as _
from .models import Task
from django.contrib.auth.models import User
from statuses.models import Status
from labels.models import Label


class TaskFilter(django_filters.FilterSet):

    status = django_filters.ModelChoiceFilter(
        queryset=Status.objects.all())

    doer = django_filters.ModelChoiceFilter(
        queryset=User.objects.all())

    labels = django_filters.ModelChoiceFilter(
        label=_('Label'),
        queryset=Label.objects.all())

    def own_tasks_filter(self, queryset, name, value):
        current_user = self.request.user
        if value:
            return queryset.filter(creator=current_user)
        return queryset

    own_task = django_filters.BooleanFilter(
        label=_('My tasks only'),
        method='own_tasks_filter',
        widget=forms.CheckboxInput())

    class Meta:
        model = Task
        fields = ['status', 'doer', 'labels', 'own_task']
