from django.shortcuts import render, redirect
from .forms import CitaForm
from .models import Servicio, Barbero


# Create your views here.
def reservar(request):
    if request.method == "POST":
        form = CitaForm(request.POST)
        # Verifica que este todo correcto en el form
        if form.is_valid():
            form.save()
            return redirect("/reservar/exito/")
        else:
            print(form.errors.as_json())

    else:
        form = CitaForm()

    return render(request, "citas/reservar.html", {"form": form})


def exito(request):
    return render(request, "exito.html")


def home(request):
    return render(request, 'index.html')


def contacto(request):
    return render(request, 'contacto.html')


def servicios(request):
    servicios = Servicio.objects.all()
    return render(
        request,
        'servicios.html',
        {
            "servicios": servicios
        })


def mostrar_barberos(request):
    barberos = Barbero.objects.all()
    return render(request, 'barberos.html',
                  {
                      "barberos": barberos
                  })
