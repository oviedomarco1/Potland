# Generated by Django 4.1.5 on 2023-07-05 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Suscripcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('usuario', models.EmailField(max_length=100)),
                ('estado', models.BooleanField(default=False)),
            ],
        ),
    ]
