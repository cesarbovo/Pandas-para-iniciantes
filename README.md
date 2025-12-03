# Pandas para iniciantes

Este repositório apresenta um script educativo em Python que demonstra os principais recursos da biblioteca Pandas para análise de dados de vendas. O programa `analise_vendas.py` cria um conjunto de dados sintético, explora sua estrutura, realiza cálculos, filtros e agrupamentos, e exporta os resultados para CSV.

## Funcionalidades Principais

O script cobre conceitos fundamentais do Pandas de forma didática e sequencial:

- Criação de DataFrames a partir de dicionários com colunas como Produto, Categoria, Preço, Quantidade e Vendedor.
- Exploração de dados com `info()`, `describe()` e `head()`.
- Cálculo de novas colunas, como Receita (Preço × Quantidade).
- Filtros condicionais para vendas de alto valor.
- Agrupamentos por Vendedor e Categoria com soma de receitas.
- Estatísticas resumidas (total, média, máximo, mínimo) e ordenação.
- Análise de diversidade (produtos únicos, vendedores) e exportação para `vendas_analise.csv.

## Pré-requisitos

- Python 3.8 ou superior.
- **Recomendado: criar um ambiente virtual para isolar as dependências do projeto.**

### Criando Ambiente Virtual

1. Abra o terminal na pasta do projeto.
2. Crie o ambiente virtual:
   - `python -m venv venv`
3. Ative o ambiente:
   - **Windows**: `venv\Scripts\activate`
   - **Linux/macOS**: `source venv/bin/activate`
4. Instale as dependências:
   - `pip install -r requirements.txt`

Para desativar o ambiente virtual, utilize:
- `deactivate.

### Dependências (requirements.txt)

As dependências do projeto devem estar listadas em um arquivo `requirements.txt` com o seguinte conteúdo:
numpy==2.3.5
pandas==2.3.3
python-dateutil==2.9.0.post0
pytz==2025.2
six==1.17.0
tzdata==2025.2


## Como Executar

1. Clone este repositório ou baixe os arquivos.
2. (Opcional, porém recomendado) Crie e ative um ambiente virtual conforme a seção acima.
3. Instale as dependências com:
   - `pip install -r requirements.txt`
4. Execute o script principal:
   - `python analise_vendas.py`

O programa exibirá as análises no console e gerará o arquivo `vendas_analise.csv` com os dados processados.

## Estrutura dos Arquivos

| Arquivo             | Descrição                                       |
|---------------------|-------------------------------------------------|
| `analise_vendas.py` | Script principal com demonstrações Pandas. |
| `vendas_analise.csv`| Dados de saída gerados pelo script.            |
| `requirements.txt`  | Dependências do projeto.                       |
| `README.md`         | Documentação deste projeto.          |

## Autor

Desenvolvido por César Bovo como exemplo educacional para estudos em análise de dados com Pandas.


