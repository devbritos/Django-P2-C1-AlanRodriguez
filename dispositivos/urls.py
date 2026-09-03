from django.urls import path
from . import views
app_name = "dispositivos"
urlpatterns = [
path("", views.inicio, name="inicio"),
path("zona/<int:id_zona>",
     views.dispositivos_zona,name="por_zona"),
path("inicio/",views.inicio,name ="inicio"),
path("dispositivos/", views.catalogo, name="catalogo"),
path("zona_consumo/",views.zonas,name = "zona_consumo")
]




