from rest_framework.viewsets import ModelViewSet
from .models import Clients
from .serializers import ClientsSerializer

class ClientsViewSet(ModelViewSet):
    queryset = Clients.objects.all()
    serializer_class = ClientsSerializer