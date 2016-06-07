import json

from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.core.urlresolvers import reverse

from .models import (Game, Character, GameCharacter, GameCharacterCharacter,
                     GameItem, CharacterStat, ItemStat, GameSession, UserGame)


def get_json():
    with open('campaigns/mock_data.json') as data_file:
        data = json.load(data_file)
    return data


def set_up_db():
    data = get_json()
    for model, key in [
        (User, 'users'), (Game, 'games'), (Character, 'characters'),
        (UserGame, 'user_games'), (GameCharacter, 'game_characters'),
        (GameCharacterCharacter, 'game_character_characters'),
        (GameItem, 'game_items'), (ItemStat, 'item_stats'),
        (CharacterStat, 'character_stats')
    ]:
        map(lambda item: model.objects.create(**item), data[key])


class BaseTests:
    class BaseModelTests(TestCase):
        @classmethod
        def setUpClass(cls):
            super(BaseTests.BaseModelTests, cls).setUpClass()
            set_up_db()

        @classmethod
        def tearDownClass(cls):
            super(BaseTests.BaseModelTests, cls).tearDownClass()
            for model in [
                ItemStat, CharacterStat, GameItem, GameCharacterCharacter,
                GameCharacter, Character, UserGame, Game, User
            ]:
                model.objects.all().delete()



class CharacterModelTests(BaseTests.BaseModelTests):
    def test_character_user_unique(self):
        with self.assertRaises(IntegrityError):
            Character.objects.create(
                user_id=1,
                character='Tyr Ma')

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
                creator_id=3,
                title='Dark Sun',
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
            game_id=12)

    @classmethod
    def tearDownClass(cls):
        super(GameCharacterModelTests, cls).tearDownClass()
        GameCharacter.objects.all().delete()

    def test_game_character_stat_unique(self):
        with self.assertRaises(IntegrityError):
            GameCharacter.objects.create(
                character_id=1,
                game_id=12)


# class UserGameModelTests(BaseTests.BaseModelTests):
#     pass
