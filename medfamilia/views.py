from django.shortcuts import render, redirect

# Create your views here.

def index (request):
    return render(request, 'index.html')


def especialidades (request):
    return render(request, 'especialidades.html')


def especialidade_especifica (request):
    return render(request, 'especialidade_especifica.html')
