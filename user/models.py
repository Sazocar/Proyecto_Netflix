from django.db import models
from django.utils.timezone import now
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class User(models.Model):
    id_user = models.AutoField(verbose_name="ID Usuario", primary_key=True)
    email = models.EmailField(
        unique=True, verbose_name="Email", max_length=254, null=False)
    password = models.CharField(verbose_name="Contraseña", max_length=50)
    name = models.CharField(verbose_name="Nombre", max_length=50)
    last_name = models.CharField(verbose_name="Apellido", max_length=30)
    user_name = models.CharField(unique=True, null=False, verbose_name="Nombre de usuario", max_length=50)
    age = models.IntegerField(verbose_name="Fecha de Nacimiento", null=False, 
                        validators=[MaxValueValidator(99), MinValueValidator(21)])
    sex = models.CharField(max_length=3, verbose_name="Sexo", null=False)


    class Meta:
        verbose_name = "usuario"
        verbose_name_plural = "usuarios"
        ordering = ['user_name']

    def __str__(self):
        return self.user_name


class CreditCard(models.Model):
    id_credit_card = models.BigIntegerField(unique = True, verbose_name="Numero Tarjeta", null=False, 
                        validators=[MaxValueValidator(9999999999999), MinValueValidator(0)])
    safe_code = models.IntegerField(verbose_name="Código de Seguridad", null=False, 
                        validators=[MaxValueValidator(999), MinValueValidator(0)])
    credit_card_date = models.DateField(verbose_name="Fecha de vencimiento tarjeta")


    class Meta:
        verbose_name = "tarjeta"
        verbose_name_plural = "tarjetas"
        ordering = ['id_credit_card']

    def __str__(self):
        return str(self.id_credit_card)


class Pais(models.Model):
    id_pais = models.AutoField(primary_key=True)
    nombre = models.CharField(unique=True, max_length=10)
    descripcion = models.CharField(max_length=50)

    class Meta:
        db_table = 'pais'
        verbose_name_plural='paises'
        ordering = ['id_pais']


    def __str__(self):
        return self.nombre


class Ciudad(models.Model):
    id_ciudad = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=10)
    descripcion = models.CharField(max_length=50)
    id_pais = models.ForeignKey(
        'Pais', on_delete=models.CASCADE, db_column='id_pais')

    class Meta:
        db_table = 'ciudad'
        verbose_name_plural = 'ciudades'
        ordering = ['id_ciudad']

    def __str__(self):
        return self.nombre
