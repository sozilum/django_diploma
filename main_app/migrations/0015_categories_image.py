# Generated by Django 4.2.3 on 2024-03-31 20:56

from django.db import migrations, models
import main_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0014_product_available_product_free_delivery'),
    ]

    operations = [
        migrations.AddField(
            model_name='categories',
            name='image',
            field=models.ImageField(null=True, upload_to=main_app.models.image_upload_categories),
        ),
    ]
