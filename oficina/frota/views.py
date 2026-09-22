from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from .forms import VeiculoFrotaForm
from .models import Veiculo


def lista(request):
    termo = request.GET.get('q', '').strip()
    veiculos = Veiculo.objects.all()
    if termo:
        veiculos = veiculos.filter(placa__icontains=termo) | veiculos.filter(modelo__icontains=termo)
        veiculos = veiculos.distinct()
    paginator = Paginator(veiculos, 10)
    pagina = request.GET.get('page')
    veiculos_paginados = paginator.get_page(pagina)
    return render(request, 'frota/lista.html', {'veiculos': veiculos_paginados, 'termo': termo})


def cadastrar(request):
    if request.method == 'POST':
        form = VeiculoFrotaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Veículo cadastrado com sucesso.')
            return redirect('frota:lista')
    else:
        form = VeiculoFrotaForm()
    return render(request, 'frota/form.html', {'form': form, 'modo': 'novo'})


def editar(request, pk):
    veiculo = get_object_or_404(Veiculo, pk=pk)
    if request.method == 'POST':
        form = VeiculoFrotaForm(request.POST, instance=veiculo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Veículo atualizado com sucesso.')
            return redirect('frota:lista')
    else:
        form = VeiculoFrotaForm(instance=veiculo)
    return render(request, 'frota/form.html', {'form': form, 'modo': 'editar', 'veiculo': veiculo})


def detalhe(request, pk):
    veiculo = get_object_or_404(Veiculo, pk=pk)
    return render(request, 'frota/detalhe.html', {'veiculo': veiculo})


def desativar(request, pk):
    veiculo = get_object_or_404(Veiculo, pk=pk)
    if request.method == 'POST':
        veiculo.ativo = False
        veiculo.save()
        messages.success(request, 'Veículo desativado com sucesso.')
        return redirect('frota:lista')
    return render(request, 'frota/detalhe.html', {'veiculo': veiculo, 'confirmar_desativacao': True})