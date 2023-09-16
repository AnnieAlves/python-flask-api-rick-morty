# Exercício de API - Python + Flask

Repositório para os exercícios de estudos de consumo de dados de API com Python e Flask, pelo Bootcamp Back-End Python+Django da WomakersCode


## Objetivos

Exercício - Consumo de API com Flask

O seriado Rick and Morty é um desenho animado americano de comédia e ficção científica criado por Justin Roiland e Dan Harmon para o bloco de programação noturno Adult Swim, exibido no canal Cartoon Network. A série acompanha as perigosas aventuras do cientista louco Rick e seu neto Morty, que dividem seu tempo entre a vida familiar e viagens interdimensionais. A série é inspirada em Back to the Future e Doctor Who.

A API do Rick and Morty é uma API pública que contém informações sobre os personagens da série. A documentação da API pode ser encontrada em: https://rickandmortyapi.com/documentation/#rest

DEFINIÇÕES

A API possui três endpoints: um para listar os personagens, um para listar as localizações e dimensões, e um para listar os episódios. Durante a aula, utilizamos apenas o endpoint de personagens.

O objetivo deste exercício é adicionar novas funcionalidades ao projeto. Você deverá adicionar uma página para listar as localizações e os episódios, além de melhorar a página de perfil do personagem. Para isso, você deverá:

Criar uma nova rota para listar as localizações. A rota deverá ser acessível através do caminho /locations. A página deverá ser renderizada através do template locations.html. A página deverá conter uma tabela com as seguintes informações: nome, tipo e dimensão. A tabela deverá conter um link para a página de perfil da localização.

Criar uma nova rota para listar os episódios. A rota deverá ser acessível através do caminho /episodes. A página deverá ser renderizada através do template episodes.html. A página deverá conter uma tabela com as seguintes informações: nome, data de lançamento e código. A tabela deverá conter um link para a página de perfil do episódio.

Criar uma nova rota para exibir o perfil da localização. A rota deverá ser acessível através do caminho /location/<id>. A página deverá ser renderizada através do template location.html. A página deverá conter as seguintes informações: nome, tipo, dimensão e uma lista com os personagens que aparecem na localização. A lista deverá conter um link para a página de perfil do personagem.

Criar uma nova rota para exibir o perfil do episódio. A rota deverá ser acessível através do caminho /episode/<id>. A página deverá ser renderizada através do template episode.html. A página deverá conter as seguintes informações: nome, data de lançamento, código e uma lista com os personagens que aparecem no episódio. A lista deverá conter um link para a página de perfil do personagem.

Na página de perfil do personagem, adicione as seguintes informações: espécie, gênero, origem e localização. As informações de origem, localização e episódio em que o personagem aparece devem conter um link para a página de perfil da localização.


## Requisitos

É necessário instalar os arquivos através do ``` pip install -r requirements.txt```
Também deve-se criar um Virtual Envrioment
```python
python -3 -m venv .venv
```