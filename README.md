# Projeto Titanic — Pré-processamento e Motor de Inferência

## Estrutura de pastas

```
titanic/
├── dataset/
│   └── train.csv                          # dataset do Titanic
├── scripts/
│   ├── 01_diagnostico.py                  # diagnóstico inicial (sem alterar os dados)
│   ├── 02_tratamento_valores_ausentes.py  # dropna / preencher com média / mediana
│   ├── 05_main_decisiontree.py            # roda a inference engine baseada em regras
│   ├── rules/
│   │   └── titanic_rules.py               # REGRAS_TITANIC usadas na inferência
│   └── enginee/
│       └── inference_engine.py            # inferir_primeira / explicar_inferencia
├── requirements.txt
└── README.md
```

> **Atenção ao nome da pasta:** o script `05_main_decisiontree.py` importa de
> `enginee.inference_engine` (com dois "e"). Confirme que a pasta se chama
> exatamente `enginee`, senão o Python não vai encontrar o módulo.

## Passo 1 — Ativar o ambiente virtual e instalar dependências

Na raiz do projeto (`titanic/`):

```
.venv\Scripts\activate      # Windows
# ou
source .venv/bin/activate   # Mac/Linux

pip install -r requirements.txt
```

## Passo 2 — Executar os scripts

Todos os scripts são executados **de dentro da pasta `scripts/`**:

```
cd scripts
python 01_diagnostico.py
python 02_tratamento_valores_ausentes.py
python 05_main_decisiontree.py
```

## O que cada script faz

- **01_diagnostico.py**: carrega o CSV, mostra primeiras linhas, dimensões, colunas, tipos de
  dados, valores ausentes, duplicidades, estatísticas descritivas e valores únicos das
  colunas categóricas. Não altera o dataset.
- **02_tratamento_valores_ausentes.py**: compara três estratégias de tratamento de valores
  ausentes (`dropna`, preencher com média, preencher com mediana), primeiro num exemplo
  didático pequeno e depois na coluna `Age` do Titanic.
- **05_main_decisiontree.py**: monta um dicionário de fatos de um passageiro fictício e roda
  a *inference engine* baseada em regras (`REGRAS_TITANIC`, definidas em
  `scripts/rules/titanic_rules.py`) para inferir e explicar um resultado, usando as funções
  `inferir_primeira` e `explicar_inferencia` de `scripts/enginee/inference_engine.py`.

## Se quiser rodar de outro lugar

Caso não queira entrar na pasta `scripts/`, rode a partir da raiz do projeto passando o
caminho completo:

```
python scripts/01_diagnostico.py
```

Mas cuidado: os caminhos relativos (`../dataset/train.csv` nos scripts 01 e 02) são calculados
a partir de onde você *executa* o comando, não de onde o `.py` está salvo — então rodando
assim, de fora da pasta `scripts/`, o `read_csv` vai quebrar. Prefira sempre `cd scripts`
antes de rodar qualquer um dos scripts.
