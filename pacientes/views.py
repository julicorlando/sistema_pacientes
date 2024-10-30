from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente, Arquivo
from .forms import PacienteForm, ArquivoForm

def cadastrar_paciente(request):
    form = PacienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_pacientes')  # Redireciona para a página de listagem após o cadastro
    return render(request, 'pacientes/cadastrar_paciente.html', {'form': form})

def listar_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'pacientes/listar_pacientes.html', {'pacientes': pacientes})

def detalhes_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    arquivos = paciente.arquivos.all()
    return render(request, 'pacientes/detalhes_paciente.html', {'paciente': paciente, 'arquivos': arquivos})

def upload_arquivo(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    form = ArquivoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        arquivo = form.save(commit=False)
        arquivo.paciente = paciente
        arquivo.save()
        return redirect('detalhes_paciente', paciente_id=paciente_id)
    return render(request, 'pacientes/upload_arquivo.html', {'form': form, 'paciente': paciente})

def excluir_arquivo(request, arquivo_id):
    arquivo = get_object_or_404(Arquivo, id=arquivo_id)
    paciente_id = arquivo.paciente.id
    arquivo.delete()
    return redirect('detalhes_paciente', paciente_id=paciente_id)

from django.shortcuts import render

def homepage(request):
    return render(request, 'pacientes/homepage.html')

def excluir_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)  # Obtém o paciente ou retorna 404 se não existir
    paciente.delete()  # Exclui o paciente
    return redirect('listar_pacientes')  # Redireciona para a lista de pacientes

def confirmar_exclusao_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    return render(request, 'pacientes/confirmar_exclusao.html', {'paciente': paciente})

def editar_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)  # Busca o paciente pelo ID ou retorna erro 404
    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)  # Atualiza o objeto com novos dados
        if form.is_valid():
            form.save()
            return redirect('listar_pacientes')  # Redireciona para a lista de pacientes após a atualização
    else:
        form = PacienteForm(instance=paciente)  # Exibe o formulário com os dados atuais do paciente
    return render(request, 'pacientes/editar_paciente.html', {'form': form, 'paciente': paciente})