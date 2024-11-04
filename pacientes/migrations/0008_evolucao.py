# Generated by Django 5.1.1 on 2024-11-04 19:33

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pacientes', '0007_alter_pagamento_paciente'),
    ]

    operations = [
        migrations.CreateModel(
            name='Evolucao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('conteudo', models.TextField()),
                ('data', models.DateTimeField(default=django.utils.timezone.now)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pacientes.paciente')),
            ],
        ),
    ]
