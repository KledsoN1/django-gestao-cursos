# 🎓 Projeto de Gestão de Cursos (Django)

Este é um projeto **CRUD** (Create, Read, Update, Delete) simples para gerenciar cursos universitários, desenvolvido com **Python** e o framework **Django**.  
A aplicação permite cadastrar, listar, editar e excluir cursos de forma simples e direta, utilizando um banco de dados **SQLite**.

## ✨ Funcionalidades
- **Cadastrar Cursos:** Adicionar novos cursos com código, nome e número de créditos.  
- **Listar Cursos:** Ver todos os cursos cadastrados em uma tabela.  
- **Editar Cursos:** Atualizar as informações de um curso existente.  
- **Excluir Cursos:** Remover um curso do banco de dados (com um pop-up de confirmação em JavaScript).  

## 🛠️ Tecnologias Utilizadas
**Backend:**  
- Python 3  
- Django  

**Frontend:**  
- HTML5  
- Bootstrap 4 (para o layout e componentes)  
- JavaScript (vanilla, para a confirmação de exclusão)  

**Banco de Dados:**  
- SQLite 3 (padrão do Django)  

## 🚀 Como Executar Localmente
Siga os passos abaixo para rodar o projeto em sua máquina local.

1. **Clone o Repositório**

```bash
git clone https://github.com/KledsoN1/django-gestao-cursos.git
cd django-gestao-cursos
```

## 🛠️ Crie e Ative um Ambiente Virtual (venv)

## Criar o ambiente
```bash
python -m venv venv
```

## Ativar no Windows (PowerShell)
```bash
.\venv\Scripts\Activate.ps1
```

## Ativar no Linux/Mac
```bash
source venv/bin/activate
```

## Instalar o Django
```bash
pip install django
```

## Aplique as migrações do banco de dados
```bash
python manage.py migrate
```

## 🧑‍💻 Crie um superusuário para acessar o painel admin (Opcional)
```bash
python manage.py createsuperuser
```
#### Siga as instruções para criar um nome de usuário e senha


## 🏗️ Rode o servidor de desenvolvimento
```bash
python manage.py runserver
```

## 🪄 Acesse a Aplicação 
#### Abra seu navegador e acesse: 
http://127.0.0.1:8000/