from django.contrib import admin

from . import models

admin.site.register(models.Character)
admin.site.register(models.Game)
admin.site.register(models.GameCharacter)
admin.site.register(models.GameSession)
admin.site.register(models.UserGame)
