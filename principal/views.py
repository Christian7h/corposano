from logging import DEBUG
from os import path
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseServerError
from django.urls import URLPattern

def server_error(request):
    raise Exception("Server Error Test")
if DEBUG:
    URLPattern += [path('500/', server_error)]

# Create your views here.
def index(request):
    # Lógica para recuperar y mostrar contenido relacionado con la salud
    return render(request, 'inicio.html')

def servicios(request):
    # Lógica para recuperar y mostrar los servicios ofrecidos
    return render(request, 'servicios.html')

def blog(request):
    # Lógica para recuperar y mostrar artículos del blog
    return render(request, 'blog.html')

def contacto(request):
    # Lógica para mostrar información de contacto y procesar el formulario
    return render(request, 'contacto.html')

def agendar_cita(request):
    return render(request, 'agendar_cita.html')

