from django import forms
from .models import Contacto


class ContactoForm(forms.ModelForm): #De esta manera creamos el formulario necesario, el nombre luego se Instancia en Views

    Nombre_Contacto = forms.CharField(
        label='Nombre Contacto',
        widget=forms.TextInput(attrs={'class': 'contacto'})
    )

    Correo_Contacto = forms.CharField(
        label='Correo Contacto',
        widget=forms.TextInput(attrs={'class': 'contacto'})
    )

    Numero_Contacto = forms.CharField(
        label='Número Contacto',
        widget=forms.TextInput(attrs={'class': 'contacto'})
    )

    Descripcion_Contacto = forms.CharField(
        label='Descripción Contacto',
        widget=forms.TextInput(attrs={'class': 'contacto'})
    )

    class Meta:
        model = Contacto    #desde donde vamos a tomar los campos para el form
        fields = '__all__'  #importamos todos los campos declarados en Models de la clase contacto