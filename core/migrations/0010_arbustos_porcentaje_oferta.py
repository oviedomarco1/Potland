# Generated by Django 4.1.5 on 2023-06-23 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_arbustos'),
    ]

    operations = [
        migrations.AddField(
            model_name='arbustos',
            name='porcentaje_oferta',
            field=models.IntegerField(default=0),
        ),
    ]
