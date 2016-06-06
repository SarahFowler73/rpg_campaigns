from rest_framework import serializers

from . import models

class RecursiveField(serializers.Serializer):
    def to_representation(self, value):
        serializer = self.parent.parent.__class__(value, context=self.context)
        return serializer.data


class CharacterStatSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CharacterStat


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


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Character
        fields = ('character', 'user', 'creation_date')


class GameCharacterSerializer(serializers.ModelSerializer):
    character = CharacterSerializer()
    stats = CharacterStatSerializer(many=True)
    class Meta:
        model = models.GameCharacter
        fields = ('character', 'stats')


class UserGameSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserGame


class GameSerializer(serializers.ModelSerializer):
    creator_name = serializers.SerializerMethodField()
    characters = GameCharacterSerializer(many=True)
    users = UserGameSerializer(many=True)

    def get_creator_name(self, obj):
        return models.Game.objects.get(id=obj.id).creator.username

    class Meta:
        model = models.Game
        fields = '__all__'


class GameDetailSerializer(serializers.ModelSerializer):
    characters = GameCharacterSerializer(many=True)
    items = GameItemSerializer(many=True)
    sessions = GameSessionSerializer(many=True)
    users = UserGameSerializer(many=True)

    class Meta:
        model = models.Game
        fields = ('title', 'creator', 'description', 'characters', 'items', 'sessions', 'users')
