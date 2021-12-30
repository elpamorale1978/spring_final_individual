from django.shortcuts import render, redirect
from PabloAplicacion.backend import MyBackend
from .forms import NuevosUsuariosForm, InicioSesionForm, NuevoAdministradorForm, UserForm, ContactoForm
from .models import Usuario, Administrador
from django.contrib.auth.models import User 
from django.contrib.auth import login as auth_login, logout, authenticate
from django.forms.forms import Form
from django.contrib.auth.decorators import login_required

myBackend=MyBackend()

# Create your views here.

def index(request):
    return render(request, 'PabloAplicacion/index.html')

def yo(request):
    return render(request, 'PabloAplicacion/yo.html')

#def yo2(request):
#    return render(request, 'PabloAplicacion/yo2.html')

def jquery(request):
    return render(request, 'PabloAplicacion/jquery.html')

def galeria(request):
    return render(request, 'PabloAplicacion/galeria.html')

def contacto(request):
    if request.method == "POST":
        form = ContactoForm(data = request.POST)
        if form.is_valid():
            contacto = form.save(commit = False)
            contacto.save()
        return redirect('/index')
    else:
        form = ContactoForm()
        return render(request,'PabloAplicacion/contacto.html', {"form": form})

def contacto1(request):
    if request.method == "POST":
        form = ContactoForm(data = request.POST)
        if form.is_valid():
            contacto = form.save(commit = False)
            contacto.save()
        return redirect('/index')
    else:
        form = ContactoForm()
        return render(request,'PabloAplicacion/contacto1.html', {"form": form})


def registrate(request):
    if request.method == "POST":
        form = NuevosUsuariosForm(data = request.POST)
        if form.is_valid():
            usuario = form.save(commit = False)
            usuario.save()
        return redirect('/index')
    else:
        form = NuevosUsuariosForm()
        return render(request,'PabloAplicacion/registro.html', {"form": form})


def registroadm(request):
    if request.method == "POST":
        form = NuevoAdministradorForm(data = request.POST)
        if form.is_valid():
            administrador = form.save(commit = False)
            administrador.save()
        return redirect('/base')
    else:
        form = NuevoAdministradorForm()
        return render(request,'PabloAplicacion/registroadm.html', {"form": form})

def login(request, backend='PabloAplicacion.backend.MyBackend'):
    usuario = Usuario.objects.all()
    if request.method == "POST":
        form = InicioSesionForm(data = request.POST)
        if form.is_valid():
            IngresarRUT = form.cleaned_data["Rut"]
            IngresarContrasena = form.cleaned_data["Contrasena"]
            user = myBackend.authenticate(request, username=IngresarRUT, password=IngresarContrasena)
            if user is not None:
                auth_login(request, user, backend)
#                if 'next' in request.POST:
#                    return render(request, 'PabloAplicacion/base.html', {"data":usuario})      
#                else: 
                return render(request, 'PabloAplicacion/bienvenida.html', {"user":user})
            else:
                return render(request, 'PabloAplicacion/sesion.html', {"form":form})
    else:
        form = InicioSesionForm()
        return render (request, 'PabloAplicacion/sesion.html', {"form":form})

def salir(request):
    return redirect('/index')

def base(request):
    usuario = Usuario.objects.all()
    return render(request, 'PabloAplicacion/base.html', {"data":usuario})
    
def crearuser(request):
    if request.method == "POST":
        form = UserForm(data = request.POST)
        if form.is_valid():
            nombre= form.cleaned_data["nombre"]
            email= form.cleaned_data["email"]
            password= form.cleaned_data["password"]
            user = User.objects.create_user(nombre, email, password)
            user.save()
            return redirect('/admin')
    else:
        form = UserForm()
        return render(request,'PabloAplicacion/registrouser.html', {"form": form})

def obtenerusuarios(request):
    usuario = Usuario.objects.raw('select * from PabloAplicacion_usuario')
    for u in usuario:
        print(u.rut, u.nombre, u.apellido)
    return render(request, 'PabloAplicacion/index.html',{'data': usuario})

def obtenerusuarios2(request):
    usuarios = Usuario.objects.all()
    usuarios2 = Usuario.objects.filter(nombre__startswith="M")
    usuarios3 = Usuario.objects.get(pk=2)
    print(usuarios3.id, usuarios3.rut, usuarios3.nombre)
    print   
    for u in usuarios2:
        print(u.id, u.rut, u.nombre, u.apellido)
    print(usuarios2)
   