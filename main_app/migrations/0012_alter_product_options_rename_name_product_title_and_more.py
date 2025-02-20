# Generated by Django 4.2.3 on 2024-02-27 20:31

from django.db import migrations, models
import main_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_order_in_order'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['title', 'price', 'producer']},
        ),
        migrations.RenameField(
            model_name='product',
            old_name='name',
            new_name='title',
        ),
        migrations.RenameField(
            model_name='review',
            old_name='review',
            new_name='text',
        ),
        migrations.RemoveField(
            model_name='review',
            name='title',
        ),
        migrations.AddField(
            model_name='order',
            name='free_delivery',
            field=models.BooleanField(default=False, verbose_name=main_app.models.order_free_delivery),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='full_description',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='email',
            field=models.TextField(null=True, verbose_name=main_app.models.user_email),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
