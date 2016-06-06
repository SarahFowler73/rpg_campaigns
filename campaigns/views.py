from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics
from rest_framework.decorators import detail_route, list_route


from . import models, serializers

class CharacterView(viewsets.ModelViewSet):
    serializer_class = serializers.CharacterSerializer
    def get_queryset(self):
        return models.Character.objects.filter(user_id=self.request.user.id)


class GameCharacterView(viewsets.ModelViewSet):
    serializer_class = serializers.GameCharacterSerializer
    def get_queryset(self) :
        return models.GameCharacter.objects.filter(
            Q(game__creator_id=self.request.user.id) |
            Q(game__characters__character__user_id=self.request.user.id)
        )


class GameSessionView(viewsets.ModelViewSet):
    serializer_class = serializers.GameSessionSerializer
    queryset = []

    @list_route
    def sessions(self, request):
        return models.GameSession.objects.filter(
            game_id=self.kwargs['game_id']
        ).ordering('session_date', 'last_updated')


class GameListView(generics.ListAPIView):
    serializer_class = serializers.GameSerializer
    def get_queryset(self):
        return models.Game.objects.filter(
            Q(characters__character__user_id=self.request.user.id) |
            Q(creator_id=self.request.user.id)
        ).prefetch_related()


class GameDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.GameDetailSerializer

    def get_queryset(self):
        return models.Game.objects.filter(id=int(self.kwargs['pk']))
