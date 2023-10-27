# Aplicação para a disciplina de computação distribuida - Ciência da computação

Realizar testes de carga utilizando o gerador de carga Locust para avaliar o desempenho de diversos cenários de uso do Wordpress, variando a arquitetura da aplicação (número de instâncias do Wordpress) e variando a quantidade de usuários gerados pelo Locust. O contêiner do Locust deve ser definido e adicionado ao docker-compose criado no Trabalho 2.
Cenários de teste:
1) Blog post com uma imagem de aproximadamente 1mb;
2) Blog post com um texto de aproximadamente 400kb;
3) Blog post com uma imagem de 300kb;

#Instalação e configuração

## Baixe e instale o python3, docker e docker-compose
- [https://www.python.org/downloads/](https://python-guide-pt-br.readthedocs.io/pt-br/latest/starting/install3/linux.html)
- https://docs.docker.com/engine/install/
- https://docs.docker.com/compose/install/

## Configurando ambiente docker-compose

- Entre na raiz do projeto e execute

- `docker-compose up `

## Configurando ambiente python3

- Entre na raiz do projeto e execute

- `python3 -m venv .venv`

- `source .venv/bin/activate`

- `pip install --upgrade pip`

- `pip install locust`

- `locust -f locustfile.py --csv=results`

## Configurando interface do locust

- Adicione por exemplo: 1000 usuários e 100 de spawn rate
## Aplicações
- Locust: http://localhost:8089
- Wordpress no nginx: http://localhost:80