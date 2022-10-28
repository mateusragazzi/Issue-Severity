# Classificador de severidade de _issues_: uma ferramenta para auxiliar novatos 

## Contextualização

_Issues_ registram e mapeiam alterações ou sugestões no projeto de
software. A severidade de uma _issue_ classifica a urgência na análise e
tratamento, definindo o andamento do projeto. Entretanto, novatos podem
confundir o conceito de severidade e seus níveis devido à inexperiência e a
falta de preparo, levando à uma má classificação. Portanto, foi desenvolvido
neste estudo: modelo de predição com técnicas de aprendizado de máquina;
uma ferramenta de apoio para sugerir a severidade; e um estudo de
viabilidade respondido por 29 participantes. A ferramenta foi avaliada como
fácil de utilizar e útil para auxiliar novatos durante a classificação de uma
_issue_, com 74.07% de taxa de concordância nas classificações das _issues_.

Ficou curioso? Leia o [artigo completo](https://drive.google.com/file/d/1MFfduP075xAzr3uI2xjq5NSt91FuhNrN/view?usp=sharing).

## Como executar?

### Ambiente

1 - Clone o projeto em sua máquina.

2 - Utilize Python 3 para executar o projeto. 

3 - Instale as dependências abaixo através do comando ```pip```: 
- pymysql
- sklearn
- pandas
- sqlalchemy
- flask_wtf
- flask

4 - Baixe a [base de dados](https://drive.google.com/file/d/1uXhP2rg_uUQJv6mY62JO5oEczIFW_w0d/view?usp=sharing). Após o download, extraia o arquivo `database.zip` e importe em seu banco de dados local.

5 - Configure o arquivo `.env`. Para isso, duplique o arquivo `.env.example` e altere os valores conforme seu ambiente.

### Aplicação

1 - Abra um terminal na raiz do projeto e execute:

```
python3 app.py
```

2 - A aplicação estará disponível em:

```
http://127.0.0.1:5000
```