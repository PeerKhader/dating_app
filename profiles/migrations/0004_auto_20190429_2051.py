# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-04-29 20:51
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0003_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='img')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='body_type',
            field=models.CharField(blank=True, choices=[('THIN', 'Thin'), ('AVERAGE', 'Average'), ('FIT', 'Fit'), ('MUSCULAR', 'Muscular'), ('A LITTLE EXTRA', 'A Little Extra'), ('CURVY', 'Curvy')], default='AVERAGE', max_length=15),
        ),
        migrations.AddField(
            model_name='profile',
            name='hair_colour',
            field=models.CharField(blank=True, choices=[('BLACK', 'Black'), ('BLONDE', 'Blonde'), ('BROWN', 'Brown'), ('RED', 'Red'), ('GREY', 'Grey'), ('BALD', 'Bald'), ('BLUE', 'Blue'), ('PINK', 'Pink'), ('GREEN', 'Green'), ('PURPLE', 'Purple'), ('OTHER', 'Other')], default='BLACK', max_length=10),
        ),
        migrations.AddField(
            model_name='profile',
            name='is_premium',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='profile',
            name='looking_for',
            field=models.CharField(blank=True, choices=[('MEN', 'Men'), ('WOMEN', 'Women'), ('BOTH', 'Both')], default='BOTH', max_length=5),
        ),
    ]
