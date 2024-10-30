# Generated by Django 5.1.1 on 2024-10-30 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0002_remove_paciente_data_nascimento_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='paciente',
            name='observações',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='paciente',
            name='atendimento',
            field=models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=10),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='filhos',
            field=models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=10),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='sexo',
            field=models.CharField(choices=[('Masc', 'Masculino'), ('Fem', 'Feminino'), ('O', 'Outro')], max_length=10),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='toma_Algum_Medicamento',
            field=models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=10),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='trabalha_no_momento',
            field=models.CharField(choices=[('Sim', 'Sim'), ('Não', 'Não')], max_length=10),
        ),
    ]
