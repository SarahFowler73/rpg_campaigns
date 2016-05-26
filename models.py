import datetime

from flask.ext.login import UserMixin
from flask.ext.bcrypt import generate_password_hash
import peewee as models


DATABASE = models.SqliteDatabase('rpg.db')


class Character(models.Model):
    character = models.PrimaryKeyField(unique=True, null=False)
    user = models.ForeignKeyField(User)
    creation_date = models.DateTimeField(default=datetime.datetime.now)


class Game(models.Model):
    title = models.CharField(null=False)
    creator = models.ForeignKeyField('User', related_name='game_creator')
    creation_date = models.DateTimeField(default=datetime.default.now)
    last_active_date = models.DateTimeField()

    class Meta:
        database = DATABASE


class GameCharacter(models.Model):
    character = models.ForeignKeyField(Character, to_field='character')
    game = models.ForeignKeyField(Game)
    stat_type = models.CharField(max_length=255)
    stat_value = models.TextField(default='')

    class Meta:
        database = DATABASE


class GameSession(models.Model):
    game = models.ForeignKeyField(Game)
    session_title = models.CharField(default='')
    session_text = models.TextField(default='')
    session_date = models.DateTimeField()
    entry_date = models.DateTimeField(default=datetime.datetime.now)
    last_updated = models.DateTimeField()

    class Meta:
        database = DATABASE


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


class UserGame(models.Model):
    user = models.ForeignKeyField(User)
    game = models.ForeignKeyField(Game)
    is_owner = models.BooleanField(default=False)
    status = models.CharField(
        choices=('PENDING', 'ACTIVE', 'RETIRED', 'REMOVED')
    )
    join_date = models.DateTimeField()
    last_active_date = models.DateTimeField()
    exp_date = models.DateTimeField()

    class Meta:
        database = DATABASE


def initialize():
    DATABASE.connect()
    DATABASE.create_tables([User], safe=True)
    DATABASE.close()
