from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Vehiculo(models.Model):
    Tipo_Vehiculo = models.CharField(unique=False, max_length=255, blank=False, null=False)
    Anno_Vehiculo = models.DateField(blank=False, null=False)
    
    def __str__(self):
        return str(self.Tipo_Vehiculo)

class Contacto(models.Model):
    Fecha_Solicitud =       models.DateField(auto_now_add=True)
    Nombre_Contacto =       models.CharField(max_length=255,blank=False,null=False)
    Correo_Contacto =       models.EmailField(max_length=255,blank=False,null=False)
    Numero_Contacto =       models.CharField(max_length=12,blank=False,null=False)
    Descripcion_Contacto =  models.TextField(max_length=1000,blank=False,null=False)

    def __str__(self):
        return str(self.Fecha_Solicitud) + ' ' + self.Nombre_Contacto
    
class Mensajes(models.Model):
    Correo_Mensaje  =       models.EmailField(max_length=255,blank=False,null=False)
    Descripcion_Mensaje =   models.TextField(max_length=1000,blank=False,null=False)

    def __str__(self):
        return str(self.Correo_Mensaje)
    

class ImagenesMecanicos(models.Model):
    id_user_id=   models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='id_mecanicos')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='mecanico')
    Foto_Mecanico = models.ImageField(upload_to='fotosMecanicos')

    def __str__(self):
        return str(self.user)
    

class Atencion(models.Model):
    Fecha_Atencion = models.DateField(default=timezone.now)
    Fotos_Atencion = models.ImageField(upload_to='imagenesMecanicos', null=True)
    Diagnostico_Atencion = models.TextField(max_length=1000, blank=False)
    MaterialesUsados = models.CharField(max_length=1000, blank=False, null=False)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='id_mecanico_atencion')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='nombre_mecanico')
    EstadoTrabajo = models.TextField(max_length=1000, blank=True)
    id_Estado = models.IntegerField(blank=False)

    def __str__(self):
        return str(self.EstadoTrabajo)






