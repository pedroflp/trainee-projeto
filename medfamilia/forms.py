from django import forms
from .models import Consulta

class ConsultaForm (forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['nome', 'email', 'telefone',
                  'especialidade', 'data', 'turno', 'info_adicionais']
                  
    def __init__(self, *args, **kwargs):
        super(ConsultaForm, self).__init__(*args, **kwargs)
        
        self.fields['nome'].widget.attrs = {'id': "nome-input-form-agendamento",
                                            'class': "nome-input-form-agendamento",
                                            'placeholder': "Digite seu Nome"}
        
        self.fields['email'].widget.attrs = {'id': "email-input-form-agendamento",
                                            'class': "email-input-form-agendamento",
                                            'placeholder': "Digite seu email"}

        self.fields['telefone'].widget.attrs = {'id': "telefone-input-form-agendamento",
                                                'class': "telefone-input-form-agendamento",
                                                'placeholder': "Digite seu telefone"}

        self.fields['especialidade'].widget.attrs = {'id':"especialidade-select",
                                                     'class':"especialidade-select"}

        self.fields['data'].widget.attrs = {'id':'id_data'}
        self.fields['data'].widget = forms.HiddenInput()

        self.fields['turno'].widget.attrs = {'id':"turno-select",
                                              'class':"turno-select"}

        self.fields['info_adicionais'].widget.attrs = {'id': "mensagem-input-form-agendamento",
                                                    'class': "mensagem-input-form-agendamento",
                                                    'placeholder': "Digite seu mensagem",
                                                    'cols':"50", 'rows':"5"}