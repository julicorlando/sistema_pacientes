# Generated by Django 5.1.1 on 2024-10-28 14:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('telefone', models.CharField(max_length=15)),
                ('endereco', models.CharField(max_length=255)),
                ('data_nascimento', models.DateField()),
                ('cpf', models.CharField(max_length=11, unique=True)),
                ('sexo', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino')], max_length=10)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Arquivo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('arquivo', models.FileField(upload_to='pacientes/pdfs/')),
                ('data_upload', models.DateTimeField(auto_now_add=True)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='arquivos', to='pacientes.paciente')),
            ],
        ),
    ]
