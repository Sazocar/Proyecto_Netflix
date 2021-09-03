from django import forms
from .models import User, CreditCard, City, Country, Ubication, Perfil
from Netflix import settings
from django.db import models

SEX_CHOICES = (
    ("", ""),
    ("M", "M"),
    ("F", "F"),
    ("N/A", "N/A")
)


class UserModelForm(forms.ModelForm):
    email = forms.EmailField(help_text='A valid email address, please.', required=True, widget=forms.EmailInput(
        attrs={'placeholder': 'Email'}), min_length=3, max_length=100)
    password = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'placeholder': 'Contraseña'}), min_length=3, max_length=100)
    name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Nombre'}), min_length=3, max_length=100)
    last_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Apellido'}), min_length=3, max_length=100)
    user_name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Nombre de Usuario'}), min_length=3, max_length=100)
    age = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Edad'}), min_length=2, max_length=2)
    sex = forms.ChoiceField(required=True, choices = SEX_CHOICES, label="Sexo")

    class Meta:
        model = User
        fields = [
            'email',
            'password',
            'name',
            'last_name',
            'user_name',
            'age',
            'sex'
        ]

    def clean_email(self):
        data = self.cleaned_data.get('email')
        return data

    def clean_user_name(self):
        wrong_characters = {'@','-', '?', '`', '˜', '#', '%', 'ˆ', '&', '*', ',', '{', '}', '[', ']', '|', '¿', '¡', '(', ')', '=', '/', '+', '.'}
        data = self.cleaned_data.get('user_name')
        data_as_string = str(data)
        if any([data_as_string.startswith(special_character) for special_character in wrong_characters]):
            raise forms.ValidationError("Nombre de Usuario no puede empezar con caracteres especiales tales como: @-?`˜#%ˆ&*,{}[]|¿¡()=/+.")
        return data

    def clean_name(self):
        data = self.cleaned_data.get('name')
        if len(data) < 3:
            raise forms.ValidationError("El nombre es muy corto, debe ser mayor a 3 caracteres")
            return data
        elif data.isalpha() is False:
            raise forms.ValidationError(
                "Nombre solo puede tener letras desde A-Z. No se aceptan numeros, caracteres especiales ni espacios en blanco")
        return data

    def clean_age(self):
        data = self.cleaned_data.get('age')
        if data.isalpha():
            raise forms.ValidationError(
                "Edad solo puede tener números enteros. No se aceptan letras ni caracteres especiales")
        return data

    def clean_last_name(self):
        data = self.cleaned_data.get('last_name')
        if len(data) < 3:
            raise forms.ValidationError("El apellido es muy corto, debe ser mayor a 3 caracteres")
            return data
        elif data.isalpha() is False:
            raise forms.ValidationError(
                "Apellido solo puede tener letras desde A-Z. No se aceptan numeros ni caracteres especiales")
        return data

class CreditCardModelForm(forms.ModelForm):
    id_credit_card = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Número de Tarjeta'}), min_length=13, max_length=13)
    credit_card_date = forms.DateField(input_formats=["%m/%d/%Y"], required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Fecha de Vencimiento (MM/DD/AA)'}))
    safe_code = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Código de Seguridad'}), min_length=3, max_length=3)

    class Meta:
        model = CreditCard
        fields = [
            'id_credit_card',
            'credit_card_date',
            'safe_code'
        ]

    def clean_id_credit_card(self):
        data = self.cleaned_data.get('id_credit_card')
        if data.isalpha():
            raise forms.ValidationError(
                "Numero de tarjeta solo puede tener números enteros. No se aceptan letras ni caracteres especiales")
        return data

    def clean_safe_code(self):
        data = self.cleaned_data.get('safe_code')
        if data.isalpha():
            raise forms.ValidationError(
                "Código de seguridad solo puede tener números enteros. No se aceptan letras ni caracteres especiales")
        return data


class UbicationModelForm(forms.ModelForm):
    class Meta:
        model = Ubication
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['city'].queryset = City.objects.none()

        if 'country' in self.data:
            try:
                country_id = int(self.data.get('country'))
                self.fields['city'].queryset = City.objects.filter(
                    country_id=country_id).order_by('name')
            except (ValueError, TypeError):
                pass  # invalid input from the client; ignore and fallback to empty City queryset
        elif self.instance.pk:
            self.fields['city'].queryset = self.instance.country.city_set.order_by(
                'name')


class PerfilModelForm(forms.ModelForm):
    name1 = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Nombre de Perfil 1'}), max_length=50)
    name2 = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Nombre de Perfil 2'}), max_length=50)
    name3 = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Nombre de Perfil 3'}), max_length=50)
    name4 = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Nombre de Perfil 4'}), max_length=50)
    name5 = forms.CharField(required=False, widget=forms.TextInput(
        attrs={'placeholder': 'Nombre de Perfil 5'}), max_length=50)
    

    class Meta:
        model = Perfil
        fields = [
            'name1',
            'name2',
            'name3',
            'name4',
            'name5',
        ]

    def clean_name1(self):
        data = self.cleaned_data.get('name1')
        wrong_characters = {'@','-', '?', '`', '˜', '#', '%', 'ˆ', '&', '*', ',', '{', '}', '[', ']', '|', '¿', '¡', '(', ')', '=', '/', '+', '.'}
        data_as_string = str(data)
        if any([data_as_string.startswith(special_character) for special_character in wrong_characters]):
            raise forms.ValidationError("Nombre de Perfil no puede empezar con caracteres especiales tales como: @-?`˜#%ˆ&*,{}[]|¿¡()=/+.")
        return data

    def clean_name2(self):
        data = self.cleaned_data.get('name2')
        wrong_characters = {'@','-', '?', '`', '˜', '#', '%', 'ˆ', '&', '*', ',', '{', '}', '[', ']', '|', '¿', '¡', '(', ')', '=', '/', '+', '.'}
        data_as_string = str(data)
        if any([data_as_string.startswith(special_character) for special_character in wrong_characters]):
            raise forms.ValidationError("Nombre de Perfil no puede empezar con caracteres especiales tales como: @-?`˜#%ˆ&*,{}[]|¿¡()=/+.")
        return data

    def clean_name3(self):
        data = self.cleaned_data.get('name3')
        wrong_characters = {'@','-', '?', '`', '˜', '#', '%', 'ˆ', '&', '*', ',', '{', '}', '[', ']', '|', '¿', '¡', '(', ')', '=', '/', '+', '.'}
        data_as_string = str(data)
        if any([data_as_string.startswith(special_character) for special_character in wrong_characters]):
            raise forms.ValidationError("Nombre de Perfil no puede empezar con caracteres especiales tales como: @-?`˜#%ˆ&*,{}[]|¿¡()=/+.")
        return data

    def clean_name4(self):
        data = self.cleaned_data.get('name4')
        wrong_characters = {'@','-', '?', '`', '˜', '#', '%', 'ˆ', '&', '*', ',', '{', '}', '[', ']', '|', '¿', '¡', '(', ')', '=', '/', '+', '.'}
        data_as_string = str(data)
        if any([data_as_string.startswith(special_character) for special_character in wrong_characters]):
            raise forms.ValidationError("Nombre de Perfil no puede empezar con caracteres especiales tales como: @-?`˜#%ˆ&*,{}[]|¿¡()=/+.")
        return data

    def clean_name5(self):
        data = self.cleaned_data.get('name5')
        wrong_characters = {'@','-', '?', '`', '˜', '#', '%', 'ˆ', '&', '*', ',', '{', '}', '[', ']', '|', '¿', '¡', '(', ')', '=', '/', '+', '.'}
        data_as_string = str(data)
        if any([data_as_string.startswith(special_character) for special_character in wrong_characters]):
            raise forms.ValidationError("Nombre de Perfil no puede empezar con caracteres especiales tales como: @-?`˜#%ˆ&*,{}[]|¿¡()=/+.")
        return data
