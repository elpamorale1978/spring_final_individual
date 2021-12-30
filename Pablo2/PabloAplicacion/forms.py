from django import forms
from django.forms.fields import EmailField
from django.forms.widgets import Textarea 
from .models import Usuario, Administrador, Comentario

class NuevosUsuariosForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields=('rut', 'nombre', 'apellido', 'email', 'contrasena')

class InicioSesionForm(forms.Form):
    Rut= forms.CharField(widget = forms.TextInput)
    Contrasena= forms.CharField(widget = forms.PasswordInput)

class NuevoAdministradorForm(forms.ModelForm):
    class Meta:
        model = Administrador
        fields=('usuario', 'email', 'contrasena', 'last_login')

class UserForm(forms.Form):
    nombre= forms.CharField(widget=forms.TextInput)
    email= forms.CharField(widget=forms.EmailInput)
    password= forms.CharField(widget=forms.PasswordInput)

class ContactoForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields=('nombre', 'email', 'comentario')
