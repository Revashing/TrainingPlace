# Generated by Django 4.1 on 2022-08-29 10:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bboard', '0006_auto_20220829_1334'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='machine',
            name='spares',
        ),
    ]
