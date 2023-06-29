from django.contrib import admin


#agregar el modelo creado de tareas
from .models import Tarea


# Register your models here.
admin.site.register(Tarea)