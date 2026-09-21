from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from .forms import MecanicoForm
from .models import Mecanico


def lista(request):
    termo = request.GET.get('q', '').strip()
    mecanicos = Mecanico.objects.all()
    if termo:
        mecanicos = mecanicos.filter(nome__icontains=termo) | mecanicos.filter(especialidade__icontains=termo)
        mecanicos = mecanicos.distinct()
    paginator = Paginator(mecanicos, 10)
    pagina = request.GET.get('page')
    mecanicos_paginados = paginator.get_page(pagina)
    return render(request, 'mecanicos/lista.html', {'mecanicos': mecanicos_paginados, 'termo': termo})


def cadastrar(request):
    if request.method == 'POST':
        form = MecanicoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mecânico cadastrado com sucesso.')
            return redirect('mecanicos:lista')
    else:
        form = MecanicoForm()
    return render(request, 'mecanicos/form.html', {'form': form, 'modo': 'novo'})


def editar(request, pk):
    mecanico = get_object_or_404(Mecanico, pk=pk)
    if request.method == 'POST':
        form = MecanicoForm(request.POST, instance=mecanico)
        if form.is_valid():
            form.save()
            messages.success(request, 'Mecânico atualizado com sucesso.')
            return redirect('mecanicos:lista')
    else:
        form = MecanicoForm(instance=mecanico)
    return render(request, 'mecanicos/form.html', {'form': form, 'modo': 'editar', 'mecanico': mecanico})


def detalhe(request, pk):
    mecanico = get_object_or_404(Mecanico, pk=pk)
    return render(request, 'mecanicos/detalhe.html', {'mecanico': mecanico})


def desativar(request, pk):
    mecanico = get_object_or_404(Mecanico, pk=pk)
    if request.method == 'POST':
        mecanico.ativo = False
        mecanico.save()
        messages.success(request, 'Mecânico desativado com sucesso.')
        return redirect('mecanicos:lista')
    return render(request, 'mecanicos/detalhe.html', {'mecanico': mecanico, 'confirmar_desativacao': True})