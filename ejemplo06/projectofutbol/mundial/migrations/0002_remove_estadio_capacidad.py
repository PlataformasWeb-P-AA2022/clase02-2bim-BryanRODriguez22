# Generated by Django 4.0.5 on 2022-06-14 00:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mundial', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estadio',
            name='capacidad',
        ),
    ]