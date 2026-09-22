from django.urls import path
from . import views

app_name = 'reservas'

urlpatterns = [
    path('', views.lista, name='lista'),
    path('nova/', views.cadastrar, name='cadastrar'),
    path('<int:pk>/', views.detalhe, name='detalhe'),
    path('<int:pk>/editar/', views.editar, name='editar'),
    path('<int:pk>/desativar/', views.desativar, name='desativar'),
]