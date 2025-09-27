# Generated manually to update patient system

from django.db import migrations, models
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0011_rename_data_de_nascimento_paciente_data_nascimento'),
    ]

    operations = [
        # Add new fields
        migrations.AddField(
            model_name='paciente',
            name='telefone_alternativo',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='paciente',
            name='possui_filhos',
            field=models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], default='Não', max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paciente',
            name='atendimento_anterior',
            field=models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], default='Não', max_length=10, verbose_name='Já fez psicoterapia anteriormente?'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='paciente',
            name='atendimento_atual',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Detalhes do atendimento atual'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='e_menor_de_idade',
            field=models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], default='Não', max_length=10, verbose_name='É menor de idade ou tutelado?'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='responsavel_nome',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Nome do responsável'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='responsavel_cpf',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='CPF do responsável'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='responsavel_endereco',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Endereço do responsável'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='responsavel_contato',
            field=models.CharField(blank=True, max_length=15, null=True, verbose_name='Contato do responsável'),
        ),
        migrations.AddField(
            model_name='paciente',
            name='responsavel_parentesco',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Grau de parentesco/relação'),
        ),
        # Update existing fields
        migrations.AlterField(
            model_name='paciente',
            name='estado_Civil',
            field=models.CharField(choices=[('Não Informado', 'Não Informado'), ('Casado(a)', 'Casado(a)'), ('Solteiro(a)', 'Solteiro(a)'), ('Divorciado(a)', 'Divorciado(a)'), ('Viúvo(a)', 'Viúvo(a)'), ('Não se aplica', 'Não se aplica')], max_length=255),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='escolaridade',
            field=models.CharField(choices=[('Sem escolaridade', 'Sem escolaridade'), ('Fundamental', 'Fundamental'), ('Médio', 'Médio'), ('Superior Completo', 'Superior Completo'), ('Superior incompleto', 'Superior incompleto'), ('Pós-Grauação', 'Pós-Graduação'), ('Mestrado', 'Mestrado'), ('Dotourado', 'Dotourado')], max_length=255),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='filhos_Quantidade',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='qual_Medicamento',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='rede_de_apoio',
            field=models.CharField(blank=True, help_text='Descreva sua rede de apoio (família, amigos, etc.) - Campo opcional', max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='motivo_e_objetivo',
            field=models.CharField(max_length=500, verbose_name='Motivo e objetivo do atendimento'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='observações',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='atendimento_Tipo_Tempo_Motivo',
            field=models.CharField(max_length=500, verbose_name='Tipo, tempo e motivo do atendimento anterior'),
        ),
        # Copy data from old fields to new fields
        migrations.RunSQL(
            "UPDATE pacientes_paciente SET possui_filhos = filhos WHERE filhos IS NOT NULL;",
            reverse_sql="UPDATE pacientes_paciente SET filhos = possui_filhos WHERE possui_filhos IS NOT NULL;",
        ),
        migrations.RunSQL(
            "UPDATE pacientes_paciente SET atendimento_anterior = atendimento WHERE atendimento IS NOT NULL;",
            reverse_sql="UPDATE pacientes_paciente SET atendimento = atendimento_anterior WHERE atendimento_anterior IS NOT NULL;",
        ),
        # Remove old fields
        migrations.RemoveField(
            model_name='paciente',
            name='filhos',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='atendimento',
        ),
        migrations.RemoveField(
            model_name='paciente',
            name='religião',
        ),
        # Update Pagamento model
        migrations.AlterField(
            model_name='pagamento',
            name='forma_pagamento',
            field=models.CharField(choices=[('Pix', 'Pix'), ('Dinheiro', 'Dinheiro'), ('Cartão de Crédito', 'Cartão de Crédito'), ('Cartão de Débito', 'Cartão de Débito'), ('Convênio', 'Convênio/Clínica')], max_length=20),
        ),
        migrations.AddField(
            model_name='pagamento',
            name='modalidade_convenio',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Modalidade do convênio/clínica'),
        ),
        migrations.AddField(
            model_name='pagamento',
            name='recibo_emitido',
            field=models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], default='Não', max_length=10, verbose_name='Recibo emitido?'),
        ),
    ]