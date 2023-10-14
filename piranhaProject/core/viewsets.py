from django.db.models import F, Value, IntegerField, DecimalField
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from . import models
from . import serializers


class UserBalanceViewSet(ModelViewSet):
    serializer_class = serializers.UserBalanceSerializer
    ordering_fields = '__all__'
    ordering = ('-id',)
    queryset = models.UserBalance.objects.all()

    @action(detail=False, methods=['GET'])
    def pegada_carbono(self, request, *args, **kwargs):
        queryset = models.UserBalance.objects.annotate(
            pegada_eletricidade=F('energy_per_month') * Value(0.0817, output_field=DecimalField()),
            pegada_gasolina=F('car_distance_in_km') * Value(2.28 / 100, output_field=DecimalField()),
            pegada_gado=F('quantity_animal') * Value(8.856 * 28, output_field=DecimalField()),
            pegada_compostagem=F('composted_material_quantity') * Value(3 *28 / 1000, output_field=DecimalField()),
            pegada_fertilizante=F('fetilizante_kg') * Value(2, output_field=DecimalField())
        )

        queryset = queryset.annotate(
            pegada_total=(
                F('pegada_eletricidade') +
                F('pegada_gasolina') +
                F('pegada_gado') -
                F('pegada_compostagem') +
                F('pegada_fertilizante')
            )
        )
        serializer = serializers.UserBalanceSerializer(queryset, many=True, context={'request': request})
        return Response(data=serializer.data, status=200)
