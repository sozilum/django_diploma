# Generated by Django 4.2.3 on 2024-07-04 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0061_alter_order_address_alter_order_city_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='email',
            field=models.TextField(blank=True, null=True),
        ),
    ]
