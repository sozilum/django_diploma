# Generated by Django 4.2.3 on 2024-04-08 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0017_rename_categories_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='count',
            field=models.IntegerField(default=0, null = True),
        ),
    ]
