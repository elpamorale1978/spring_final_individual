from django.urls import path
from . import views
from django.urls.resolvers import URLPattern


urlpatterns = [
    path('', views.index),
    path('index', views.index),
    path('yo', views.yo),
    path('jquery', views.jquery),
    path('galeria', views.galeria),
    path('contacto', views.contacto), 
    path('contacto1', views.contacto1),
    path('registro', views.registrate), 
    path('base', views.base),  
    path('sesion', views.login),
    path('salir', views.salir), 
    path('administrador', views.registroadm), 
    path('nuevousuario', views.crearuser), 
    path('obtenerusuarios', views.obtenerusuarios), 
    path('obtenerusuarios2', views.obtenerusuarios2) 
]
