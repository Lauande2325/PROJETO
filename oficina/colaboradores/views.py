from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ColaboradorForm
from .models import Colaborador


def lista(request):
    termo = request.GET.get('q', '').strip()
    colaboradores = Colaborador.objects.all()
    if termo:
        colaboradores = colaboradores.filter(nome__icontains=termo) | colaboradores.filter(departamento__icontains=termo)
        colaboradores = colaboradores.distinct()
    paginator = Paginator(colaboradores, 10)
    pagina = request.GET.get('page')
    colaboradores_paginados = paginator.get_page(pagina)
    return render(request, 'colaboradores/lista.html', {'colaboradores': colaboradores_paginados, 'termo': termo})


def cadastrar(request):
    if request.method == 'POST':
        form = ColaboradorForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Colaborador cadastrado com sucesso.')
            return redirect('colaboradores:lista')
    else:
        form = ColaboradorForm()
    return render(request, 'colaboradores/form.html', {'form': form, 'modo': 'novo'})


def editar(request, pk):
    colaborador = get_object_or_404(Colaborador, pk=pk)
    if request.method == 'POST':
        form = ColaboradorForm(request.POST, instance=colaborador)
        if form.is_valid():
            form.save()
            messages.success(request, 'Colaborador atualizado com sucesso.')
            return redirect('colaboradores:lista')
    else:
        form = ColaboradorForm(instance=colaborador)
    return render(request, 'colaboradores/form.html', {'form': form, 'modo': 'editar', 'colaborador': colaborador})


def detalhe(request, pk):
    colaborador = get_object_or_404(Colaborador, pk=pk)
    return render(request, 'colaboradores/detalhe.html', {'colaborador': colaborador})


def desativar(request, pk):
    colaborador = get_object_or_404(Colaborador, pk=pk)
    if request.method == 'POST':
        colaborador.ativo = False
        colaborador.save()
        messages.success(request, 'Colaborador desativado com sucesso.')
        return redirect('colaboradores:lista')
    return render(request, 'colaboradores/detalhe.html', {'colaborador': colaborador, 'confirmar_desativacao': True})