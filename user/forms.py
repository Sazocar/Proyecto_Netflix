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


    class Meta:
        model = User
        fields = [
            'email',
            'password',
            'name',
            'credit_card'
        ]

    # def clean_name(self):
    #     data = self.cleaned_data.get('name')
    #     if len(data) < 5:
    #         raise forms.ValidationError("El nombre es muy corto")
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

    
