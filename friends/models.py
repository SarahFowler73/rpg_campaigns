from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class UserUser(models.Model):
    from_user = models.ForeignKey(User, related_name="relationships")
    to_user = models.ForeignKey(User, related_name='related_to')

    class Meta:
        unique_together = (('from_user', 'to_user'),)
