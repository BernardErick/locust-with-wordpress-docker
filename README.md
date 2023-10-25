
# Baixe e instale o python3, docker e docker-compose

# Configurando ambiente docker-compose

- Entre na raiz do projeto e execute

- docker-compose up

# Configurando ambiente python3

- Entre na raiz do projeto e execute

- python3 -m venv .venv

- source .venv/bin/activate

- pip install --upgrade pip

- pip install locust

- locust -f locustfile.py

# Configurando interface do locust

- Adicione por exemplo: 1000 usuários e 100 de spawn rate
