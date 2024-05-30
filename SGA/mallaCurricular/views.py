from django.shortcuts import render, redirect

from mallaCurricular.models import Facultad, Carrera, Ciclo, Asignatura
from .forms import FacultadForm, CarreraForm


def home(request):
    return render(request, 'index.html')

def facultades(request):
    facultades = Facultad.objects.all()
    context = {
        'facultades': facultades
    }
    return render(request, 'facultad.html', context)

def carreras(request):
    carreras = Carrera.objects.all()
    context = {
        'carreras': carreras
    }
    return render(request, 'carrera.html', context)

def ciclo(request):
    ciclos = Ciclo.objects.all()
    context = {
        'ciclos': ciclos
    }
    return render(request, 'ciclo.html', context)

def asignaturas(request):
    asignaturas = Asignatura.objects.all()
    context = {
        'asignaturas': asignaturas
    }
    return render(request, 'asignatura.html', context)

def ciclo(request,id):
    ciclo = Ciclo.objects.get(id=id)
    context = {
        'ciclo': ciclo
    }
    return render(request, 'ciclodetail.html', context)

def asignatura(request, id):
    asignatura = Asignatura.objects.get(id=id)
    context = {
        'asignatura': asignatura
    }
    return render(request, 'asignaturadetail.html', context)


def carrera(request, id):
    carrera = Carrera.objects.get(id=id)
    context = {
        'carrera': carrera
    }
    return render(request, 'carreradetail.html', context)

def agregar_facultad(request):
    if request.method == 'POST':
        form = FacultadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('facultades')
    else:
        form = FacultadForm()
        context = {
            'form': form
        }
        return render(request, 'addFacultad.html',context)

def agregar_carrera(request):
    if request.method == 'POST':
        form = CarreraForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('carreras')
    else:
        form = CarreraForm()
        context = {
            'form': form
        }
        return render(request, 'addCarrera.html',context)