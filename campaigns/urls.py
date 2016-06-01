from django.conf.urls import url
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()

router.register(r'character', views.CharacterView, base_name='character')
router.register(r'game_character', views.GameCharacterView, base_name='game_character')
router.register(r'game', views.GameView, base_name='game')

urlpatterns = router.urls
