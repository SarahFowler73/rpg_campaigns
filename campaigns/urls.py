from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register(r'characters', views.CharacterView, base_name='characters')
router.register(r'game_characters', views.GameCharacterView, base_name='game_characters')
router.register(r'character_stats', views.CharacterStatView, base_name='character_stats')


router.register(r'games', views.GameView, base_name='games')
router.register(
    r'games/(?P<game_id>[0-9]+)/items',
    views.GameItemView,
    base_name='items'
)
router.register(
    r'games/(?P<game_id>[0-9]+)/items/(?P<item_id>[0-9]+/stats)',
    views.ItemStatView,
    base_name='item_stats'
)
router.register(
    r'games/(?P<game_id>[0-9]+)/sessions',
    views.GameSessionView,
    base_name='sessions'
)

router.register(r'players', views.UserGameView, base_name='players')

urlpatterns = [
    # url(r'game/(?P<pk>[0-9]+)/?$', views.GameDetailView.as_view(), name='game_detail'),
    # url(r'game/?$', views.GameListView.as_view(), name='game_list'),

]

urlpatterns += router.urls
