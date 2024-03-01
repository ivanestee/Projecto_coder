from django.http import HttpResponse
from django.template import Template, Context
from django.template import loader
import os
import datetime

def saludo(request):
    return HttpResponse("Bienvenido al blog")

def probandoTemplate(request):
    # Obtén la ruta del archivo de plantilla de manera dinámica
    # Esto asume que el archivo de plantilla está en la misma carpeta que este script
    ruta_plantilla = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'plantillas', 'templante1.html')

    # Abre el archivo de plantilla
    with open(ruta_plantilla, 'r') as miHtml:
        contenido_html = miHtml.read()

    # Compila la plantilla
    plantilla = Template(contenido_html)

    # Define el contexto
    miContexto = Context({})  # Puedes agregar variables al contexto si lo necesitas

    # Renderiza la plantilla con el contexto
    documento = plantilla.render(miContexto)

    # Devuelve la respuesta HTTP con el contenido renderizado de la plantilla
    return HttpResponse(documento)

    documento = plantilla.render(diccionario)
    return HttpResponse(documento)