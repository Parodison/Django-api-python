from django.shortcuts import render, redirect
from .models import Gestion
from django.http.response import JsonResponse
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def showIndex(request):
    return render(request,'index.html')

def createUser(request):
    return render(request,'create_user.html')

def save_users(request):
    usuarios = Gestion(nombre=request.POST['nombre'],
                           email=request.POST['email'],
                           telefono=request.POST['telefono'],
                           cedula=request.POST['cedula'],
                           password=request.POST['password'],)
    usuarios.save()
    return redirect('/')

def tables(request):
    return render(request, 'tables.html')

def list_table(request):
    tabla = list(Gestion.objects.values())
    datos = {'tabla':tabla}
    return JsonResponse(datos)