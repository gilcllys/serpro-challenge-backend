from django.db import models


# Create your models here.

class UserBalance(models.Model):
    class YesOrNo(models.TextChoices):
        Y = 'Y', 'SIM',
        N = 'N', 'NÃO'

    class Month(models.TextChoices):
        JAN = 'JAN', 'Janeiro',
        FEV = 'FEV', 'Fevereiro',
        MAR = 'MAR', 'Março',
        ABR = 'ABR', 'Abril',
        MAI = 'MAI', 'Abril',
        JUN = 'JUN', 'Junho',
        JUL = 'JUL', 'JULHO',
        AGO = 'AGO', 'Agosto',
        SET = 'SET', 'Setembro',
        OUT = 'OUT', 'Outubro',
        NOV = 'NOV', 'Novembro',
        DEZ = 'DEZ', 'Dezembro',

    has_animal = models.CharField(
        max_length=1,
        choices=YesOrNo.choices,
        default=YesOrNo.N,
        db_column='cb_has_animal'

    )

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

    month = models.CharField(
        max_length=3,
        choices=Month.choices,
        default=Month.JAN,
        db_column='cb_month'
    )
    year = models.IntegerField(
        null=True,
        blank=True,
        db_column='nb_year',
    )
