# API de Gerenciamento de Times e Campeonatos

Este é um projeto de API REST desenvolvido em Python utilizando o framework Flask. A API permite o gerenciamento básico de times e campeonatos através de endpoints HTTP.

## Funcionalidades

- Gerenciamento de times (adicionar e listar)
- Gerenciamento de campeonatos (adicionar e listar)
- API RESTful com endpoints JSON
- Tratamento de erros 404

## Tecnologias Utilizadas

- Python 3.12
- Flask 3.0.3
- Werkzeug 3.0.3
- Docker

## Estrutura do Projeto

```
.
├── Dockerfile
├── requirements.txt
├── settings.yml
└── src/
    ├── app.py
    └── test_app.py
```

## Endpoints da API

- `GET /`: Página inicial com mensagem de boas-vindas
- `GET /times`: Lista todos os times cadastrados
- `POST /times`: Adiciona um novo time
- `GET /campeonatos`: Lista todos os campeonatos cadastrados
- `POST /campeonatos`: Adiciona um novo campeonato

## Como Executar

### Usando Docker

1. Construa a imagem Docker:
```bash
docker build -t python-image .
```

2. Execute o container:
```bash
docker run -p 9000:9000 python-image
```

### Localmente

1. Instale as dependências:
```bash
pip install -r requirements.txt
```

2. Execute a aplicação:
```bash
python src/app.py
```

A API estará disponível em `http://localhost:9000`

## Testes

O projeto inclui testes automatizados usando pytest. Para executar os testes:

```bash
pytest src/test_app.py
```

## Observações

- A aplicação utiliza armazenamento em memória (não persistente)
- A API está configurada para rodar na porta 9000
- O modo debug está desativado por padrão 