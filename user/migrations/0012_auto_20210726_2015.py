# Generated by Django 3.1.3 on 2021-07-26 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_auto_20210726_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='credit_card',
            field=models.PositiveIntegerField(verbose_name='Nro Tarjeta'),
        ),
    ]
