from django.db import models

class Paciente(models.Model):
    nome = models.CharField(max_length=100)
    telefone = models.CharField(max_length=15)
    endereco = models.CharField(max_length=255)
    data_nascimento = models.DateField()
    cpf = models.CharField(max_length=11, unique=True)
    sexo = models.CharField(max_length=10, choices=[('M', 'Masculino'), ('F', 'Feminino')])
    email = models.EmailField()

    def __str__(self):
        return self.nome

class Arquivo(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='arquivos')
    arquivo = models.FileField(upload_to='pacientes/pdfs/')
    data_upload = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Arquivo de {self.paciente.nome}"
