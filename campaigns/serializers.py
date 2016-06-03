from rest_framework import serializers

from . import models


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Character
        fields = ('character', 'user', 'creation_date')


class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Game
        fields = '__all__'


class GameCharacterSerializer(serializers.ModelSerializer):
    game = GameSerializer
    character = CharacterSerializer

    class Meta:
        model = models.GameCharacter
        fields = '__all__'


class GameNPCSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GameNPC


class GameSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GameSession


class GameLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GameLocation

class GameDetailSerializer(serializers.ModelSerializer):
    gamecharacter_set = GameCharacterSerializer(many=True)
    gamenpc_set = GameNPCSerializer(many=True)
    gamelocation_set = GameLocationSerializer(many=True)
    sessions = GameSessionSerializer(many=True)

    class Meta:
        model = models.Game
        fields = ('title', 'creator', 'gamecharacter_set', 'gamenpc_set', 'gamelocation_set', 'sessions')
