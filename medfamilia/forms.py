from django import forms
from .models import Consulta

class ConsultaForm (forms.ModelForm):
    class Meta:
        model = Consulta
        fields = ['nome', 'email', 'telefone', 
                  'especialidade', 'data', 'turno', 'info_adicionais']

    def __init__(self, *args, **kwargs):
        super(ConsultaForm, self).__init__(*args, **kwargs)

        self.fields['data'].widget.attrs = {'placeholder': 'ex: 27/04/2020',
                                            'id': 'id_data'}
        self.fields['data'].widget = forms.HiddenInput()