from rest_framework import serializers

from . import models


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Character


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Game
        fields = '__all__'


class GameCharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GameCharacter


class GameSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GameSession
