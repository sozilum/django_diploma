# Generated by Django 4.2.3 on 2024-07-16 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0066_alter_review_options_rename_points_review_rate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='tags',
        ),
        migrations.AddField(
            model_name='products',
            name='tags',
            field=models.ManyToManyField(to='main_app.tags'),
        ),
    ]
