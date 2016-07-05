from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register(r'character', views.CharacterView, base_name='character')
router.register(r'game_character', views.GameCharacterView, base_name='game_character')
router.register(
    r'game_character/(?P<game_character_id>[0-9]+)/character_stat',
    views.CharacterStatView,
    base_name='character_stat'
)

router.register(r'game', views.GameView, base_name='game')
router.register(
    r'game/(?P<game_id>[0-9]+)/item',
    views.GameItemView,
    base_name='item'
)
router.register(
    r'game/(?P<game_id>[0-9]+)/item/(?P<item_id>[0-9]+)/stat',
    views.ItemStatView,
    base_name='item_stat'
)
router.register(
    r'game/(?P<game_id>[0-9]+)/session',
    views.GameSessionView,
    base_name='session'
)

router.register(r'player', views.UserGameView, base_name='player')

urlpatterns = [
    # url(r'game/(?P<pk>[0-9]+)/?$', views.GameDetailView.as_view(), name='game_detail'),
    # url(r'game/?$', views.GameListView.as_view(), name='game_list'),

]

urlpatterns += router.urls
