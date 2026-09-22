from django.shortcuts import render

# Create your views here.
from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from .forms import MotoristaForm
from .models import Motorista


def lista(request):
    termo = request.GET.get('q', '').strip()
    motoristas = Motorista.objects.all()
    if termo:
        motoristas = motoristas.filter(nome__icontains=termo) | motoristas.filter(cnh__icontains=termo)
        motoristas = motoristas.distinct()
    paginator = Paginator(motoristas, 10)
    pagina = request.GET.get('page')
    motoristas_paginados = paginator.get_page(pagina)
    return render(request, 'motoristas/lista.html', {'motoristas': motoristas_paginados, 'termo': termo})


def cadastrar(request):
    if request.method == 'POST':
        form = MotoristaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Motorista cadastrado com sucesso.')
            return redirect('motoristas:lista')
    else:
        form = MotoristaForm()
    return render(request, 'motoristas/form.html', {'form': form, 'modo': 'novo'})


def editar(request, pk):
    motorista = get_object_or_404(Motorista, pk=pk)
    if request.method == 'POST':
        form = MotoristaForm(request.POST, instance=motorista)
        if form.is_valid():
            form.save()
            messages.success(request, 'Motorista atualizado com sucesso.')
            return redirect('motoristas:lista')
    else:
        form = MotoristaForm(instance=motorista)
    return render(request, 'motoristas/form.html', {'form': form, 'modo': 'editar', 'motorista': motorista})


def detalhe(request, pk):
    motorista = get_object_or_404(Motorista, pk=pk)
    return render(request, 'motoristas/detalhe.html', {'motorista': motorista})


def desativar(request, pk):
    motorista = get_object_or_404(Motorista, pk=pk)
    if request.method == 'POST':
        motorista.ativo = False
        motorista.save()
        messages.success(request, 'Motorista desativado com sucesso.')
        return redirect('motoristas:lista')
    return render(request, 'motoristas/detalhe.html', {'motorista': motorista, 'confirmar_desativacao': True})