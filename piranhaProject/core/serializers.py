from . import models
from rest_framework import serializers
from django.db import models as dj_models


class SerializerBase(serializers.HyperlinkedModelSerializer):
    serializer_field_mapping = {
        dj_models.AutoField: serializers.IntegerField,
        dj_models.BigIntegerField: serializers.IntegerField,
        dj_models.BooleanField: serializers.BooleanField,
        dj_models.CharField: serializers.CharField,
        dj_models.CommaSeparatedIntegerField: serializers.CharField,
        dj_models.DateField: serializers.DateField,
        dj_models.DecimalField: serializers.DecimalField,
        dj_models.EmailField: serializers.EmailField,
        dj_models.Field: serializers.ModelField,
        dj_models.FileField: serializers.FileField,
        dj_models.FloatField: serializers.FloatField,
        dj_models.ImageField: serializers.ImageField,
        dj_models.IntegerField: serializers.IntegerField,
        dj_models.PositiveIntegerField: serializers.IntegerField,
        dj_models.PositiveSmallIntegerField: serializers.IntegerField,
        dj_models.SlugField: serializers.SlugField,
        dj_models.SmallIntegerField: serializers.IntegerField,
        dj_models.TextField: serializers.CharField,
        dj_models.TimeField: serializers.TimeField,
        dj_models.URLField: serializers.URLField,
        dj_models.GenericIPAddressField: serializers.IPAddressField,
        dj_models.FilePathField: serializers.FilePathField,
    }

    def get_field_names(self, declared_fields, info):
        fields = super().get_field_names(declared_fields, info)
        fields.insert(0, 'id')
        return fields


class UserBalanceSerializer(SerializerBase):
    pegada_total = serializers.IntegerField(read_only=True)
    class Meta:
        model = models.UserBalance
        fields = '__all__'
