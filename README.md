# ubots-moviesapi-challenge

## Resumo

Desafio técnico para a vaga de estágio.

O objetivo é criar uma API RESTFUL para cadastrar e avaliar filmes.

## Tecnologias

- [Python 3.12](https://python.org)
    - [FastAPI](https://fastapi.tiangolo.com/)
    - [SQLModel](https://sqlmodel.tiangolo.com/)
    - [Uvicorn](https://www.uvicorn.org/)

## Setup

1. Instale o Python 3.12

2. Baixe o zip do código no GitHub ou se preferir, use o comando abaixo (necessário git instalado):

```bash
git clone "https://github.com/ReiLoko4/Ubots-challenge"
```

3. Navegue até a pasta raiz do projeto e abra um terminal

3. Instale as dependências do projeto com o comando abaixo:

```bash
pip install -r requirements.txt
```

5. Inicie o servidor da API com o comando abaixo:

```bash
uvicorn MovieApi.main:app
```

6. Acesse o endereço de host, por padrão `http://127.0.0.1:8000`

Agora só utilizar!

## Modo de uso

### Dicas

Recomendo utilizar o endpoint padrão da própria biblioteca, a FastAPI, para testar os endpoints.

Para isso, basta adicionar o endpoint `/docs` na url.

### Modelos

No projeto temos dois modelos, o `Movie` (filme) e a `Review` (avaliação)

Sendo assim:

```js
Movie {
    id: integer,
    title: string,
    synopsis: string,
    dubbing: string,
    subtitle: string,
    director: string,
    duration: string,
    release_date: string,
    rating: float
}

Review {
    id: integer,
    movie_id: integer,
    title: string,
    text: string,
    reviewer: string
    rating: float,
}
```

### Endpoints

- POST `/create_movie`
    - Recebe um JSON no modelo `Movie`, porém com `id` como nulo ou sem a chave.
    - Status 200 retorna um JSON no modelo `Movie`

- POST `/create_review`
    - Recebe um JSON no modelo `Review`, porém com `id` como nulo ou sem a chave. 
    - `movie_id` referência um filme existente no modelo `Movie`.
    - Status 200 retorna um JSON no modelo `Review`

- GET `/movie/<movie_id>`
    - Recebe `movie_id`como parâmetro através da URL.
    - Retorna um JSON no modelo `Movie` se o id do filme existir.

- GET `/movies`
    - Retorna todos os filmes cadastrados em uma lista de filmes no modelo `Movie`.
    - Retorna a lista vazia se não houver nenhum filme.

- GET `/review/<review_id>`
    - Recebe `review_id`como parâmetro através da URL.
    - Retorna um JSON no modelo `Review` se o id da avaliação existir.

- GET `/reviews/<movie_id>`
    - Recebe `movie_id`como parâmetro através da URL.
    - Retorna todos as avaliações cadastrados no filme por meio do `movie_id` 
    uma lista de avaliações no modelo `Review`.
    - Se o filme não existir um erro será gerado
    - Retorna a lista vazia se não houver nenhum filme.

- PUT `/update_movie/<movie_id>`
    - Recebe `movie_id`como parâmetro através da URL.
    - Recene um JSON no modelo `Movie` através do corpo da requisição.
    - Retorna um JSON no modelo `Movie` atualizado.
    - Se o filme não existir, retorna um erro.

- PUT `/update_review/<review_id>`
    - Recebe `review_id`como parâmetro através da URL.
    - Recene um JSON no modelo `Review` através do corpo da requisição.
    - Retorna um JSON no modelo `Review` atualizado.
    - Se a avaliação não existir, retorna um erro.

- DELETE `/delete_movie/<movie_id>`
    - Recebe `movie_id`como parâmetro através da URL.
    - Retorna uma mensagem de confirmação dizendo o id do filme apagado.
    - Se o filme não existir, retorna um erro.

- DELETE `/delete_review/<review_id>`
    - Recebe `review_id`como parâmetro através da URL.
    - Retorna uma mensagem de confirmação dizendo o id da avaliação apagada.
    - Se a avaliação não existir, retorna um erro.

