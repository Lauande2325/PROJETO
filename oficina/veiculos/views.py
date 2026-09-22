from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from .forms import VeiculoForm
from .models import Veiculo


def lista(request):
    termo = request.GET.get('q', '').strip()
    veiculos = Veiculo.objects.select_related('cliente').all()
    if termo:
        veiculos = veiculos.filter(placa__icontains=termo) | veiculos.filter(modelo__icontains=termo) \
            | veiculos.filter(cliente__nome_completo__icontains=termo)
        veiculos = veiculos.distinct()
    paginator = Paginator(veiculos, 10)
    pagina = request.GET.get('page')
    veiculos_paginados = paginator.get_page(pagina)
    return render(request, 'veiculos/lista.html', {'veiculos': veiculos_paginados, 'termo': termo})


def cadastrar(request):
    if request.method == 'POST':
        form = VeiculoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Veículo cadastrado com sucesso.')
            return redirect('veiculos:lista')
    else:
        form = VeiculoForm()
    return render(request, 'veiculos/form.html', {'form': form, 'modo': 'novo'})


def editar(request, pk):
    veiculo = get_object_or_404(Veiculo, pk=pk)
    if request.method == 'POST':
        form = VeiculoForm(request.POST, instance=veiculo)
        if form.is_valid():
            form.save()
            messages.success(request, 'Veículo atualizado com sucesso.')
            return redirect('veiculos:lista')
    else:
        form = VeiculoForm(instance=veiculo)
    return render(request, 'veiculos/form.html', {'form': form, 'modo': 'editar', 'veiculo': veiculo})


def detalhe(request, pk):
    veiculo = get_object_or_404(Veiculo, pk=pk)
    return render(request, 'veiculos/detalhe.html', {'veiculo': veiculo})


def desativar(request, pk):
    veiculo = get_object_or_404(Veiculo, pk=pk)
    if request.method == 'POST':
        veiculo.ativo = False
        veiculo.save()
        messages.success(request, 'Veículo desativado com sucesso.')
        return redirect('veiculos:lista')
    return render(request, 'veiculos/detalhe.html', {'veiculo': veiculo, 'confirmar_desativacao': True})