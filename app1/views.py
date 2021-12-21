from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# Si queremos mostrar un archivo HTML lo hacemos mediante un RENDER.
def holaMundo(request):
    #return HttpResponse("hola mundillo del orto!")
    return render(request, 'app1/index.html') # Render recibe dos parametros, 1ro la request del usuario, y 2do el archivo HTML.

#def vader(request):
#    return HttpResponse("Soy Vader")

# Ruta dinámica
#def saludo(request,nombre):
#    return HttpResponse(f"Hola {nombre}")

def saludo(request,nombre):
    # Para poder pasar una variable a nuestro HTML lo hacemos mediante un contexto.
    # Un contexto envia/pasa una variables a nuestro HTML mediante Diccionarios {'llave':valor}
    context = {'name':nombre}
    return render(request, 'app1/saludo.html', context) # Aparte de enviar la request del usuario e indicarle el archivo HTML debemos pasar el context.
