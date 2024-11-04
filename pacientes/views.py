import datetime
from datetime import datetime
from django.shortcuts import render, redirect, get_object_or_404

import pacientes
from .models import Paciente, Arquivo, Pagamento
from .forms import EvolucaoForm, PacienteForm, ArquivoForm, NovoUsuarioForm, PagamentoForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from .models import Evolucao, Paciente
from django.utils import timezone


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
    query = request.GET.get('search', '')
    if query:
        pacientes = Paciente.objects.filter(nome__icontains=query)
    else:
        pacientes = Paciente.objects.all()

    return render(request, 'pacientes/listar_pacientes.html', {'pacientes': pacientes})

@login_required
def detalhes_paciente(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    pagamentos = Pagamento.objects.filter(paciente=paciente)  # Filtra os pagamentos do paciente

    context = {
        'paciente': paciente,
        'pagamentos': pagamentos,
        # Se você tiver algum formulário para adicionar pagamento, adicione aqui
    }
    return render(request, 'pacientes/detalhes_paciente.html', context)

@login_required
def upload_arquivo(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    
    if request.method == "POST":
        form = ArquivoForm(request.POST, request.FILES)
        if form.is_valid():
            arquivo = form.save(commit=False)
            arquivo.paciente = paciente
            arquivo.save()
            return redirect('detalhes_paciente', pk=paciente.pk)
        else:
            print(form.errors)  # Exibe os erros, se houver
    else:
        form = ArquivoForm()

    return render(request, 'pacientes/upload_arquivo.html', {'form': form, 'paciente': paciente})

@login_required
def excluir_arquivo(request, pk, arquivo_pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    arquivo = get_object_or_404(Arquivo, pk=arquivo_pk, paciente=paciente)
    
    if request.method == "POST":
        arquivo.delete()
        return redirect('detalhes_paciente', pk=paciente.pk)  # Redireciona para a página do paciente

    return redirect('detalhes_paciente', pk=paciente.pk)

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

@login_required
def adicionar_pagamento(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    
    if request.method == 'POST':
        valor = request.POST.get('valor')
        forma_pagamento = request.POST.get('forma_pagamento')
        
        # Lógica para adicionar pagamento ao paciente
        pagamento = Pagamento.objects.create(
            paciente=paciente,
            valor=valor,
            forma_pagamento=forma_pagamento,
            data_pagamento=datetime.now(),  # Certifique-se de importar datetime
        )
        
        return redirect('detalhes_paciente', pk=paciente.id)  # Redireciona para os detalhes do paciente

    return render(request, 'pacientes/detalhes_paciente.html', {'paciente': paciente})


@login_required
def registrar_pagamento(request, paciente_id):
    # Obtém o paciente ou retorna 404 se não encontrado
    paciente = get_object_or_404(Paciente, id=paciente_id)
    
    if request.method == 'POST':
        form = PagamentoForm(request.POST)
        if form.is_valid():
            pagamento = form.save(commit=False)
            pagamento.paciente = paciente  # Atribui o paciente ao pagamento
            pagamento.save()  # Salva o pagamento no banco de dados
            return redirect('detalhes_paciente', paciente_id=paciente.id)  # Redireciona para os detalhes do paciente
    else:
        form = PagamentoForm()  # Cria um novo formulário vazio
    
    # Renderiza a página com o formulário e o paciente
    return render(request, 'pagamentos/registrar_pagamento', {
        'form': form,
        'paciente': paciente
    })

@login_required
def excluir_pagamento(request, paciente_id, pagamento_id):
    if request.method == 'POST':
        pagamento = get_object_or_404(Pagamento, id=pagamento_id)
        pagamento.delete()
        return redirect('detalhes_paciente', pk=paciente_id)  # Aqui deve ser 'pk' se você usar 'pk' na URL
    return redirect('detalhes_paciente', pk=paciente_id)

@login_required
def evolucoes(request, paciente_id):
    paciente = get_object_or_404(Paciente, id=paciente_id)
    evolucoes = Evolucao.objects.filter(paciente=paciente).order_by('-data')
    return render(request, 'pacientes/evolucoes.html', {'paciente': paciente, 'evolucoes': evolucoes})

@login_required
def adicionar_evolucao(request, paciente_id):
    if request.method == 'POST':
        conteudo = request.POST['conteudo']
        paciente = get_object_or_404(Paciente, id=paciente_id)
        Evolucao.objects.create(paciente=paciente, conteudo=conteudo, data=timezone.now())
        return redirect('evolucoes', paciente_id=paciente.id)

@login_required
def editar_evolucao(request, evolucao_id):
    # Obtenha a evolução específica usando o ID
    evolucao = get_object_or_404(Evolucao, id=evolucao_id)
    
    if request.method == "POST":
        # Processa o formulário de edição e salva as alterações
        form = EvolucaoForm(request.POST, instance=evolucao)
        if form.is_valid():
            form.save()
            return redirect('evolucoes', paciente_id=evolucao.paciente.id)
    else:
        form = EvolucaoForm(instance=evolucao)
    
    return render(request, 'pacientes/editar_evolucao.html', {'form': form, 'paciente': evolucao.paciente})

@login_required
def excluir_evolucao(request, evolucao_id):
    evolucao = get_object_or_404(Evolucao, id=evolucao_id)
    paciente_id = evolucao.paciente.id
    evolucao.delete()
    return redirect('evolucoes', paciente_id=paciente_id)
