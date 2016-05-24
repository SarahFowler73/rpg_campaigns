import datetime

from flask.ext.login import UserMixin
from flask.ext.bcryp import generate_password_hash
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
