from rest_framework import serializers

from . import models


class CharacterSerializer(serializers.ModelSerializer):
    games = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='campaigns:game_character-detail'
    )
    class Meta:
        model = models.Character
        fields = '__all__'


class CharacterStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CharacterStat


class GameSerializer(serializers.ModelSerializer):
    creator_name = serializers.SerializerMethodField()
    characters = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='campaigns:game_character-detail'
    )
    players = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='campaigns:player-detail'
    )
    sessions = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
    )
    items = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
    )
    def get_creator_name(self, obj):
        return models.Game.objects.get(id=obj.id).creator.username

    class Meta:
        model = models.Game
        fields = '__all__'


class GameCharacterSerializer(serializers.ModelSerializer):
    stats = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
    )
    class Meta:
        model = models.GameCharacter
        fields = '__all__'


class GameItemSerializer(serializers.ModelSerializer):
    stats = serializers.PrimaryKeyRelatedField(
        many=True,
        read_only=True,
    )
    class Meta:
        model = models.GameItem


class GameSessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.GameSession


class ItemStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ItemStat


class UserGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserGame
