import datetime

from flask.ext.login import UserMixin
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
