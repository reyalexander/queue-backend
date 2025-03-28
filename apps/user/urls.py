from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, EmployeeViewSet

router = DefaultRouter()
router.register(r'', UserViewSet, basename="user")
router.register(r'employee', EmployeeViewSet)

urlpatterns = [
    path('', include(router.urls)),
]