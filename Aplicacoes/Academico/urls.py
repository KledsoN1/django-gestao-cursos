from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('registrarCurso/', views.registrar_curso), 
    path('edicaoCurso/<codigo>', views.edicao_curso), 
    path('editarCurso/', views.editar_curso),
    path('excluirCurso/<codigo>', views.excluir_curso) 
]