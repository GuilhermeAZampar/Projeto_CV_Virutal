# Projeto Currículo Virtual

Desenvolvi este projeto com Python e Django para apresentar meu currículo, habilidades e projetos. A interface foi feita com HTML e CSS, com visual inspirado em terminal.

Os projetos podem ser cadastrados, editados e excluídos pelo painel administrativo do Django. Utilizei SQLite como banco de dados, Podman/Docker para execução em containers e GitHub Actions para CI/CD.

Para executar localmente, crie e ative um ambiente virtual e rode:

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Acesse http://127.0.0.1:8000/.

Desenvolvido por [Guilherme Zampar](https://github.com/GuilhermeAZampar).
