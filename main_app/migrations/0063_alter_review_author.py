# Generated by Django 4.2.3 on 2024-07-04 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0062_alter_review_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='author',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
