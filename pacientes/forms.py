from django import forms
from .models import Paciente, Arquivo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nome', 'sexo', 'estado_Civil', 'data_de_nascimento', 'cpf', 'telefone', 'endereco', 'email', 'filhos', 'filhos_Quantidade', 'atendimento', 'atendimento_Tipo_Tempo_Motivo', 'religião', 'escolaridade', 'trabalha_no_momento', 'profissão', 'toma_Algum_Medicamento', 'qual_Medicamento', 'Disponibilidade', 'rede_de_apoio', 'contato_de_emergência', 'motivo_e_objetivo', 'observações' ]

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