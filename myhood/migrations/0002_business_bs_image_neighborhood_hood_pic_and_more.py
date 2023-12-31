# Generated by Django 4.2.8 on 2023-12-12 05:05

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myhood', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='bs_image',
            field=cloudinary.models.CloudinaryField(default='image/upload/v1627341811/company_default_qb4ili.png', max_length=255, verbose_name='images'),
        ),
        migrations.AddField(
            model_name='neighborhood',
            name='hood_pic',
            field=cloudinary.models.CloudinaryField(default='image/upload/v1627343010/neighborhood1_cj2fyx.jpg', max_length=255, verbose_name='images'),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_picture',
            field=cloudinary.models.CloudinaryField(default='image/upload/v1626430054/default_zogkvr.png', max_length=255, verbose_name='images'),
        ),
    ]
