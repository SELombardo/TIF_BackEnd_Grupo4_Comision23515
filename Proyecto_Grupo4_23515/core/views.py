from django.shortcuts import render, redirect
from core.form import AlumnoForm
from core.models import Alumno

def home(request):
    if not request.user.is_authenticated:
        return redirect('/')
    return render(request, "index.html")


def actividades(request):
    if not request.user.is_authenticated:
        return redirect('/')
    return render(request, "actividades.html")


def contacto(request):
    if not request.user.is_authenticated:
        return redirect('/')
    return render(request, "contacto.html")


def galeria(request):
    if not request.user.is_authenticated:
        return redirect('/')
    return render(request, "galeria.html")


def sobre_nosotros(request):
    if not request.user.is_authenticated:
        return redirect('/')
    return render(request, "sobre_nosotros.html")


# LISTAR
def alumnos(request):
    if not request.user.is_authenticated:
        return redirect('/')
    alumnos = Alumno.objects.all()
    return render(request, "alumnos_registrados.html", {"alumnos": alumnos})


# REGISTRAR
def registrar_alumno(request):
    if not request.user.is_authenticated:
        return redirect('/')
    valid = False
    form = AlumnoForm()
    alumnos = Alumno.objects.all()

    if request.method == "POST":
        form = AlumnoForm(data=request.POST)
        print(form)
        if form.is_valid():
            valid = True
            form.save()
            form = AlumnoForm()
            return render(
                request,
                "alumnos_registrados.html",
                {"valid": valid, "alumnos": alumnos},
            )
        else:
            return render(request, "registro.html", {"form": form, "valid": valid})

    return render(
        request,
        "registro.html",
        {"form": form, "alumnos": alumnos, "valid": valid},
    )

# ELIMINAR
def eliminar_alumno(request, alumno):
    if not request.user.is_authenticated:
        return redirect('/')
    eliminar_alumno = Alumno.objects.get(id=alumno)
    eliminar_alumno.delete()

    return redirect("alumnos")
