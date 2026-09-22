from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ServicoForm
from .models import Servico


def lista(request):
    termo = request.GET.get('q', '').strip()
    servicos = Servico.objects.all()
    if termo:
        servicos = servicos.filter(nome__icontains=termo) | servicos.filter(categoria__icontains=termo)
        servicos = servicos.distinct()
    paginator = Paginator(servicos, 10)
    pagina = request.GET.get('page')
    servicos_paginados = paginator.get_page(pagina)
    return render(request, 'servicos/lista.html', {'servicos': servicos_paginados, 'termo': termo})


def cadastrar(request):
    if request.method == 'POST':
        form = ServicoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Serviço cadastrado com sucesso.')
            return redirect('servicos:lista')
    else:
        form = ServicoForm()
    return render(request, 'servicos/form.html', {'form': form, 'modo': 'novo'})


def editar(request, pk):
    servico = get_object_or_404(Servico, pk=pk)
    if request.method == 'POST':
        form = ServicoForm(request.POST, instance=servico)
        if form.is_valid():
            form.save()
            messages.success(request, 'Serviço atualizado com sucesso.')
            return redirect('servicos:lista')
    else:
        form = ServicoForm(instance=servico)
    return render(request, 'servicos/form.html', {'form': form, 'modo': 'editar', 'servico': servico})


def detalhe(request, pk):
    servico = get_object_or_404(Servico, pk=pk)
    return render(request, 'servicos/detalhe.html', {'servico': servico})


def desativar(request, pk):
    servico = get_object_or_404(Servico, pk=pk)
    if request.method == 'POST':
        servico.ativo = False
        servico.save()
        messages.success(request, 'Serviço desativado com sucesso.')
        return redirect('servicos:lista')
    return render(request, 'servicos/detalhe.html', {'servico': servico, 'confirmar_desativacao': True})