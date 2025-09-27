from django import forms
from django.shortcuts import redirect
from .models import Evolucao, Paciente, Arquivo, Pagamento
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nome', 'sexo', 'estado_Civil', 'data_nascimento', 'cpf', 'telefone', 'telefone_alternativo', 'endereco', 'email', 'possui_filhos', 'filhos_Quantidade', 'atendimento_anterior', 'atendimento_atual', 'atendimento_Tipo_Tempo_Motivo', 'escolaridade', 'trabalha_no_momento', 'profissão', 'e_menor_de_idade', 'responsavel_nome', 'responsavel_cpf', 'responsavel_endereco', 'responsavel_contato', 'responsavel_parentesco', 'toma_Algum_Medicamento', 'qual_Medicamento', 'Disponibilidade', 'rede_de_apoio', 'contato_de_emergência', 'motivo_e_objetivo', 'observações' ]

class ArquivoForm(forms.ModelForm):
    class Meta:
        model = Arquivo
        fields = ['arquivo']  # Certifique-se de que o campo 'arquivo' é um FileField no modelo
        
class NovoUsuarioForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NovoUsuarioForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class PagamentoForm(forms.ModelForm):
    class Meta:
        model = Pagamento
        fields = ['valor', 'forma_pagamento', 'modalidade_convenio', 'recibo_emitido']  # Updated to include new fields



class EvolucaoForm(forms.ModelForm):
    class Meta:
        model = Evolucao
        fields = ['conteudo']  # Campos que deseja permitir a edição