from django import forms
from .models import Paciente, Arquivo

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nome', 'sexo', 'estado_Civil', 'data_de_nascimento', 'cpf', 'telefone', 'endereco', 'email', 'filhos', 'filhos_Quantidade', 'atendimento', 'atendimento_Tipo_Tempo_Motivo', 'religião', 'escolaridade', 'trabalha_no_momento', 'profissão', 'toma_Algum_Medicamento', 'qual_Medicamento', 'Disponibilidade', 'rede_de_apoio', 'contato_de_emergência', 'motivo_e_objetivo', 'observações' ]

class ArquivoForm(forms.ModelForm):
    class Meta:
        model = Arquivo
        fields = ['arquivo']
