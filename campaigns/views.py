from django.db.models import Q
from django.shortcuts import get_object_or_404
from rest_framework import viewsets, generics
from rest_framework.decorators import detail_route, list_route
from rest_framework.response import Response

from . import models, serializers

class CharacterView(viewsets.ModelViewSet):
    serializer_class = serializers.CharacterSerializer
    def get_queryset(self):
        return models.Character.objects.filter(user_id=self.request.user.id)


class GameCharacterView(viewsets.ModelViewSet):
    serializer_class = serializers.GameCharacterSerializer
    def get_queryset(self) :
        return models.GameCharacter.objects.filter(
            game__users__user_id=self.request.user.id
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
            users__user_id=self.request.user.id
        ).prefetch_related()


class GameDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = serializers.GameDetailSerializer

    def get_queryset(self):
        return models.Game.objects.filter(id=int(self.kwargs['pk']))


class UserGameView(viewsets.ModelViewSet):
    serializer_class = serializers.UserGameSerializer
    def get_queryset(self):
        return models.UserGame.objects.filter(
            user_id=self.request.user.id
        )

    @list_route(methods=['get'])
    def fellow_players(self, request):
        # Get the games the user belongs to
        games = models.UserGame.objects\
            .filter(user_id=self.request.user.id)\
            .values_list('game_id')
        # Get all players in mutually played games
        queryset = models.UserGame.objects\
            .filter(game_id__in=games)\
            .exclude(user_id=self.request.user.id)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class UserUserView(viewsets.ModelViewSet):
    serializer_class = serializers.UserUserSerializer
    def get_queryset(self):
        return models.UserUser.objects.filter(
            Q(to_user_id=self.request.user.id) |
            Q(from_user_id=self.request.user.id)
        )
