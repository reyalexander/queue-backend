from rest_framework import serializers
from .models import QueueType, Counter

class QueueTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QueueType
        fields = '__all__'

        
class CounterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Counter
        fields = '__all__'