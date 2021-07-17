# Generated by Django 3.2.5 on 2021-07-17 08:53

import cloudinary.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('awwardsapp', '0003_alter_rating_average'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.TextField(default='user bio', max_length=200),
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=cloudinary.models.CloudinaryField(default='https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQI6LEtiD3hnhE1XMgE5eoafi_JFE5hxp4N4A&usqp=CAU', max_length=255, verbose_name='pic'),
        ),
    ]
