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

### Arquitetura do Projeto
![plot](./assets/arquitetura_etl.png)

## Implementação

Para a construção do projeto, utilizei Pandas, pois facilitaria a exploração dos dados, para assim poder construir a pipeline e realizar os joins corretamente, além de ser uma tecnologia que tenho mais domínio. A princípio estranhei um pouco os arquivos de dados, pois não conhecia o formato jsonlines e tsv, porém uma jogada no google rápido resolveu essas questões. Assim que minha pipeline fazia exatamente o que precisava fazer, percebi que estava um pouco dificil de ler e compreender o que estava rolando, em partes por serem vários pequenos passos, e em outra pela própria sintaxe do pandas não ser tão clara, então trabalhei por últime em refatorar bem o código e deixar minhas ações bem explicitas. Por fim decidi colocar o código para rodar em container, para não acontecer caso "mas roda na minha máquina".

## Utilização

### Requisitos
* Docker
```sh
sudo apt get docker
```
* Docker-compose
```sh
sudo apt get docker-compose
```
* python
```sh
sudo apt get python3
```

### Instalação
* Clone o repositório
```sh
git clone https://github.com/brianamaral/infoprice-engenheiro-de-dados-teste-tecnico-etl.git
```

### Rodar

#### Rodando com docker
* Rode o seguinte comando a partir da pasta raiz do repositório
```sh
make run-docker
```
#### Rodando localmente
* Rode o seguinte comando a partir da pasta raiz do repositório para inicializar o ambiente
```sh
make build
```
* E então rode o seguinte comando para iniciar a pipeline
```sh
make run
```

