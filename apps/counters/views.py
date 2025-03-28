from rest_framework.viewsets import ModelViewSet
from .models import QueueType, Counter
from .serializers import QueueTypeSerializer, CounterSerializer

class QueueTypeViewSet(ModelViewSet):
    queryset = QueueType.objects.all()
    serializer_class = QueueTypeSerializer

class CounterViewSet(ModelViewSet):
    queryset = Counter.objects.all()
    serializer_class = CounterSerializer