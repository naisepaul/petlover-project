# Generated by Django 3.2.24 on 2024-03-16 23:38

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('home', '0003_alter_profile_profile_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('breed', models.CharField(choices=[('labrador retriever', 'Labrador Retriever'), ('german shepherd', 'German Shepherd'), ('golden retriever', 'Golden Retriever'), ('bulldog', 'Bulldog'), ('beagle', 'Beagle'), ('poodle', 'Poodle'), ('french bulldog', 'French Bulldog'), ('boxer', 'Boxer'), ('dachshund', 'Dachshund'), ('siberian husky', 'Siberian Husky'), ('yorkshire terrier', 'Yorkshire Terrier'), ('rottweiler', 'Rottweiler'), ('shih tzu', 'Shih Tzu'), ('great dane', 'Great Dane'), ('australian shepherd', 'Australian Shepherd'), ('doberman pinscher', 'Doberman Pinscher'), ('border collie', 'Border Collie'), ('shetland sheepdog', 'Shetland Sheepdog'), ('boston terrier', 'Boston Terrier')], max_length=100)),
                ('DOB', models.DateField()),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('temperament', models.TextField(choices=[('friendly', 'Friendly'), ('affectionate', 'Affectionate'), ('protective', 'Protective'), ('active', 'Active'), ('loyal', 'Loyal')], max_length=100)),
                ('photo', cloudinary.models.CloudinaryField(max_length=255, verbose_name='image')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dogs_for_sale', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('location', models.CharField(choices=[('antrim', 'Antrim'), ('armagh', 'Armagh'), ('carlow', 'Carlow'), ('cavan', 'Cavan'), ('clare', 'Clare'), ('cork', 'Cork'), ('derry', 'Derry'), ('donegal', 'Donegal'), ('down', 'Down'), ('dublin', 'Dublin'), ('fermanagh', 'Fermanagh'), ('galway', 'Galway'), ('kerry', 'Kerry'), ('kildare', 'Kildare'), ('kilkenny', 'Kilkenny'), ('laois', 'Laois'), ('leitrim', 'Leitrim'), ('limerick', 'Limerick'), ('longford', 'Longford'), ('louth', 'Louth'), ('mayo', 'Mayo'), ('meath', 'Meath'), ('monaghan', 'Monaghan'), ('offaly', 'Offaly'), ('roscommon', 'Roscommon'), ('sligo', 'Sligo'), ('tipperary', 'Tipperary'), ('tyrone', 'Tyrone'), ('waterford', 'Waterford'), ('westmeath', 'Westmeath'), ('wexford', 'Wexford'), ('wicklow', 'Wicklow')], max_length=100)),
                ('description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('dog', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.dog')),
            ],
        ),
    ]