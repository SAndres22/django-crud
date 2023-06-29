from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

# importar para crear un formulario de registro con el mismo Django
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
# Importar el modelo por defecto de la tabla user de django
# usar el comando apra migar lo de la bd -- py manage.py migrate y
from django.contrib.auth.models import User
# importar para enviar algunos mensajes como respuesta
from django.http import HttpResponse
#importar para pasar el usuario como un request a las cookis, la sesion
from django.contrib.auth import login, logout, authenticate
#importar error de BD de integridad (por ejemplo para no repetir nombre de usuario)
from django.db import IntegrityError

#Importamos el formulario que creamos para las tareas
from .forms import FormTarea

#Importar para consultar la BD del modelo de tarea
from .models import Tarea
#Proteger rutas
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    return render(request, "home.html")

# metodo de registro
def registro(request):

    if request.method == 'GET':
        return render(request, "registro.html", {
            'formRegistro': UserCreationForm
        })
    else:
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(username=request.POST['username'],
                                                password=request.POST['password1'])
                user.save()
                #pasamos un ide de sesion del usuario
                login(request, user)
                return redirect('tareas')
            except IntegrityError:
                return render(request, "registro.html", {
                    'formRegistro': UserCreationForm,
                    'error': "El nombre de Usuario ya existe"
                })
        return render(request, "registro.html", {
                    'formRegistro': UserCreationForm,
                    'error': "Las contraseñas no coinciden"
                })

@login_required
def tareas(request):
    list_Tareas= Tarea.objects.filter(user=request.user, fecha_Realizada__isnull = True)
    return render(request, "tareas.html",{
        "list_tareas" : list_Tareas
    })

@login_required
def tareasCompletadas( request):
    list_Tareas= Tarea.objects.filter(user=request.user, fecha_Realizada__isnull = False).order_by('-fecha_Realizada')
    return render(request, "tareas_Completadas.html",{
        "list_tareas" : list_Tareas
    })

@login_required
def crear_Tarea(request):
    if request.method == 'GET':
        return render(request, "crear_Tarea.html",{
            'form_tarea' : FormTarea
        })
    else:
        try:
            form = FormTarea(request.POST)
            new_tarea = form.save(commit=False)
            #Agregamos el usuario a la tarea que creamos
            new_tarea.user = request.user
            new_tarea.save()
            return redirect ("tareas")
        except ValueError:
            return render(request, "crear_Tarea.html",{
                'form_tarea' : FormTarea,
                'error': "Por favor envie datos validos"
            })
    
@login_required
def detalle_Tarea(request, id):
    if request.method == 'GET':
        tarea = get_object_or_404(Tarea, pk = id, user = request.user)
        #Para devolver el formulario para editarlo
        form = FormTarea(instance=tarea)
        return render(request, "detalle_Tarea.html",{
            'tarea': tarea,
            'form' : form
        })
    else:
        try:
            #Actualizar la tarea y que solo sea la de dicho usuario
            tarea = get_object_or_404(Tarea, pk = id , user = request.user)
            form = FormTarea(request.POST, instance= tarea)
            form.save()
            return redirect('tareas')
        except ValueError:
            return render(request, "detalle_Tarea.html",{
            'tarea': tarea,
            'form' : form,
            'error' : "Hubo un error actualice de nuevo"
        })
            

@login_required
def tarea_Completada(request, id):
    tarea = get_object_or_404(Tarea, pk = id, user = request.user)
    if request.method == 'POST':
        tarea.fecha_Realizada = timezone.now()
        tarea.save()
        return redirect("tareas")
    

@login_required
def tarea_Eliminada(request, id):
    tarea = get_object_or_404(Tarea, pk = id, user = request.user)
    if request.method == 'POST':
        tarea.delete()
        return redirect("tareas")


@login_required
def cerarSesion(request):
    logout(request)
    return redirect("home")

def iniciarS(request):
    if request.method == 'GET':
        return render(request, "login.html", {
            'formInicioS': AuthenticationForm
        })
    else:
        userA = authenticate(request, username = request.POST['username'],
        password = request.POST['password'])

        if userA is None:
            return render(request, "login.html", {
            'formInicioS': AuthenticationForm,
            'error': "Usuario o contraseña incorrectos"
        })
        else:
        #pasamos un ide de sesion del usuario
            login(request, userA)
            return redirect('tareas')
