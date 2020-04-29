from django.shortcuts import render, redirect
from django.views import View
from datetime import datetime
from .models import Especialidade
from .forms import ConsultaForm

# Create your views here.

class Index(View):
    def get(self, request):
        especialidades = Especialidade.objects.all()
        form = ConsultaForm()
        return render(request, 'index.html', {'especialidades': especialidades,
                                              'form': form})

    def post(self, request):
        form = ConsultaForm(request.POST)

        if form.is_valid():
            try:
                datetime.strptime(form.data['data'], "%d/%m/%Y")
                form.save()

            except:
                especialidades = Especialidade.objects.all()
                return render(request, 'index.html', {'especialidades': especialidades,
                                              'form': form,
                                              'erro': 'Formato de data inválido. ex: 01/01/2020'})
                

        especialidades = Especialidade.objects.all()
        return render(request, 'index.html', {'especialidades': especialidades,
                                              'form': form})




def especialidades (request):
    especialidades = Especialidade.objects.all()
    return render(request, 'especialidades.html', {'especialidades': especialidades})


def especialidade_especifica (request):
    return render(request, 'especialidade_especifica.html')
