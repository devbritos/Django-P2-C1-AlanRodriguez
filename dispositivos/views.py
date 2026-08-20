from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def inicio(request):
    return HttpResponse(
    "<h1>EcoEnergy</h1>"
    "<p>Back End en funcionamiento</p>"
    )


def dispositivos_zona(request, zona_id):
    if zona_id != 3:
        return HttpResponse(
        "Zona no encontrada", status=404)
        
    return HttpResponse(
    f"Dispositivos de la zona {zona_id}"
    )

zonas = {"zona_1": 1,
         "zona_2": 2,
         "zona_3":3}


def zona(request, zona_id):
    if zona_id == 1:
        return HttpResponse(
            "Estas En Brasil"
        )
    elif zona_id == 2:
        return HttpResponse(
            "Estas En Chile"
        )
    elif zona_id == 3:
        return HttpResponse(
            "Estas En Argentina"
        )
    else:
        return HttpResponse(
        "Zona no encontrada", status=404)
        

    

