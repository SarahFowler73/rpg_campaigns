from rest_framework import serializers

from . import models


class CharacterSerializer(serializers.ModelSerializer):
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
        view_name='campaigns:game_characters-detail'
    )
    players = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='campaigns:players-detail'
    )
    sessions = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='campaigns:sessions-detail'
    )
    items = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='campaigns:items-detail'
    )
    def get_creator_name(self, obj):
        return models.Game.objects.get(id=obj.id).creator.username

    class Meta:
        model = models.Game
        fields = '__all__'


class GameCharacterSerializer(serializers.ModelSerializer):
    character = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='campaigns:characters-detail'
    )
    stats = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='campaigns:character_stats-detail'
    )
    class Meta:
        model = models.GameCharacter
        fields = '__all__'


class GameItemSerializer(serializers.ModelSerializer):
    stats = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='campaigns:item_stats'
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
