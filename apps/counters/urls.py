from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import CounterViewSet, QueueTypeViewSet

router = DefaultRouter()
router.register(r'', CounterViewSet)
router.register(r'queue_type', QueueTypeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]