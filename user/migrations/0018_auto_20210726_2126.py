# Generated by Django 3.1.3 on 2021-07-26 21:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0017_auto_20210726_2120'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='safe_code',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(999), django.core.validators.MinValueValidator(0)], verbose_name='Código de Seguridad'),
        ),
    ]
