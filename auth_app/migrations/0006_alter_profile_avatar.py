# Generated by Django 4.2.3 on 2024-07-11 19:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auth_app', '0005_avatarprofile_alter_profile_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='avatar',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='auth_app.avatarprofile'),
        ),
    ]
