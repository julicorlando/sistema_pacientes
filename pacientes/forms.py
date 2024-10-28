from django import forms
from .models import Paciente, Arquivo

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nome', 'sexo', 'data_nascimento', 'cpf', 'telefone', 'endereco', 'email']

class ArquivoForm(forms.ModelForm):
    class Meta:
        model = Arquivo
        fields = ['arquivo']
