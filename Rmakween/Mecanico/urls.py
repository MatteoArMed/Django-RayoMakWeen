from django.urls import path
from .views import home, datosContacto, login, registro, mecanico, tienda, trabajosMecanico, Franchesco, Yayo, Luigi, administrarTrabajos,modificarTrabajo,eliminarTrabajo, admin, verTrabajo, verMensaje, licencia, terminosycondiciones, privacidad
# Desde aqui importamos todos los templates 

urlpatterns = [
    path('',home, name='home'),
    path('datosContacto',datosContacto, name='datosContacto'),
    path('accounts/login/', login, name='login'),
    path('registro',registro,name='registro'),
    path('mecanico',mecanico, name='mecanico'),
    path('tienda',tienda, name='tienda'),
    path('trabajosMecanico',trabajosMecanico,name='trabajosMecanico'),
    path('Franchesco', Franchesco, name='Franchesco'),
    path('Yayo', Yayo, name='Yayo'),
    path('Luigi', Luigi, name='Luigi'),
    path('administrarTrabajos', administrarTrabajos ,name='administrarTrabajos'),
    path('modificarTrabajo/<int:pk>/',modificarTrabajo,name='modificarTrabajo'),
    path('eliminarTrabajo/<str:pk>/',eliminarTrabajo, name='eliminarTrabajo'),
    path('admin/',admin,name='admin'),
    path('verTrabajo',verTrabajo,name='verTrabajo'),
    path('verMensaje',verMensaje, name='verMensaje'),
    path('licencia',licencia, name='licencia'),
    path('terminosycondiciones',terminosycondiciones, name='terminosycondiciones'),
    path('privacidad',privacidad,name='privacidad'),
    
]
