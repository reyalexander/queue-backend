from rest_framework import serializers
from .models import Turn, TurnLog

class TurnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Turn
        fields = '__all__'

class TurnLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = TurnLog
        fields = '__all__'