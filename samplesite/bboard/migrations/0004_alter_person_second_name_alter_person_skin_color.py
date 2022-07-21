# Generated by Django 4.0.5 on 2022-07-19 15:33

import bboard.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0003_alter_firstmodel_options_person_second_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='second_name',
            field=models.CharField(default='', max_length=15, validators=[django.core.validators.MinLengthValidator(bboard.models.get_min_length)], verbose_name='Второе имя'),
        ),
        migrations.AlterField(
            model_name='person',
            name='skin_color',
            field=models.CharField(default='', max_length=15, validators=[django.core.validators.MinLengthValidator(bboard.models.get_min_length)], verbose_name='Цвет кожи'),
        ),
    ]
