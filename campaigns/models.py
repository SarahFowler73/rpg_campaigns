from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Character(models.Model):
    character = models.CharField(max_length=255, null=False)
    user = models.ForeignKey(User, related_name='characters')
    creation_date = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True)

    class Meta:
        unique_together = (('character', 'user'),)


class GameCharacter(models.Model):
    character = models.ForeignKey(
        Character,
        related_name='games')
    game = models.ForeignKey('Game', related_name="characters")

    class Meta:
        unique_together = (('game', 'character'),)


class Game(models.Model):
    title = models.CharField(max_length=100, null=False)
    description = models.TextField(blank=True)
    creator = models.ForeignKey(User, related_name='created_games')
    creation_date = models.DateTimeField(auto_now=True)
    last_active_date = models.DateTimeField(null=True)

    class Meta:
        unique_together = (('title', 'creator'),)
        ordering = ['last_active_date', 'creation_date']


class GameCharacterCharacter(models.Model):
    from_character = models.ForeignKey(GameCharacter, related_name="bonds")
    to_character = models.ForeignKey(GameCharacter, related_name="bonded_to")
    bond = models.CharField(max_length=255)
    creation_date = models.DateField(auto_now_add=True)
    expiration_date = models.DateField(null=True)

    class Meta:
        unique_together = (('from_character', 'to_character', 'bond'))


class GameItem(models.Model):
    game = models.ForeignKey(Game, related_name='items')
    name = models.CharField(max_length=100)
    description = models.TextField()
    item_type = models.CharField(max_length=3,
        choices = (
            ('NPC', "NPC"),
            ("LOC", 'Location'),
            ("ITM", 'Item'),
        )
    )
    class Meta:
        unique_together = (('game', 'name'),)


class Stat(models.Model):
    stat_name = models.CharField(max_length=255)
    stat_value = models.TextField(default='')
    val_type = models.CharField(max_length=4,
        choices = (
            ("NUM", "NUMERIC"),
            ("TXT", 'TEXT'),
            ('IMG', 'IMAGE'),
        )
    )
    class Meta:
        abstract = True


class CharacterStat(Stat):
    game_character = models.ForeignKey(GameCharacter, related_name='stats')

    class Meta:
        unique_together = (('game_character', 'stat_name', 'stat_value'),)


class ItemStat(Stat):
    item = models.ForeignKey(GameItem, related_name='stats')

    class Meta:
        unique_together = (('item', 'stat_name', 'stat_value'),)


class GameSession(models.Model):
    game = models.ForeignKey(Game, related_name='sessions')
    session_title = models.CharField(max_length=255, default='')
    session_text = models.TextField(default='')
    session_date = models.DateTimeField(null=True)
    entry_created = models.DateTimeField(auto_now=True)
    last_updated = models.DateTimeField(null=True)

    class Meta:
        ordering = ['session_date',]


class UserGame(models.Model):
    user = models.ForeignKey(User, related_name='games')
    game = models.ForeignKey(Game, related_name='users')
    is_owner = models.BooleanField(default=False)
    status = models.CharField(max_length=7,
        choices=(
            ('PENDING', 'PENDING'),
            ('ACTIVE', 'ACTIVE'),
            ('RETIRED', 'RETIRED'),
            ('REMOVED', 'REMOVED')
        )
    )
    join_date = models.DateTimeField(blank=True)
    last_active_date = models.DateTimeField(blank=True)
    exp_date = models.DateTimeField(blank=True)

    class Meta:
        unique_together = (('user', 'game'),)


class UserUser(models.Model):
    from_user = models.ForeignKey(User, related_name="relationships")
    to_user = models.ForeignKey(User, related_name='related_to')

    class Meta:
        unique_together = (('from_user', 'to_user'),)
