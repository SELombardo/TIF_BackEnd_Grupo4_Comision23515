from django.contrib import admin
from core.models import Alumno

class AlumnoAdmin(admin.ModelAdmin):
    list_display = (
        "nombre",
        "apellido",
        "dni",
        "create",
    )
    search_fields = (
        "nombre",
        "apellido",
        "dni",
    )

admin.site.register(Alumno, AlumnoAdmin)
