# Generated by Django 3.1.3 on 2021-07-26 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('password', models.CharField(max_length=30, verbose_name='Contraseña')),
                ('name', models.CharField(max_length=50, verbose_name='Nombre')),
                ('created', models.DateField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'usuario',
                'verbose_name_plural': 'usuario',
                'ordering': ['email'],
            },
        ),
    ]
