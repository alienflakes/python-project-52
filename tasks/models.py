from django.db import models
from django.contrib.auth.models import User
from statuses.models import Status
from django.utils.translation import gettext_lazy as _


class Task(models.Model):

    name = models.CharField(max_length=150, verbose_name=_('Name'))
    description = models.TextField(default='', null=True, blank=True,
                                   verbose_name=_('Description'))
    status = models.ForeignKey(Status, on_delete=models.PROTECT,
                               verbose_name=_('Status'))
    creator = models.ForeignKey(User, on_delete=models.PROTECT,
                                related_name='creator',
                                verbose_name=_('Creator'))
    doer = models.ForeignKey(User, on_delete=models.PROTECT,
                             null=True, blank=True,
                             related_name='doer',
                             verbose_name=_('Doer'))
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
