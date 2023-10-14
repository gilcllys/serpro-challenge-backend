from django.db import models

# Create your models here.

class UserBalance(models.Model):
    class YesOrNo(models.TextChoices):
        Y = 'Y','SIM',
        N = 'N','NÃO'
        
    class Month(models.TextChoices):
        JAN = 'JAN','Janeiro',
        FEV = 'FEV','Fevereiro',
        MAR = 'MAR','Março',
        ABR = 'ABR','Abril',
        MAI = 'MAI','Abril',
        JUN = 'JUN','Junho',
        JUL = 'JUL','JULHO',
        AGO = 'AGO','Agosto',
        SET = 'SET','Setembro',
        OUT = 'OUT','Outubro',
        NOV = 'NOV','Novembro',
        DEZ = 'DEZ','Dezembro',

    has_animal = models.CharField(
        max_length=1,
        choices=YesOrNo.choices,
        default=YesOrNo.N,
        db_column='cb_has_animal'
        
    )
    type_animal = models.CharField(
        null=True,
        blank=True,
        max_length=44,
        db_column='ch_type_animal',
    )
    quantity_animal = models.IntegerField(
        null=True,
        blank=True,
        db_column='nb_quantity_animal',
    )
    energy_per_month = models.DecimalField(
        null=True,
        blank=True,
        max_digits=5, 
        decimal_places=2,
        db_column='dc_energy_per_month',
    )
    car_quantity = models.IntegerField(
        null=True,
        blank=True,
        db_column='nb_car_quantity',
    )
    car_distance_in_km = models.IntegerField(
        null=True,
        blank=True,
        db_column='nb_car_distance_in_km',
    )
    composted_material_quantity = models.DecimalField(
        null=True,
        blank=True,
        max_digits=6, 
        decimal_places=2,
        db_column='dc_composted_material_quantity',
    )
    has_cultivo = models.CharField(
        max_length=1,
        choices=YesOrNo.choices,
        default=YesOrNo.N,
        db_column='cb_has_cultivo'
    )
    cultivo_type = models.CharField(
        null=True,
        blank=True,
        db_column='ch_cultivo_type',
    )
    cultivo_area = models.CharField(
        null=True,
        blank=True,
        db_column='ch_cultivo_area',
    )
    month = models.CharField(
        max_length=3,
        choices=Month.choices,
        default=Month.JAN,
        db_column='cb_month'
    )

