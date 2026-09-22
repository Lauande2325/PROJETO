from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('clientes/', include('clientes.urls')),
    path('veiculos/', include('veiculos.urls')),
    path('pecas/', include('pecas.urls')),
    path('servicos/', include('servicos.urls')),
    path('mecanicos/', include('mecanicos.urls')),
    path('fornecedores/', include('fornecedores.urls')),
    path('estoque/', include('estoque.urls')),
    path('ordens-servico/', include('ordens_servico.urls')),
    path('financeiro/', include('financeiro.urls')),
    path('relatorios/', include('relatorios.urls')),
    path('colaboradores/', include('colaboradores.urls')),
    path('motoristas/', include('motoristas.urls')),
    path('frota/', include('frota.urls')),
    path('reservas/', include('reservas.urls')),
]