from rest_framework.viewsets import ViewSet
from core import serializers
from core import models

class UserBalanceViewSet(ViewSet):
    serializer_class = serializers.UserBalanceSerializer
    ordering_fields = '__all__'
    ordering = ('-id',)
    queryset = models.UserBalance.objects.all()
