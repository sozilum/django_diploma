# Generated by Django 4.2.3 on 2024-06-30 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0053_rename_basket_basketitems_products'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='basket',
            name='products',
        ),
        migrations.AddField(
            model_name='basket',
            name='basketitems',
            field=models.ManyToManyField(to='main_app.basketitems'),
        ),
    ]
