from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TurnViewSet, TurnLogViewSet

router = DefaultRouter()
router.register(r'turn', TurnViewSet)
router.register(r'turn_log', TurnLogViewSet)

urlpatterns = [
    path('', include(router.urls)),
]