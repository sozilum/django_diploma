# Generated by Django 4.2.3 on 2024-06-02 16:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0035_categoriesavatar_productavatar_subcategoriesavatar_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categories',
            old_name='image',
            new_name='images',
        ),
        migrations.RenameField(
            model_name='subcategories',
            old_name='image',
            new_name='images',
        ),
    ]
