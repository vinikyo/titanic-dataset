# ============================================================
# PROJETO: TITANIC - PRÉ-PROCESSAMENTO DE DADOS
# ============================================================
#
# Objetivo desta etapa:
#   - Carregar o dataset Titanic
#   - Conhecer sua estrutura
#   - Identificar valores ausentes
#   - Identificar dados duplicados
#   - Observar estatísticas básicas
#   - Identificar valores categóricos
#
# IMPORTANTE:
# Nesta etapa NÃO vamos modificar os dados.
# Primeiro vamos fazer o diagnóstico do dataset.
# ============================================================

import pandas as pd
import numpy as np

# ============================================================
# 1. CARREGAMENTO DO DATASET
# ============================================================
# Este script é executado de dentro da pasta "scripts",
# por isso o caminho sobe um nível ("..") para achar "dataset/train.csv"
df = pd.read_csv("../dataset/train.csv")

# ============================================================
# 2. VISUALIZAR AS PRIMEIRAS LINHAS
# ============================================================
print("\n===== PRIMEIRAS LINHAS =====")
print(df.head())

# ============================================================
# 3. DIMENSÕES DO DATASET
# ============================================================
print("\n===== DIMENSÕES =====")
print(f"Dimensões: {df.shape}")
print(f"Linhas: {df.shape[0]}")
print(f"Colunas: {df.shape[1]}")

# ============================================================
# 4. NOMES DAS COLUNAS
# ============================================================
print("\n===== COLUNAS =====")
print(df.columns)
print(df.columns.tolist())

# ============================================================
# 5. INFORMAÇÕES SOBRE O DATASET
# ============================================================
print("\n===== INFORMAÇÕES =====")
df.info()

# ============================================================
# 6. IDENTIFICAÇÃO DE VALORES AUSENTES
# ============================================================
print("\n===== VALORES AUSENTES =====")
print(df.isnull().sum())

# ============================================================
# 7. PERCENTUAL DE VALORES AUSENTES
# ============================================================
print("\n===== PERCENTUAL DE VALORES AUSENTES =====")
percentual_ausentes = df.isnull().mean() * 100
missing = pd.DataFrame({
    "Quantidade": df.isnull().sum(),
    "Percentual": percentual_ausentes
})
print(missing)

# ============================================================
# 8. VERIFICAÇÃO DE LINHAS DUPLICADAS
# ============================================================
print("\n===== DUPLICIDADES =====")
quantidade_duplicados = df.duplicated().sum()
print(f"Quantidade de linhas duplicadas: {quantidade_duplicados}")

# ============================================================
# 9. VERIFICAÇÃO DE DUPLICIDADE DO PASSENGERID
# ============================================================
print("\n===== DUPLICIDADE DO PASSENGERID =====")
duplicados_passenger_id = df["PassengerId"].duplicated().sum()
print(f"PassengerId duplicados: {duplicados_passenger_id}")

# ============================================================
# 10. ESTATÍSTICAS DESCRITIVAS
# ============================================================
print("\n===== ESTATÍSTICAS DESCRITIVAS =====")
print(df.describe())

# ============================================================
# 11. ESTATÍSTICAS DAS VARIÁVEIS CATEGÓRICAS
# ============================================================
print("\n===== ESTATÍSTICAS CATEGÓRICAS =====")
print(df.describe(include="object"))

# ============================================================
# 12. VALORES ÚNICOS DA COLUNA SEX
# ============================================================
print("\n===== VALORES ÚNICOS - SEX =====")
print(df["Sex"].unique())

# ============================================================
# 13. VALORES ÚNICOS DA COLUNA EMBARKED
# ============================================================
print("\n===== VALORES ÚNICOS - EMBARKED =====")
print(df["Embarked"].unique())

# ============================================================
# 14. FREQUÊNCIA DA VARIÁVEL SEX
# ============================================================
print("\n===== FREQUÊNCIA - SEX =====")
print(df["Sex"].value_counts())

# ============================================================
# FIM DA ANÁLISE INICIAL
# ============================================================
