# Generated by Django 4.2.6 on 2023-10-14 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_userbalance_composted_material_quantity'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userbalance',
            name='has_animal',
        ),
        migrations.AlterField(
            model_name='userbalance',
            name='month',
            field=models.IntegerField(db_column='cb_month'),
        ),
    ]