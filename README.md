 Projeto Currículo Virtual

Desenvolvi esta aplicação para reunir meu currículo, habilidades e projetos em um só lugar, facilitando a consulta das minhas informações profissionais.

Criei a interface com HTML e CSS, com visual inspirado em terminal, e o back-end com Python e Django. Os projetos podem ser cadastrados, editados e excluídos pelo painel administrativo, sem alterar o código.

Utilizei SQLite como banco de dados, Podman/Docker para execução em containers e GitHub Actions para CI/CD.

Para testar localmente, crie e ative um ambiente virtual e execute:

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Acesse http://127.0.0.1:8000/.

Desenvolvido por [Guilherme Zampar](https://github.com/GuilhermeAZampar).
