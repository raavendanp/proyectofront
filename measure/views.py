from django.shortcuts import render, HttpResponse
import requests

# Create your views here.
def home(request):
    return render(request, "measure/home.html")

def measure(request):
    # Verifica si hay un parametro Longitud en la petición GET
    if 'Longitud' and 'Codigo' and 'Latitud' and 'Producto' and 'Area' in request.GET:
        Longitud = request.GET['Longitud']
        Latitud = request.GET['Latitud']
        Codigo = request.GET['Codigo']
        Producto = request.GET['Producto']
        Area = request.GET['Area']
        # Verifica si el Longitud no esta vacio
        if Longitud and Codigo and Latitud and Area:
            # Crea el json para realizar la petición POST al Web Service
            args = {'Codigo': Codigo, 'Longitud': Longitud, 'Latitud': Latitud, 'Producto':Producto, 'Area': Area}
            response = requests.post('http://127.0.0.1:8000/measures/', args)
            # Convierte la respuesta en JSON
            measure_json = response.json()

    # Realiza una petición GET al Web Services
    response = requests.get('http://127.0.0.1:8000/measures/')
    # Convierte la respuesta en JSON
    measures = response.json()
    # Rederiza la respuesta en el template measure
    return render(request, "measure/measure.html", {'measures': measures})