## Sobre o Projeto 
Minha solução para o teste técnico para vaga de Engenheiro de Dados Jr na InfoPrice

### Construido Com
* [Python](https://www.python.org/)
* [Pandas](https://pandas.pydata.org/)
* [Docker](https://www.docker.com/)

### Estrutura de Diretórios
```sh
|--data #Pasta com o dados
	|--input #dados de entrada
	|--output #dados resultantes da transformação
|--pipeline #codigos da pipeline
	|--preprocess_pipelines #pasta com pacote de sub pipelines, para dar mais legibilidade
             |--pipelines.py
	|--transformations #pasta com pacote de transformações comuns nos datasets
             |--columns_transformations.py #transformações comuns de colunas
             |--joins.py #transformações de joins
             |--response_transformations.py #transformações especificas para a coluna response
             |--row_transformations.py #transformações comuns de linhas
	|--main.py #script principal da pipeline
```
