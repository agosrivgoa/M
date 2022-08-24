from django.shortcuts import render
from .models import Familiar

def home(request):
    return render(request, 'home.html')

def crear_familiar(request):
    familiar1  = Familiar.objects.create(
        nombre ="Lorena", 
        edad = "39", 
        fecha_de_nacimiento="1982-09-16",
        dni = "29585637",
        numero_de_telefono = "2974624398",
        nacionalidad = "argentina",
        parentesco = "madre",
         )
    familiar2  = Familiar.objects.create(
        nombre ="Miguel", 
        edad = "44", 
        fecha_de_nacimiento="1978-01-04",
        dni = "26234987",
        numero_de_telefono = "2974651243",
        nacionalidad = "argentina",
        parentesco = "padre",
         )
    familiar3  = Familiar.objects.create(
        nombre ="Thiago", 
        edad = "9", 
        fecha_de_nacimiento="2013-01-29",
        dni = "52123095",
        numero_de_telefono = "2974439805",
        nacionalidad = "argentina",
        parentesco = "hermano",
         )
    familiar4  = Familiar.objects.create(
        nombre ="Elena", 
        edad = "65", 
        fecha_de_nacimiento="1957-01-05",
        dni = "18889345",
        numero_de_telefono = "297540965",
        nacionalidad = "argentina",
        parentesco = "abuela",
         )
    familiar5  = Familiar.objects.create(
        nombre ="Reinaldo", 
        edad = "65", 
        fecha_de_nacimiento="1957-05-22",
        dni = "18345098",
        numero_de_telefono = "2975230965",
        nacionalidad = "argentina",
        parentesco = "abuelo",
         )
          
    contexto = { 'madre': familiar1, 'padre': familiar2, 'hermano': familiar3, 'abuela': familiar4, 'abuelo': familiar5}

    return render(request, "home.html", contexto)

def ver_familiar(request):
    familia = Familiar.objects.all()
    contexto = {'familia': familia}
    return render(request, "home.html", contexto)