from django.shortcuts import render

from .services import cargar_dispositivos,cargar_clientes,cargar_zonas,cargar_categoria

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


def zona_id(request, zona_id):
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
        


def catalogo(request):
    dispositivos = [
    {"nombre": "Medidor inteligente", "estado": "Activo"},
    {"nombre": "Sensor de temperatura", "estado": "Activo"},
    {"nombre": "Climatizador", "estado": "Revisión"},
    ]
    return render(
    request,
    "dispositivos/catalogo.html",
    {"dispositivos": dispositivos},
    )
# dispositivos/urls.py
def inicio(request):
    contexto = {
    "sistema": "EcoEnergy",
    "mensaje": "Monitoreo energético responsable",
    "asignatura": "Programación Back End",
    }
    return render(
    request,
    "dispositivos/inicio.html",
    contexto,
    )

# dispositivos/views.py
def catalogo(request):
    dispositivos = cargar_dispositivos()
    activos = sum(
    1 for item in dispositivos
    if item["estado"] == "Activo"
    )
    contexto = {
    "dispositivos": dispositivos,
    "total": len(dispositivos),
    "total_activos": activos,
    }
    return render(
    request, "dispositivos/catalogo.html", contexto
    )

def zonas(request):
    zones = cargar_zonas()
    dispositivos = cargar_dispositivos()
    categorias = cargar_categoria()
    total_dispositivos = len(dispositivos)
    zona_filtrada = {}



    for z in zones:
        zona_filtrada = [] 
        
        for d in dispositivos:
            if d["id_zona"] == z["id_zona"]:  # Compara el zona_id del dispositivo con el id de la zona
                zona_filtrada.append(d)
        z["dispositivos"] = zona_filtrada
        z["total_dispositivos"] = len(zona_filtrada)

    for d in dispositivos: 
        for c in categorias:
            if c["categoria_id"] == d["categoria_id"]:
                d["categoria_nombre"] = c["nombre"]
                d["categoria_descripcion"] = c["descripcion"]
        
            
    contexto={
        "zonas": zones,
        "dispositivos": total_dispositivos,
    }

    return render(
        request, "dispositivos/zonas.html", contexto
    )
