from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente, Arquivo
from .forms import PacienteForm, ArquivoForm, NovoUsuarioForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

@login_required
def cadastrar_paciente(request):
    if request.method == "POST":
        form = PacienteForm(request.POST)
        if form.is_valid():
            paciente = form.save(commit=False)  # Não salva ainda
            paciente.usuario = request.user  # Atribui o usuário logado
            paciente.save()  # Agora salva
            return redirect('listar_pacientes')  # Certifique-se de que 'listar_pacientes' está correto
    else:
        form = PacienteForm()  # Inicializa o formulário vazio
    return render(request, 'pacientes/cadastrar_paciente.html', {'form': form})

@login_required
def listar_pacientes(request):
    if request.user.is_authenticated:
        pacientes = Paciente.objects.filter(usuario=request.user)  # Filtra pacientes do usuário logado
    else:
        pacientes = Paciente.objects.none()  # Se não estiver logado, não retorna nada

    return render(request, 'pacientes/listar_pacientes.html', {'pacientes': pacientes})

@login_required
def detalhes_paciente(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    if paciente.usuario != request.user:  # Verifica se o paciente pertence ao usuário logado
        return render(request, '403.html')  # Retorna uma página de erro 403 se não for permitido

    return render(request, 'detalhes_paciente.html', {'paciente': paciente})

@login_required
def upload_arquivo(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    form = ArquivoForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        arquivo = form.save(commit=False)
        arquivo.paciente = paciente
        arquivo.save()
        return redirect('detalhes_paciente', paciente_id=paciente_id)
    return render(request, 'pacientes/upload_arquivo.html', {'form': form, 'paciente': paciente})

@login_required
def excluir_arquivo(request, arquivo_id):
    arquivo = get_object_or_404(Arquivo, id=arquivo_id)
    paciente_id = arquivo.paciente.id
    arquivo.delete()
    return redirect('detalhes_paciente', paciente_id=paciente_id)

from django.shortcuts import render

def homepage(request):
    return render(request, 'pacientes/homepage.html')

@login_required
def excluir_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)  # Obtém o paciente ou retorna 404 se não existir
    paciente.delete()  # Exclui o paciente
    return redirect('listar_pacientes')  # Redireciona para a lista de pacientes

@login_required
def confirmar_exclusao_paciente(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    return render(request, 'pacientes/confirmar_exclusao.html', {'paciente': paciente})

@login_required
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

def cadastro(request):
    if request.method == "POST":
        form = NovoUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # Faz login automaticamente após cadastro
            return redirect("homepage")  # Redireciona para uma página inicial após cadastro
    else:
        form = NovoUsuarioForm()
    return render(request, "cadastro.html", {"form": form})