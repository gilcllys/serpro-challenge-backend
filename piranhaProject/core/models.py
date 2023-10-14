from django.db import models


# Create your models here.

class UserBalance(models.Model):
   
    quantity_animal = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        db_column='nb_quantity_animal',
    )
    energy_per_month = models.IntegerField(
        null=True,
        blank=True,
        db_column='dc_energy_per_month',
    )

    car_distance_in_km = models.IntegerField(
        null=True,
        blank=True,
        db_column='nb_car_distance_in_km',
    )
    composted_material_quantity = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        db_column='dc_composted_material_quantity',
    )
    fetilizante_kg = models.IntegerField(
        null=True,
        blank=True,
        default=0,
        db_column='nb_fetilizante_kg',
    )

    month = models.IntegerField(
        null=False,
        blank=False,
        db_column='cb_month'
    )
    year = models.IntegerField(
        null=True,
        blank=True,
        db_column='nb_year',
    )
