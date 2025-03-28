from rest_framework.viewsets import ModelViewSet
from .models import Turn, TurnLog
from .serializers import TurnSerializer, TurnLogSerializer

class TurnViewSet(ModelViewSet):
    queryset = Turn.objects.all()
    serializer_class = TurnSerializer

class TurnLogViewSet(ModelViewSet):
    queryset = TurnLog.objects.all()
    serializer_class = TurnLogSerializer