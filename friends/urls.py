from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'friend', views.UserUserView, base_name='friend')

urlpatterns = router.urls
