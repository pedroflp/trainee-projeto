from django.shortcuts import render, redirect, get_object_or_404
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
        fragmento = "#form"

        if form.is_valid():
            try:
                datetime.strptime(form.data['data'], "%d/%m/%Y")

            except:
                return render(request, 'index.html', {'especialidades': especialidades,
                                              'form': form,
                                              'erro': 'Formato de data inválido. ex: 01/01/2020',
                                              'fragmento': fragmento})
                

            expressaoSemEspaco = re.compile(r'\(\d{2}\)\d{4,5}-\d{4}\Z')
            expressaoComEspaco = re.compile(r'\(\d{2}\) \d{4,5}-\d{4}\Z')

            if expressaoSemEspaco.match(form.data['telefone']) or expressaoComEspaco.match(form.data['telefone']):
                consulta = form.save(commit=False)
                consulta.respondida = False
                consulta.save()

                return redirect('confirmacao_consulta', nome=consulta.nome)

            else:
                return render(request, 'index.html', {'especialidades': especialidades,
                                              'form': form,
                                              'erro': 'Formato de telefone inválido. ex: (01) 98765-4321 ou (01) 8765-4321',
                                              'fragmento':fragmento})

        return render(request, 'index.html', {'especialidades': especialidades,
                                              'form': form,
                                              'fragmento':fragmento})


def especialidades (request):
    especialidades = Especialidade.objects.all()
    return render(request, 'especialidades.html', {'especialidades': especialidades})


class especialidade_especifica (View):
    def get (self, request, id):
        especialidade = get_object_or_404(Especialidade, pk=id)

        #initial define valores pré definidos para os campos que podem ser
        #alterados
        form = ConsultaForm(initial = {'especialidade': id})

        return render(request, 'especialidade_especifica.html', 
                        {'especialidade': especialidade, 'form': form})


    def post(self, request, id):
        especialidade = get_object_or_404(Especialidade, pk=id)
        form = ConsultaForm(request.POST)
        fragmento = "#form"

        if form.is_valid():
            try:
                datetime.strptime(form.data['data'], "%d/%m/%Y")

            except:
                return render(request, 'especialidade_especifica.html', {'especialidade': especialidade,
                                              'form': form,
                                              'erro': 'Formato de data inválido. ex: 01/01/2020',
                                              'fragmento': fragmento})
                

            expressaoSemEspaco = re.compile(r'\(\d{2}\)\d{4,5}-\d{4}\Z')
            expressaoComEspaco = re.compile(r'\(\d{2}\) \d{4,5}-\d{4}\Z')

            if expressaoSemEspaco.match(form.data['telefone']) or expressaoComEspaco.match(form.data['telefone']):
                consulta = form.save(commit=False)
                consulta.respondida = False
                consulta.save()

                return redirect('confirmacao_consulta', nome=consulta.nome)

            else:
                return render(request, 'especialidade_especifica.html', {'especialidade': especialidade,
                                              'form': form,
                                              'erro': 'Formato de telefone inválido. ex: (01) 98765-4321 ou (01) 8765-4321',
                                              'fragmento':fragmento})

        return render(request, 'especialidade_especifica.html', {'especialidade': especialidade,
                                              'form': form,
                                              'fragmento':fragmento})


def confirmacao_consulta (request, nome):
    return render (request, 'confirmacao_consulta.html', {'nome':nome})
