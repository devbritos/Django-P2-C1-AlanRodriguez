7. Verificación individual escrita 
Responda después del cierre técnico. Puede revisar el código entregado, pero no modificarlo. 
Pregunta 1 
Explique el recorrido de una solicitud desde /resumen-zonas/ hasta la respuesta HTML. Mencione la 
URL, la View, el contexto y el Template. 
1. Hacer los services
Sin services no podriamos extraer los datos del json

2. Crear la views
importando las funciones que creamos en los services podemos
agregar logica haciendo funciones personalizadas como lo que hicimos con las zonas
y la suma de CADA dispositivo por zona

3. Despues pasamos a las urls aqui creando la ruta 
haciendo referencia a la view creada anteriormente

4. Finalmente tenemos que programar el template que queramos mostrar los datos
idealmente esto es bueno porque mediante vaya creciendo lo datos este mismo se irá 
incrementando sin romper la pagina web.

Pregunta 2 
Indique el archivo y la parte de su código donde cuenta dispositivos y suma consumo_kwh por zona. 
Explique brevemente cómo funciona. 

Primero que todo hay que hacer un BUCLE FOR en zonas porque es donde agruparemos todo
Ej : for z in zonas

Despues dentro de este for tenemos que hacer otro con los dispositivos
como estamos trabajando con diccionarios vamos a tener que hacer referencia
a las keys y para esto usaremos un condicional para detectar a que zona pertenece c/u de los dispositivos
d_encontrados = []
for d in dispositivos:
    if d["id_zona"] == z["id_zona"]:
        d_encontrados.append(d)
        suma_contenido += d["consumo_kwh"]
Previamente tenemos que crear una variable valor: 0 que funcionara como contador
"suma_contenido = 0"

Como podemos ver en cada iteracion que se vincule a la zona id se irá sumando el consumo de CADA DISPOSITIVO POR ITERACION.


Pregunta 3 
Indique la condición utilizada para definir el estado de una zona y explique qué ocurre cuando una zona 
no tiene dispositivos. 
