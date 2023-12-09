"""
URL configuration for CodoPowerGym project.

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
from django.urls import path, include
from core import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("autenticacion.urls")),
    path("home", views.home, name="home"),
    path("actividades", views.actividades, name="actividades"),
    path("contacto", views.contacto, name="contacto"),
    path("sobre_nosotros", views.sobre_nosotros, name="sobre_nosotros"),
    path("galeria", views.galeria, name="galeria"),
    path("registro", views.registrar_alumno, name="registrar_alumno"),
    path("alumnos_registrados", views.alumnos, name="alumnos"),
    path("eliminar_alumno/<int:alumno>", views.eliminar_alumno, name="eliminar_alumno"),
]