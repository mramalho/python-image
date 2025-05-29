# API de Gerenciamento de Times e Campeonatos

Este projeto é uma API REST desenvolvida em Python com Flask para gerenciar times e campeonatos. A API permite adicionar e listar times e campeonatos, com respostas em JSON e tratamento de erros para rotas inexistentes.

## Funcionalidades

- Adicionar e listar times de futebol
- Adicionar e listar campeonatos
- Respostas em JSON
- Tratamento de erro 404 personalizado

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
├── sonar-project.properties
└── src/
    ├── app.py
    └── test_app.py
```

## Endpoints da API

- `GET /`  
  Retorna mensagem de boas-vindas.

- `GET /times`  
  Lista todos os times cadastrados.

- `POST /times`  
  Adiciona um novo time.  
  Exemplo de payload:
  ```json
  {
    "nome": "Flamengo",
    "estado": "RJ"
  }
  ```

- `GET /campeonatos`  
  Lista todos os campeonatos cadastrados.

- `POST /campeonatos`  
  Adiciona um novo campeonato.  
  Exemplo de payload:
  ```json
  {
    "nome": "Brasileirão",
    "ano": 2024
  }
  ```

- Resposta para rotas inexistentes:
  ```json
  { "error": "Pagina nao encontrada!" }
  ```

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

A API estará disponível em `http://localhost:9000`

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

O projeto inclui testes automatizados usando `unittest`. Para executar os testes:

```bash
python -m unittest src/test_app.py
```

## Observações

- O armazenamento é feito em memória (os dados são perdidos ao reiniciar a aplicação).
- A API está configurada para rodar na porta 9000.
- O modo debug está desativado por padrão.
- O arquivo `settings.yml` e `sonar-project.properties` são usados para configurações de CI/CD e análise estática, respectivamente. 