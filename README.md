# 🚀 Portfólio & Currículo Interativo em Django

Um sistema web interativo estilo *terminal/developer* construído para expor meu currículo profissional, habilidades e projetos de desenvolvimento. O projeto conta com painel administrativo interno para cadastro dinâmico de novos projetos e esteira automatizada de CI/CD.

🔗 **Repositório oficial:** [https://github.com/GuilhermeAZampar/Projeto_CV_Virutal](https://github.com/GuilhermeAZampar/Projeto_CV_Virutal)

---

## 🛠️ Tecnologias Utilizadas

- **Back-end:** Python, Django (ORM, Views, Templates, Autenticação)
- **Banco de Dados:** SQLite3 (gerenciado via ORM nativo do Django)
- **Front-end:** HTML5, CSS3 (Design customizado no estilo *Cyberpunk/Terminal*)
- **Containerização:** Podman / Docker
- **DevOps & CI/CD:** GitHub Actions (Pipelines automatizados de verificação, build e deploy)

---

## 📌 Funcionalidades

- **Apresentação Profissional:** Exibição do resumo profissional, tecnologias/stack, informações de contato e status do sistema.
- **Gerenciamento de Projetos:**
  - Listagem dos meus projetos novos e antigos com descrição, tecnologias utilizadas e links diretos.
  - Visualização detalhada de cada projeto (`/projeto/<id>/`).
- **Painel Administrativo (`/admin/`):**
  - Sistema seguro de autenticação/login para administração.
  - CRUD completo para adicionar, editar ou remover novos projetos sem precisar alterar o código-fonte.
- **Ambiente Containerizado:** Pronto para execução isolada via Podman/Docker.
- **Pipelines de CI/CD:** Integração e entrega contínua pré-configuradas para validação e rotinas automatizadas.

- ## ⚙️ Como Executar o Projeto Localmente

### Opção 1: Executando com Podman / Docker (Recomendado)

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/GuilhermeAZampar/Projeto_CV_Virutal.git](https://github.com/GuilhermeAZampar/Projeto_CV_Virutal.git)
   cd Projeto_CV_Virutal

Construa a imagem:
   podman build -t curriculo-django .

 
Execute o container mapeando o volume do projeto e a porta 8000:
podman run -d -p 8000:8000 -v "${PWD}:/app" --name curriculo-django curriculo-django

Aplique as migrações no banco de dados interno:
podman exec -it curriculo-django python manage.py migrate


Opção 2: Executando com Ambiente Virtual Python (.venv)

Clone o repositório e mude para a pasta do projeto:
git clone [https://github.com/GuilhermeAZampar/Projeto_CV_Virutal.git](https://github.com/GuilhermeAZampar/Projeto_CV_Virutal.git)
cd Projeto_CV_Virutal

Crie e ative o ambiente virtual:
python -m venv .venv
# Windows (PowerShell):
.\.venv\Scripts\Activate.ps1
# Linux/macOS:
source .venv/bin/activate


Instale as dependências:
pip install -r requirements.txt


Execute as migrações do banco de dados:
python manage.py migrate


Inicie o servidor de desenvolvimento:
python manage.py runserver
Acesse no navegador em http://127.0.0.1:8000/

