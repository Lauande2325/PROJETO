from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PecaForm
from .models import Peca


def lista(request):
    termo = request.GET.get('q', '').strip()
    pecas = Peca.objects.all()
    if termo:
        pecas = pecas.filter(nome__icontains=termo) | pecas.filter(codigo__icontains=termo) \
            | pecas.filter(fabricante__icontains=termo) | pecas.filter(categoria__icontains=termo)
        pecas = pecas.distinct()
    paginator = Paginator(pecas, 10)
    pagina = request.GET.get('page')
    pecas_paginadas = paginator.get_page(pagina)
    return render(request, 'pecas/lista.html', {'pecas': pecas_paginadas, 'termo': termo})


def cadastrar(request):
    if request.method == 'POST':
        form = PecaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Peça cadastrada com sucesso.')
            return redirect('pecas:lista')
    else:
        form = PecaForm()
    return render(request, 'pecas/form.html', {'form': form, 'modo': 'novo'})


def editar(request, pk):
    peca = get_object_or_404(Peca, pk=pk)
    if request.method == 'POST':
        form = PecaForm(request.POST, instance=peca)
        if form.is_valid():
            form.save()
            messages.success(request, 'Peça atualizada com sucesso.')
            return redirect('pecas:lista')
    else:
        form = PecaForm(instance=peca)
    return render(request, 'pecas/form.html', {'form': form, 'modo': 'editar', 'peca': peca})


def detalhe(request, pk):
    peca = get_object_or_404(Peca, pk=pk)
    return render(request, 'pecas/detalhe.html', {'peca': peca})


def desativar(request, pk):
    peca = get_object_or_404(Peca, pk=pk)
    if request.method == 'POST':
        peca.ativo = False
        peca.save()
        messages.success(request, 'Peça desativada com sucesso.')
        return redirect('pecas:lista')
    return render(request, 'pecas/detalhe.html', {'peca': peca, 'confirmar_desativacao': True})