from django import forms
from .models import Consulta

class ConsultaForm (forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['nome', 'email', 'telefone', 
                  'especialidade', 'data', 'turno', 'info_adicionais']

    def __init__(self, *args, **kwargs):
        super(ConsultaForm, self).__init__(*args, **kwargs)

        self.fields['data'].widget.attrs = {'class':"form-control",
                                            'id':"exemplo",
                                            'placeholder':"Selecione a Data",
                                            'min':"1", 'max':"31"}