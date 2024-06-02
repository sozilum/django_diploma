# Generated by Django 4.2.3 on 2024-06-01 18:07

from django.db import migrations, models
import django.db.models.deletion
import main_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0034_alter_basket_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Categoriesavatar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('src', models.ImageField(null=True, upload_to=main_app.models.image_upload_categories)),
                ('alt', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Productavatar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('src', models.ImageField(null=True, upload_to=main_app.models.image_upload)),
                ('alt', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Subcategoriesavatar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('src', models.ImageField(null=True, upload_to=main_app.models.image_upload_subcategories)),
                ('alt', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Subcategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.subcategoriesavatar')),
            ],
        ),
        migrations.AddField(
            model_name='categories',
            name='subcategories',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.subcategories'),
        ),
        migrations.AlterField(
            model_name='categories',
            name='image',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.categoriesavatar'),
        ),
        migrations.AlterField(
            model_name='product',
            name='images',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='main_app.productavatar'),
        ),
    ]
