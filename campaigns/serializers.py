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


class CharacterStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CharacterStat


class GameCharacterSerializer(serializers.ModelSerializer):
    game = GameSerializer
    character = CharacterSerializer
    stats = CharacterStatSerializer(many=True)

    class Meta:
        model = models.GameCharacter
        fields = '__all__'


class ItemStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ItemStat


class GameItemSerializer(serializers.ModelSerializer):
    stats = ItemStatSerializer(many=True)
    class Meta:
        model = models.GameItem


class GameSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GameSession


class GameDetailSerializer(serializers.ModelSerializer):
    characters = GameCharacterSerializer(many=True)
    items = GameItemSerializer(many=True)
    sessions = GameSessionSerializer(many=True)

    class Meta:
        model = models.Game
        fields = ('title', 'creator', 'description', 'characters', 'items', 'sessions')
