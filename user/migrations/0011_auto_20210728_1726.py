# Generated by Django 3.2.5 on 2021-07-28 21:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0010_ubicacion'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ubicacion',
            options={'ordering': ['country'], 'verbose_name': 'ubicacion', 'verbose_name_plural': 'ubicaciones'},
        ),
        migrations.RenameField(
            model_name='ubicacion',
            old_name='ciudad',
            new_name='city',
        ),
        migrations.RenameField(
            model_name='ubicacion',
            old_name='pais',
            new_name='country',
        ),
    ]
