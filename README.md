# APYLivros

APYLivros é uma API simples de gerenciamento de livros, construída com Python e Flask.

## Visão geral

APYLivros é uma API que permite visualizar, adicionar, editar e excluir informações sobre livros. Ela foi desenvolvida com o objetivo de ser uma implementação inicial de uma API básica, adequada para fins educacionais e de aprendizado.

## Funcionalidades

- Visualizar a lista de todos os livros cadastrados.
- Obter informações detalhadas sobre um livro específico através do seu ID.
- Adicionar um novo livro à lista.
- Editar informações de um livro existente com base no seu ID.
- Excluir um livro da lista com base no seu ID.

## Instalação

1. Certifique-se de ter o Python instalado (versão 3.6 ou superior).

2. Instale as dependências do projeto:

```markdown
pip install -r requirements.txt
```



## Exemplos de uso

1. Inicie o servidor Flask:

```markdown
python app.py
```

2. Acesse a API usando as seguintes rotas:

### Consultar livros cadastrados

```http
GET /livros
```
Retorna a lista de todos os livros cadastrados.

### Consultar livro pela ID
```http
GET /livros/{id}
```
Substitua `{id}` pelo ID numérico do livro desejado para obter detalhes sobre ele.


### Editar livro pela ID
```http
PUT /livros/{id}
```
Substitua `{id}` pelo ID numérico do livro que deseja editar. Envie um JSON com os campos `title` e `autor` para atualizar as informações do livro.

### Criar novo livro
```http
POST /livros
```
Envie um JSON com os campos `title` e `autor` para criar um novo livro. O ID será gerado automaticamente.

### Excluir livro pela ID
```http
DELETE /livros/{id}
```
Substitua `{id}` pelo ID numérico do livro que deseja excluir.


## Pré-requisitos

- Python 3.x
- Flask (instalado automaticamente ao seguir as etapas de instalação)

