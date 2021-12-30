from django.db import models
from django.forms.widgets import PasswordInput

# Create your models here.

class Usuario(models.Model):
    rut= models.CharField(max_length=20, unique=True)
    nombre= models.CharField(max_length=30)
    apellido = models.CharField(max_length=50)
    email= models.CharField(max_length=70)
    contrasena = models.CharField(max_length=30)
    last_login = models.CharField(max_length=300)

class Administrador(models.Model):
    usuario= models.CharField(max_length=20, unique=True)
    email= models.CharField(max_length=70)
    contrasena = models.CharField(max_length=30)
    last_login = models.CharField(max_length=300)

class Comentario(models.Model):
    nombre= models.CharField(max_length=50)
    email= models.CharField(max_length=70)
    comentario = models.TextField(max_length=250)
    last_login = models.CharField(max_length=300)
    


    

