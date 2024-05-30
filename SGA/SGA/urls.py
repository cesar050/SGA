"""
URL configuration for SGA project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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

from mallaCurricular.views import home, facultades, carreras, carrera, agregar_facultad, agregar_carrera, ciclo, \
    asignaturas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('facultades/', facultades, name='facultades'),
    path('carreras/', carreras, name='carreras'),
    path('ciclos/', ciclo, name='ciclos'),
    path('asignaturas/', asignaturas, name='asignaturas'),
    path('carreras/<int:id>/', carrera, name='carrera'),
    path('ciclos/<int:id>/', ciclo, name='ciclo'),
    path('facultades/add/', agregar_facultad, name='addFacultad'),
    path('carreras/add/', agregar_carrera, name='addCarrera')
]
