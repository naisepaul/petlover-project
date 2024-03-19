# Generated by Django 3.2.24 on 2024-03-19 21:38

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0005_auto_20240317_2354'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=cloudinary.models.CloudinaryField(default='v1710884105/default-user-image_zeg1uq.webp', max_length=255, verbose_name='image'),
        ),
    ]
