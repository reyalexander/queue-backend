from rest_framework.viewsets import ModelViewSet
from .models import User, Employee
from .serializers import UserSerializer, EmployeeSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class EmployeeViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer