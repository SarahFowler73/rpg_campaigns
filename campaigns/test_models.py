import json

from django.test import TestCase
from django.utils import timezone
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.core.urlresolvers import reverse

from .models import (Game, Character, GameCharacter, GameCharacterCharacter,
                     GameItem, CharacterStat, ItemStat, GameSession, UserGame)


class BaseTests:
    class BaseModelTests(TestCase):
        fixtures = ['fixtures.json']

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

    def test_game_character_unique(self):
        with self.assertRaises(IntegrityError):
            GameCharacter.objects.create(
                character_id=4,
                game_id=12)


class UserGameModelTests(BaseTests.BaseModelTests):
    def test_user_game_unique(self):
        with self.assertRaises(IntegrityError):
            UserGame.objects.create(
                user_id=3,
                game_id=12,
                status="PENDING")


class GameCharacterCharacterModelTests(BaseTests.BaseModelTests):
    def test_to_from_bond_unique(self):
        with self.assertRaises(IntegrityError):
            GameCharacterCharacter.objects.create(
                from_character_id=2,
                to_character_id=1,
                bond="Was saved from dying in the desert. Owes his life, and will protect her.")

    def test_creation_date_set(self):
        bond, c = GameCharacterCharacter.objects.get_or_create(
            from_character_id=2,
            to_character_id=1,
            bond="New bond.")
        now = timezone.now()
        self.assertLess(bond.creation_date, now)


class GameItemModelTests(BaseTests.BaseModelTests):
    def test_game_item_name_unique(self):
        with self.assertRaises(IntegrityError):
            GameItem.objects.create(
                game_id=12,
                name="Tyr",
                description='City of Kalak',
                item_type='LOC')


class CharacterStatModelTests(BaseTests.BaseModelTests):
    def test_char_name_val_unique(self):
        with self.assertRaises(IntegrityError):
            CharacterStat.objects.create(
                game_character_id=1,
                stat_name='ASPECT',
                stat_value='Ends justify the means',
                val_type='TXT')


class ItemStatModelTests(BaseTests.BaseModelTests):
    def test_item_name_val_unique(self):
        with self.assertRaises(IntegrityError):
            ItemStat.objects.create(
                item_id=1,
                stat_name='MAP',
                stat_value="./static/images/favicon.ico",
                val_type='TXT')


class GameSessionModelTests(BaseTests.BaseModelTests):
    pass
