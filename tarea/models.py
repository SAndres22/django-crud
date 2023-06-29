from django.db import models
from django.contrib.auth.models import User


#Comandos para crear el super Usuario
#py manage.py createsuperuser

# Create your models here.
class Tarea(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    #guardar fecha y hora de creacion de la tarea
    fecha_Creacion = models.DateTimeField(auto_now_add=True)
    fecha_Realizada = models.DateTimeField(null=True, blank=True)
    importancia = models.BooleanField(default=False)
    #Relacion con un usuario
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    #para que se vea mejor
    def __str__(self):
        return self.titulo + ' Por -->' + self.user.username