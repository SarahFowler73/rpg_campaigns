from django.contrib import admin

from . import models
from rpgs.models import User

admin.site.register(models.Character)
admin.site.register(models.Game)
admin.site.register(models.GameCharacter)
admin.site.register(models.GameSession)
admin.site.register(models.UserGame)
admin.site.register(models.UserUser)
