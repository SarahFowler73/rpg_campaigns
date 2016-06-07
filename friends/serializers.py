from rest_framework import serializers

from . import models


class UserUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserUser
