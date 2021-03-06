# Generated by Django 3.2.5 on 2021-07-28 22:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0013_user_id_city'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='id_city',
            new_name='city',
        ),
        migrations.AddField(
            model_name='user',
            name='country',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='user.country'),
        ),
    ]
