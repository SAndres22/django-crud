"""
URL configuration for djangoCrud project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

#Importar las urls de la app tarea
from tarea import views

urlpatterns = [

    #el path es como aparece en la ruta
    path('admin/', admin.site.urls),
    #ruta home
    path('', views.home, name="home"),
    #ruta de form registro
    path('signup/', views.registro, name="registro"),
    #ruta de tareas luego de iniciar sesion
    path('tareas/', views.tareas, name ="tareas"),
    path('list_tareas_Completas/', views.tareasCompletadas, name="tareasCompletadas"),
    path('cerarS/', views.cerarSesion, name="Cerrar_Sesion"),
    path("login/", views.iniciarS, name= "iniciar_Sesion"),
    path("crear/tarea/", views.crear_Tarea, name="crear_tareas"),
    path("tareas/detalle/<int:id>/", views.detalle_Tarea, name="detalle_tarea"),
    path("tareas/completas/<int:id>/", views.tarea_Completada, name="tarea_Completada"),
    path("tareas/eliminar/<int:id>/", views.tarea_Eliminada, name= "tarea_Eliminada")
]
