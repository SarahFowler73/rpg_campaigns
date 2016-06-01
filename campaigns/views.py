from django.db.models import Q
from rest_framework import viewsets, generics


from . import models, serializers

class CharacterView(viewsets.ModelViewSet):
    serializer_class = serializers.CharacterSerializer
    def get_queryset(self):
        return models.Character.objects.filter(user_id=self.request.user.id)


class GameCharacterView(viewsets.ModelViewSet):
    serializer_class = serializers.GameCharacterSerializer
    def get_queryset(self) :
        return models.GameCharacter.objects.filter(
            character__user_id=self.request.user.id
        )


class GameView(viewsets.ModelViewSet):
    serializer_class = serializers.GameSerializer
    def get_queryset(self):
        return models.Game.objects.filter(
            Q(characters__character__user_id=self.request.user.id) |
            Q(creator_id=self.request.user.id)
        )
