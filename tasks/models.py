from django.db import models
from django.contrib.auth.models import User
from statuses.models import Status


class Task(models.Model):

    name = models.CharField(max_length=150)
    description = models.TextField(default='', null=True, blank=True)
    status = models.ForeignKey(Status, on_delete=models.PROTECT)
    creator = models.ForeignKey(User, on_delete=models.PROTECT,
                                related_name='creator')
    doer = models.ForeignKey(User, on_delete=models.PROTECT,
                             related_name='doer', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
