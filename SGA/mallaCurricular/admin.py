from django.contrib import admin
from mallaCurricular.models import *

admin.site.register(Facultad)
admin.site.register(Carrera)
admin.site.register(Ciclo)

@admin.register(Asignatura) # Decorador
class AsignaturaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'codigo', 'aa', 'acd', 'ape', 'ciclo')
    search_fields = ('nombre', 'codigo',)
    list_filter = ('ciclo', 'ciclo__carrera', 'ciclo__carrera__facultad')
    list_per_page = 10
    ordering = ('ciclo', 'nombre')
    fieldsets = (
        ('Información de la asignatura', {
            'fields': ('nombre', 'codigo', 'aa', 'acd', 'ape', 'ciclo')
        }),
    )




