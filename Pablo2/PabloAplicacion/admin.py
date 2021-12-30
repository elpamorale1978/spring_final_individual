from django.contrib import admin
from .models import Usuario, Administrador, Comentario

# Register your models here.

admin.site.register(Usuario)
admin.site.register(Administrador)
admin.site.register(Comentario)
