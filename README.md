# Projeto Titanic — Pré-processamento de Dados

## Estrutura de pastas

```
titanic/
├── dataset/
│   └── train.csv                          # dataset do Titanic
├── scripts/
│   ├── 01_diagnostico.py                  # diagnóstico inicial (sem alterar os dados)
│   └── 02_tratamento_valores_ausentes.py  # dropna / preencher com média / mediana
├── requirements.txt
└── README.md
```

## Passo 1 — Instalar as dependências

Abra o terminal na pasta `titanic/` e rode:

```bash
pip install -r requirements.txt
```

(se preferir usar um ambiente virtual, crie antes com `python -m venv venv` e ative com
`venv\Scripts\activate` no Windows ou `source venv/bin/activate` no Mac/Linux)

## Passo 2 — Executar os scripts

Os scripts esperam ser executados **de dentro da pasta `scripts/`**, pois usam o caminho
relativo `../dataset/train.csv` para achar o CSV. Então:

```bash
cd scripts
python 01_diagnostico.py
```

e depois:

```bash
python 02_tratamento_valores_ausentes.py
```

Cada script imprime os resultados direto no terminal — não precisa de mais nada para testar.

## Se quiser rodar de outro lugar

Caso não queira entrar na pasta `scripts/`, rode a partir da raiz do projeto passando o caminho
completo do arquivo, por exemplo:

```bash
python scripts/01_diagnostico.py
```

Só que aí o `pd.read_csv("../dataset/train.csv")` vai quebrar, porque o caminho relativo é
calculado a partir de onde você *executa* o comando, não de onde o arquivo `.py` está salvo.
Duas opções:
- sempre rode com `cd scripts` antes (mais simples), **ou**
- troque o caminho dentro dos scripts para `"dataset/train.csv"` (sem o `../`) e sempre rode a
  partir da raiz do projeto (`titanic/`).

## O que cada script faz

- **01_diagnostico.py**: carrega o CSV, mostra as primeiras linhas, dimensões, colunas, tipos de
  dados, valores ausentes (quantidade e percentual), duplicidades, estatísticas descritivas e
  valores únicos de colunas categóricas. Não altera o dataset.
- **02_tratamento_valores_ausentes.py**: mostra três estratégias para lidar com valores ausentes
  (excluir linhas com `dropna`, preencher com a média, preencher com a mediana), primeiro com um
  exemplo didático pequeno e depois aplicando na coluna `Age` do Titanic, comparando o tamanho do
  dataset resultante em cada abordagem.
