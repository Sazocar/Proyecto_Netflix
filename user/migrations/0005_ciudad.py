# Generated by Django 3.2.5 on 2021-07-28 02:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0004_auto_20210727_2246'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('id_ciudad', models.AutoField(primary_key=True, serialize=False, verbose_name='Id Ciudad')),
                ('name', models.CharField(max_length=50, unique=True, verbose_name='Nombre')),
                ('description', models.TextField(verbose_name='Descripción')),
                ('id_country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.country', verbose_name='Id Pais')),
            ],
            options={
                'verbose_name': 'ciudad',
                'verbose_name_plural': 'ciudades',
                'ordering': ['name'],
            },
        ),
    ]
