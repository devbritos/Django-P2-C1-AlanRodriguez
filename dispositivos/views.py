from django.shortcuts import render

from .services import cargar_dispositivos,cargar_clientes,cargar_zonas,cargar_categoria

from django.http import Http404
# Create your views here.
from django.http import HttpResponse
def inicio(request):
    return HttpResponse(
    "<h1>EcoEnergy</h1>"
    "<p>Back End en funcionamiento</p>"
    )




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
        suma_consumo = 0 

        for d in dispositivos:# Compara el zona_id del dispositivo con el id de la zona
            if d["id_zona"] == z["id_zona"]:
                zona_filtrada.append(d)
                suma_consumo += d["consumo_kwh"]

        z["dispositivos"] = zona_filtrada
        z["total_dispositivos"] = len(zona_filtrada)
        z["suma_consumo"] = round(suma_consumo, 2)
        if z["suma_consumo"] > z["limite_kwh"]:
            z["estado"] = "ALERTA"
        else:
            z["estado"] = "NORMAL"


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
        request, "dispositivos/zona_consumo.html", contexto
    )
def dispositivos_zona(request, id_zona):
    zones = cargar_zonas()
    dispositivos = cargar_dispositivos()
    categorias = cargar_categoria()

    #Buscar la zona solicitada por su ID
    zona_encontrada = None
    for z in zones:
        if int(z["id_zona"]) == int(id_zona):
            zona_encontrada = z
            break

    if not zona_encontrada:
        raise Http404("La zona solicitada no existe")

  
    dispositivos_zona_lista = []
    suma_consumo = 0

    for d in dispositivos:
        if int(d["id_zona"]) == int(id_zona):
            # Buscar nombre de categoría
            for c in categorias:
                if int(c["categoria_id"]) == int(d["categoria_id"]):
                    d["categoria_nombre"] = c["nombre"]
            
            dispositivos_zona_lista.append(d)
            suma_consumo += float(d["consumo_kwh"])

    zona_encontrada["dispositivos"] = dispositivos_zona_lista
    zona_encontrada["total_dispositivos"] = len(dispositivos_zona_lista)
    zona_encontrada["suma_consumo"] = round(suma_consumo, 2)

    # Evaluar alerta de la zona
    limite = float(zona_encontrada.get("limite_kwh", zona_encontrada.get("limite", 0)))
    if zona_encontrada["suma_consumo"] > limite:
        zona_encontrada["estado"] = "ALERTA"
    else:
        zona_encontrada["estado"] = "NORMAL"

    return render(request, "por_zona.html", {"zona": zona_encontrada})