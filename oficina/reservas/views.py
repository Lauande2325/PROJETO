import uuid

from django.contrib import messages
from django.core.paginator import Paginator
from django.core.exceptions import ValidationError
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ReservaForm
from .models import Reserva


def lista(request):
    termo = request.GET.get('q', '').strip()
    reservas = Reserva.objects.all()
    if termo:
        reservas = reservas.filter(atividade__icontains=termo) | reservas.filter(setor__icontains=termo)
        reservas = reservas.distinct()
    paginator = Paginator(reservas, 10)
    pagina = request.GET.get('page')
    reservas_paginadas = paginator.get_page(pagina)
    return render(request, 'reservas/lista.html', {'reservas': reservas_paginadas, 'termo': termo})


def cadastrar(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            reserva = form.save(commit=False)
            if not reserva.protocolo_unico:
                reserva.protocolo_unico = uuid.uuid4().hex[:12].upper()
            try:
                reserva.full_clean()
                reserva.save()
                messages.success(request, 'Reserva cadastrada com sucesso.')
                return redirect('reservas:lista')
            except ValidationError as erro:
                for msg in erro.messages:
                    form.add_error(None, msg)
    else:
        form = ReservaForm()
    return render(request, 'reservas/form.html', {'form': form, 'modo': 'novo'})


def editar(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            messages.success(request, 'Reserva atualizada com sucesso.')
            form.save()
            return redirect('reservas:lista')
    else:
        form = ReservaForm(instance=reserva)
    return render(request, 'reservas/form.html', {'form': form, 'modo': 'editar', 'reserva': reserva})


def detalhe(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    return render(request, 'reservas/detalhe.html', {'reserva': reserva})


def desativar(request, pk):
    reserva = get_object_or_404(Reserva, pk=pk)
    if request.method == 'POST':
        reserva.status = 'cancelada'
        reserva.save()
        messages.success(request, 'Reserva cancelada com sucesso.')
        return redirect('reservas:lista')
    return render(request, 'reservas/detalhe.html', {'reserva': reserva, 'confirmar_desativacao': True})