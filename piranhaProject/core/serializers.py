from core import models
from rest_framework import serializers

class UserBalanceSerializer(serializers.Serializer):
    class Meta:
        model = models.UserBalance
        fields = '__all__'
