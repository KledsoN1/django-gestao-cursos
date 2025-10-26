from django.shortcuts import render, redirect
from .models import Curso
from django.contrib import messages

# Create your views here.


def home(request):
    cursos_listados = Curso.objects.all()
    messages.success(request, 'Cursos listados com sucesso!')
    return render(request, "gestaoCursos.html", {"cursos": cursos_listados})


def registrar_curso(request):
    codigo = request.POST['txtCodigo']
    nome = request.POST['txtNome']
    creditos = request.POST['numCreditos']

    curso = Curso.objects.create(
        codigo=codigo, nome=nome, creditos=creditos)
    messages.success(request, 'Curso cadastrado com sucesso!')
    return redirect('/')


def edicao_curso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    return render(request, "edicaoCurso.html", {"curso": curso})


def editar_curso(request):
    codigo = request.POST['txtCodigo']
    nome = request.POST['txtNome']
    creditos = request.POST['numCreditos']

    curso = Curso.objects.get(codigo=codigo)
    curso.nome = nome
    curso.creditos = creditos
    curso.save()

    messages.success(request, 'Curso atualizado com sucesso!')

    return redirect('/')


def excluir_curso(request, codigo):
    curso = Curso.objects.get(codigo=codigo)
    curso.delete()

    messages.success(request, 'Curso excluído com sucesso!')

    return redirect('/')
