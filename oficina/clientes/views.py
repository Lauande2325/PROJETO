from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ClienteForm
from .models import Cliente


def lista(request):
    termo = request.GET.get('q', '').strip()
    clientes = Cliente.objects.all()
    if termo:
        clientes = clientes.filter(nome_completo__icontains=termo)
    paginator = Paginator(clientes, 10)
    pagina = request.GET.get('page')
    clientes_paginados = paginator.get_page(pagina)
    return render(request, 'clientes/lista.html', {'clientes': clientes_paginados, 'termo': termo})


def cadastrar(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente cadastrado com sucesso.')
            return redirect('clientes:lista')
    else:
        form = ClienteForm()
    return render(request, 'clientes/form.html', {'form': form, 'modo': 'novo'})


def editar(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente atualizado com sucesso.')
            return redirect('clientes:lista')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'clientes/form.html', {'form': form, 'modo': 'editar', 'cliente': cliente})


def detalhe(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    return render(request, 'clientes/detalhe.html', {'cliente': cliente})


def desativar(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.ativo = False
        cliente.save()
        messages.success(request, 'Cliente desativado com sucesso.')
        return redirect('clientes:lista')
    return render(request, 'clientes/detalhe.html', {'cliente': cliente, 'confirmar_desativacao': True})