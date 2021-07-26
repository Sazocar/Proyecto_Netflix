from django import forms
from .models import User

class UserModelForm(forms.ModelForm):
    email = forms.EmailField(required=True, widget=forms.EmailInput(
        attrs={'placeholder': 'Email'}), min_length=3, max_length=100)
    password = forms.CharField(required=True, widget=forms.PasswordInput(
        attrs={'placeholder': 'Contraseña'}), min_length=3, max_length=100)
    name = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Escribe tu nombre'}), min_length=3, max_length=100)
    credit_card = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Número de Tarjeta'}), min_length=13, max_length=13)
    safe_code = forms.CharField(required=True, widget=forms.TextInput(
        attrs={'placeholder': 'Código de Seguridad'}), min_length=3, max_length=3)


    class Meta:
        model = User
        fields = [
            'email',
            'password',
            'name',
            'credit_card',
            'safe_code'
        ]

    def clean_name(self):
        data = self.cleaned_data.get('name')
        if len(data) < 3:
            raise forms.ValidationError("El nombre es muy corto, debe ser mayor a 3 caracteres")
            return data
        elif data.isalpha() is False:
            raise forms.ValidationError(
                "Nombre solo puede tener letras desde A-Z. No se aceptan numeros ni caracteres especiales")
        return data

    def clean_credit_card(self):
        data = self.cleaned_data.get('credit_card')
        if data.isalpha():
            raise forms.ValidationError(
                "Numero de tarjeta solo puede tener números enteros. No se aceptan letras ni caracteres especiales")
        return data

    def clean_safe_code(self):
        data = self.cleaned_data.get('safe_code')
        # data_as_int = int(data)
        if data.isalpha():
            raise forms.ValidationError(
                "Código de seguridad solo puede tener números enteros. No se aceptan letras ni caracteres especiales")
        return data
        # elif (data_as_int < 0):
        #     raise forms.ValidationError("Ingrese un codigo de seguridad positivo y entero de 3 digitos")
        # return data

    # def clean_name(self):
    #     data = self.cleaned_data.get('name')
    #     if data.isalpha() is False:
    #         raise forms.ValidationError("Nombre solo puede tener letras desde A-Z. No se aceptan numeros ni caracteres especiales")
    #     return data


    # name = forms.CharField(required=True, widget=forms.TextInput(
    #     attrs={'placeholder': 'Escribe tu nombre'}
    # ), min_length=3, max_length=100)
    # password = forms.EmailField(required=True, widget=forms.PasswordInput(
    #     attrs={'placeholder': 'Contraseña'}
    # ), min_length=3, max_length=100)
    # email = forms.EmailField(required=True, widget=forms.EmailInput(
    #     attrs={'placeholder': 'Escribe tu email'}
    # ), min_length=3, max_length=100)


    #  Validacion de cada campo en forms
    # def clean_name(self):
    #     data = self.cleaned_data.get('name')
    #     if len(data) < 6:
    #         raise forms.ValidationError('El campo debe ser mayor a 6 caracteres')
    #     return data

    
