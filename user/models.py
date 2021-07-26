from django.db import models
from django.utils.timezone import now
from django import forms
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.
class User(models.Model):
    email = models.EmailField(
        unique=True, verbose_name="Email", max_length=254, null=False)
    password = models.CharField(verbose_name="Contraseña", max_length=30)
    name = models.CharField(verbose_name="Nombre", max_length=50)
    credit_card = models.BigIntegerField(unique = True, verbose_name="Nro Tarjeta", null=False, 
                        validators=[MaxValueValidator(9999999999999), MinValueValidator(0)])
    safe_code = models.IntegerField(verbose_name="Código de Seguridad", null=False, 
                        validators=[MaxValueValidator(999), MinValueValidator(0)])

    class Meta:
        verbose_name = "usuario"
        verbose_name_plural = "usuario"
        ordering = ['name']

    def __str__(self):
        return self.email
