from __future__ import unicode_literals

from django.db import models
from django.contrib.auth import User


class Character(models.Model):
    character = models.CharField(unique=True, null=False)
    user = models.ForeignKey(User, related_name='characters')
    creation_date = models.DateTimeField(auto_now=True)

    # def get_games(self):
    #     return (
    #         Game.select(Game, GameCharacter)
    #             .join(GameCharacter)
    #             .where(GameCharacter.character == self)
    #     )

    class Meta:
        unique_together = (('character', 'user'),)


class Game(models.Model):
    title = models.CharField(max_length=100, null=False)
    creator = models.ForeignKey(User, related_name='created_games')
    creation_date = models.DateTimeField(auto_now=True)
    last_active_date = models.DateTimeField(null=True)

    # def get_characters(self):
    #     return GameCharacter.select().where(GameCharacter.game == self)
    #
    # def get_players(self):
    #     return (
    #         self.get_characters()
    #             .select(User.username, GameCharacter)
    #             .join(Character)
    #             .join(User)
    #             .group_by(Character.user)
    #     )

    class Meta:
        unique_together = (('title', 'creator'),)
        order_by = ('last_active_date', 'creation_date')


class GameCharacter(models.Model):
    character = models.ForeignKey(
        Character,
        related_name='games')
    game = models.ForeignKey(Game, related_name='characters')
    stat_type = models.CharField(max_length=255)
    stat_value = models.TextField(default='')

    class Meta:
        unique_together = (('game', 'character', 'stat_type'),)


class GameSession(models.Model):
    game = models.ForeignKey(Game, related_name='sessions')
    session_title = models.CharField(default='')
    session_text = models.TextField(default='')
    session_date = models.DateTimeField(null=True)
    entry_created = models.DateTimeField(auto_now=True)
    last_updated = models.DateTimeField(null=True)

    class Meta:
        order_by = ('session_date',)


class UserGame(models.Model):
    user = models.ForeignKey(User, related_name='games')
    game = models.ForeignKey(Game, related_name='users')
    is_owner = models.BooleanField(default=False)
    status = models.CharField(
        choices=('PENDING', 'ACTIVE', 'RETIRED', 'REMOVED')
    )
    join_date = models.DateTimeField(null=True)
    last_active_date = models.DateTimeField(null=True)
    exp_date = models.DateTimeField(null=True)

    class Meta:
        unique_together = (('user', 'game'),)


class UserUser(models.Model):
    from_user = models.ForeignKey(User, related_name="relationships")
    to_user = models.ForeignKey(User, related_name='related_to')

    class Meta:
        unique_together = (('from_user', 'to_user'),)
