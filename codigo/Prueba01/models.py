from django.db import models

# Create your models here.

class Genero(models.Model):
    id_genero = models.AutoField(db_column='idGenero',prymary_ket=True)
    genero = models.CharField(max_length=20,blank=False,null=False)