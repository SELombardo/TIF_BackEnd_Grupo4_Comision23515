from django.urls import path
from autenticacion.views import cerrar_sesion, logear

urlpatterns = [
    path("cerrar_sesion/", cerrar_sesion, name="cerrar_sesion"),
    path("", logear, name="login"),
]
