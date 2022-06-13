# Generated by Django 3.2.4 on 2021-06-10 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrativo', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='estudiante',
            name='tipo_estudiante',
            field=models.CharField(choices=[('becado', 'Estudiante Becado'), ('no-becado', 'Estudiante No Becado')], default='becado', max_length=30),
            preserve_default=False,
        ),
    ]