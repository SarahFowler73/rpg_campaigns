import datetime

from flask.ext.login import UserMixin
from flask.ext.bcrypt import generate_password_hash
import peewee as models

DATABASE = models.SqliteDatabase('rpg.db')


class User(UserMixin, models.Model):
    username = models.CharField(unique=True)
    email = models.CharField(unique=True)
    password = models.CharField(max_length=100)
    join_date = models.DateTimeField(default=datetime.datetime.now)
    is_admin = models.BooleanField(default=False)

    class Meta:
        database = DATABASE

    @classmethod
    def create_user(cls, username, email, password, admin=False):
        try:
            cls.create(
                username=username,
                email=email,
                password=generate_password_hash(password),
                is_admin=admin
            )
        except models.IntegrityError:
            raise ValueError("User already exists")


class Character(models.Model):
    character = models.PrimaryKeyField(unique=True, null=False)
    user = models.ForeignKeyField(User, related_name='characters')
    creation_date = models.DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = DATABASE
        indexes = ((('character', 'user'), True),)


class Game(models.Model):
    title = models.CharField(max_length=100, null=False)
    creator = models.ForeignKeyField(User, related_name='created_games')
    creation_date = models.DateTimeField(default=datetime.datetime.now)
    last_active_date = models.DateTimeField(null=True)

    class Meta:
        database = DATABASE
        indexes = ((('title', 'creator'), True),)
        order_by = ('last_active_date', 'creation_date')


class GameCharacter(models.Model):
    character = models.ForeignKeyField(
        Character,
        to_field='character',
        related_name='games')
    game = models.ForeignKeyField(Game, related_name='characters')
    stat_type = models.CharField(max_length=255)
    stat_value = models.TextField(default='')

    class Meta:
        database = DATABASE
        indexes = ((('game', 'character'), True),)


class GameSession(models.Model):
    game = models.ForeignKeyField(Game, related_name='sessions')
    session_title = models.CharField(default='')
    session_text = models.TextField(default='')
    session_date = models.DateTimeField(null=True)
    entry_date = models.DateTimeField(default=datetime.datetime.now)
    last_updated = models.DateTimeField(null=True)

    class Meta:
        database = DATABASE
        order_by = ('session_date',)


class UserGame(models.Model):
    user = models.ForeignKeyField(User, related_name='games')
    game = models.ForeignKeyField(Game, related_name='users')
    is_owner = models.BooleanField(default=False)
    status = models.CharField(
        choices=('PENDING', 'ACTIVE', 'RETIRED', 'REMOVED')
    )
    join_date = models.DateTimeField(null=True)
    last_active_date = models.DateTimeField(null=True)
    exp_date = models.DateTimeField(null=True)

    class Meta:
        database = DATABASE
        indexes = ((('user', 'game'), True),)


def initialize():
    DATABASE.connect()
    DATABASE.create_tables(
        [User, Game, Character, GameCharacter],
        safe=True)
    DATABASE.close()
