from django.shortcuts import render
from django.db.models import Q
from rest_framework import viewsets

from . import models
from . import serializers


class UserUserView(viewsets.ModelViewSet):
    serializer_class = serializers.UserUserSerializer
    def get_queryset(self):
        return models.UserUser.objects.filter(
            Q(to_user_id=self.request.user.id) |
            Q(from_user_id=self.request.user.id)
        )
