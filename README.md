Projeto de Gestão de Cursos (Django)
Este é um projeto CRUD (Create, Read, Update, Delete) simples para gerenciar cursos universitários, desenvolvido com Python e o framework Django.

A aplicação permite cadastrar, listar, editar e excluir cursos de forma simples e direta, utilizando um banco de dados SQLite.

📸 Visão Geral
Aqui está uma captura de tela da aplicação principal, mostrando o formulário de cadastro e a listagem de cursos:

(Para que esta imagem apareça, certifique-se de ter enviado o arquivo image_412980.png para o seu repositório GitHub, na mesma pasta que este README.md.)

✨ Funcionalidades
Cadastrar Cursos: Adicionar novos cursos com código, nome e número de créditos.

Listar Cursos: Ver todos os cursos cadastrados em uma tabela.

Editar Cursos: Atualizar as informações de um curso existente.

Excluir Cursos: Remover um curso do banco de dados (com um pop-up de confirmação em JavaScript).

🛠️ Tecnologias Utilizadas
Backend:

Python 3

Django

Frontend:

HTML5

Bootstrap 4 (para o layout e componentes)

JavaScript (vanilla, para a confirmação de exclusão)

Banco de Dados:

SQLite 3 (padrão do Django)

🚀 Como Executar Localmente
Siga os passos abaixo para rodar o projeto em sua máquina local.

1. Clone o Repositório

Bash

git clone https://github.com/SEU-USUARIO/NOME-DO-SEU-REPOSITORIO.git
cd NOME-DO-SEU-REPOSITORIO
(Substitua pela URL do seu repositório)

2. Crie e Ative um Ambiente Virtual (venv)

Bash

# Criar o ambiente
python -m venv venv

# Ativar no Windows (PowerShell)
.\venv\Scripts\Activate.ps1

# Ativar no Linux/Mac
source venv/bin/activate
3. Instale as Dependências Este projeto requer apenas o Django.

Bash

pip install django
4. Aplique as Migrações do Banco de Dados Isso criará o arquivo de banco de dados Universidad.db e as tabelas necessárias.

Bash

python manage.py migrate
5. Crie um Superusuário (Opcional) Isso é útil para acessar o painel /admin e gerenciar os dados por lá.

Bash

python manage.py createsuperuser
(Siga as instruções para criar um nome de usuário e senha)

6. Rode o Servidor de Desenvolvimento

Bash

python manage.py runserver
7. Acesse a Aplicação Abra seu navegador e acesse: http://127.0.0.1:8000/