from django.shortcuts import render, redirect
from django.views import View
from datetime import datetime
import re
from .models import Especialidade
from .forms import ConsultaForm

# Create your views here.

class Index(View):
    #passa o formulário de consulta para a pagina inicial
    def get(self, request):
        especialidades = Especialidade.objects.all()
        form = ConsultaForm()
        return render(request, 'index.html', {'especialidades': especialidades,
                                              'form': form})

    #realiza o cadastro da consulta no banco de dado se tudo estiver correto
    def post(self, request):
        form = ConsultaForm(request.POST)
        especialidades = Especialidade.objects.all()

        if form.is_valid():
            try:
                datetime.strptime(form.data['data'], "%d/%m/%Y")

            except:
                return render(request, 'index.html', {'especialidades': especialidades,
                                              'form': form,
                                              'erro': 'Formato de data inválido. ex: 01/01/2020'})
                

            expressao = re.compile(r'\(\d{2}\) \d{4,5}-\d{4}\Z')

            if expressao.match(form.data['telefone']):
                consulta = form.save(commit=False)
                consulta.respondida = False
                consulta.save()

            else:
                return render(request, 'index.html', {'especialidades': especialidades,
                                              'form': form,
                                              'erro': 'Formato de telefone inválido. ex: (01)98765-4321 ou (01)8765-4321'})

        return redirect('index')


def especialidades (request):
    especialidades = Especialidade.objects.all()
    return render(request, 'especialidades.html', {'especialidades': especialidades})


def especialidade_especifica (request):
    return render(request, 'especialidade_especifica.html')
