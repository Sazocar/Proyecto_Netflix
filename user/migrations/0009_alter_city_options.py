# Generated by Django 3.2.5 on 2021-07-28 03:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_alter_city_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='city',
            options={'ordering': ['name'], 'verbose_name': 'ciudad', 'verbose_name_plural': 'ciudades'},
        ),
    ]
