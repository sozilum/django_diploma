# Generated by Django 4.2.3 on 2024-07-03 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0058_rename_products_order_baskets'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='totalCost',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
