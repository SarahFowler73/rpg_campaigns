from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register(r'character', views.CharacterView, base_name='character')
router.register(r'game_character', views.GameCharacterView, base_name='game_character')

urlpatterns = [
    url(r'game/(?P<pk>[0-9]+)/?$', views.GameDetailView.as_view(), name='game_detail'),
    url(r'game', views.GameListView.as_view(), name='game_list'),

]


urlpatterns += router.urls
