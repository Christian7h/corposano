from django.shortcuts import render
from django.http import HttpResponse

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