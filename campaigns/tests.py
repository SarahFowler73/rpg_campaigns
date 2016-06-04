from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.core.urlresolvers import reverse

from .models import Character, Game, GameCharacter


class BaseTests:
    class BaseModelTests(TestCase):
        @classmethod
        def setUpClass(cls):
            super(BaseTests.BaseModelTests, cls).setUpClass()
            User.objects.create(
                id=1, username='sarah', email='sarah@stuff.com')
            Game.objects.create(
                id=1,
                creator_id=1,
                title='My Cool Game')
            Character.objects.create(
                id=1,
                user_id=1,
                character='Billy the Kid')

        @classmethod
        def tearDownClass(cls):
            super(BaseTests.BaseModelTests, cls).tearDownClass()
            User.objects.all().delete()
            Game.objects.all().delete()
            Character.objects.all().delete()


class CharacterModelTests(BaseTests.BaseModelTests):
    def test_character_user_unique(self):
        with self.assertRaises(IntegrityError):
            Character.objects.create(
                user_id=1,
                character='Billy the Kid')

    def test_created_date_set(self):
        character, c = Character.objects.get_or_create(
            user_id=1,
            character="Jenny Peters"
        )
        now = timezone.now()
        self.assertLess(character.creation_date, now)


class GameModelTests(BaseTests.BaseModelTests):
    def test_game_creator_unique(self):
        with self.assertRaises(IntegrityError):
            Game.objects.create(
                creator_id=1,
                title='My Cool Game',
                description='I described it!')

    def test_created_date_set(self):
        game, c = Game.objects.get_or_create(
            creator_id=1,
            title='My REALLY Cool Game',
            description="I described this, too!")
        now = timezone.now()
        self.assertLess(game.creation_date, now)

    def test_description_unneeded(self):
        try:
            Game.objects.create(
                creator_id=1,
                title="My Non-Descript Game"
            )
        except :
            self.fail('Game should be create-able without description')

class GameCharacterModelTests(BaseTests.BaseModelTests):
    @classmethod
    def setUpClass(cls):
        super(GameCharacterModelTests, cls).setUpClass()
        GameCharacter.objects.create(
            character_id=1,
            game_id=1)

    @classmethod
    def tearDownClass(cls):
        super(GameCharacterModelTests, cls).tearDownClass()
        GameCharacter.objects.all().delete()

    def test_game_character_stat_unique(self):
        with self.assertRaises(IntegrityError):
            GameCharacter.objects.create(
                character_id=1,
                game_id=1)
