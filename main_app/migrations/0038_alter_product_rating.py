# Generated by Django 4.2.3 on 2024-06-02 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0037_rename_images_categories_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='rating',
            field=models.TextField(null=True),
        ),
    ]
