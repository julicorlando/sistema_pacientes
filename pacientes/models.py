from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=255)
    data_nascimento = models.DateField(null=True, blank=True)
    cpf = models.CharField(max_length=11, unique=True)
    sexo = models.CharField(max_length=10, choices=[('Masc', 'Masculino'), ('Fem', 'Feminino'), ('O', 'Outro')])
    email = models.EmailField()
    estado_Civil = models.CharField(max_length=255, choices=[('Não Informado', 'Não Informado'), ('Casado(a)', 'Casado(a)'), ('Solteiro(a)', 'Solteiro(a)'), ('Divorciado(a)', 'Divorciado(a)'), ('Viúvo(a)', 'Viúvo(a)'), ('Não se aplica', 'Não se aplica')])
    telefone_alternativo = models.CharField(max_length=15, blank=True, null=True)
    possui_filhos = models.CharField(max_length=10, choices=[('Sim', 'Sim'), ('Não', 'Não')])
    filhos_Quantidade = models.CharField(max_length=10, blank=True, null=True)
    atendimento_anterior = models.CharField(max_length=10, choices=[('Sim', 'Sim'), ('Não', 'Não')], verbose_name="Já fez psicoterapia anteriormente?")
    atendimento_atual = models.CharField(max_length=500, blank=True, null=True, verbose_name="Detalhes do atendimento atual")
    atendimento_Tipo_Tempo_Motivo = models.CharField(max_length=500, verbose_name="Tipo, tempo e motivo do atendimento anterior")
    # Removed religião field as requested
    escolaridade = models.CharField(max_length=255, choices=[('Sem escolaridade', 'Sem escolaridade'), ('Fundamental', 'Fundamental'), ('Médio', 'Médio'), ('Superior Completo', 'Superior Completo'), ('Superior incompleto', 'Superior incompleto'), ('Pós-Grauação', 'Pós-Graduação'), ('Mestrado', 'Mestrado'), ('Dotourado', 'Dotourado')])
    trabalha_no_momento = models.CharField(max_length=10, choices=[('Sim', 'Sim'), ('Não', 'Não')])
    profissão = models.CharField(max_length=50)
    # Minor/Guardian fields
    e_menor_de_idade = models.CharField(max_length=10, choices=[('Sim', 'Sim'), ('Não', 'Não')], default='Não', verbose_name="É menor de idade ou tutelado?")
    responsavel_nome = models.CharField(max_length=100, blank=True, null=True, verbose_name="Nome do responsável")
    responsavel_cpf = models.CharField(max_length=11, blank=True, null=True, verbose_name="CPF do responsável")
    responsavel_endereco = models.CharField(max_length=255, blank=True, null=True, verbose_name="Endereço do responsável")
    responsavel_contato = models.CharField(max_length=15, blank=True, null=True, verbose_name="Contato do responsável")
    responsavel_parentesco = models.CharField(max_length=50, blank=True, null=True, verbose_name="Grau de parentesco/relação")
    toma_Algum_Medicamento =models.CharField(max_length=10, choices=[('Sim', 'Sim'), ('Não', 'Não')])
    qual_Medicamento =  models.CharField(max_length=100, blank=True, null=True)
    Disponibilidade = models.CharField(max_length=100)
    rede_de_apoio = models.CharField(max_length=255, blank=True, null=True, help_text="Descreva sua rede de apoio (família, amigos, etc.) - Campo opcional")
    contato_de_emergência = models.CharField(max_length=100)
    motivo_e_objetivo = models.CharField(max_length=500, verbose_name="Motivo e objetivo do atendimento")
    observações = models.CharField(max_length=1000, blank=True, null=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE, related_name='pacientes')
    
    def __str__(self):
        return self.nome
    
class Pagamento(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='pagamentos')    
    data_pagamento = models.DateField(auto_now_add=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)  
    forma_pagamento = models.CharField(max_length=20, choices=[
        ('Pix', 'Pix'),
        ('Dinheiro', 'Dinheiro'),
        ('Cartão de Crédito', 'Cartão de Crédito'),
        ('Cartão de Débito', 'Cartão de Débito'),
        ('Convênio', 'Convênio/Clínica'),
    ])
    modalidade_convenio = models.CharField(max_length=100, blank=True, null=True, verbose_name="Modalidade do convênio/clínica")
    recibo_emitido = models.CharField(max_length=10, choices=[('Sim', 'Sim'), ('Não', 'Não')], default='Não', verbose_name="Recibo emitido?")

    def __str__(self):
        return f'{self.paciente.nome} - {self.valor} - {self.data_pagamento}'

class Arquivo(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='arquivos')
    arquivo = models.FileField(upload_to='arquivos/')
    data_upload = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Arquivo de {self.paciente.nome}"

class Evolucao(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    conteudo = models.TextField()
    data = models.DateTimeField(default=timezone.now)