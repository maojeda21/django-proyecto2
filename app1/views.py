from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def holaMundo(request):
    return HttpResponse("hola mundillo del orto!")

def vader(request):
    return HttpResponse("Soy Vader")

def saludo(request,nombre):
    return HttpResponse(f"hola {nombre}")

