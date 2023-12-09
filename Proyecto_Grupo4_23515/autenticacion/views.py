from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

def cerrar_sesion(request):
    logout(request)
    return redirect("/")

def logear(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            usuario = authenticate(username=username, password=password)
            if usuario is not None:
                login(request, usuario)
                return redirect("home")
            else:
                messages.error(request, "Usuario no valido")
        else:
            messages.error(request, "Informacion incorrecta")

    form = AuthenticationForm()
    return render(request, "login.html", {"form": form})
