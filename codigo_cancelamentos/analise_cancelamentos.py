import pandas as pd
import plotly.express as px

# ============================================
# PASSO 1: IMPORTAR A BASE DE DADOS
# ============================================
tabela = pd.read_csv("cancelamentos_sample.csv")

# ============================================
# PASSO 2: VISUALIZAR A BASE DE DADOS
# ============================================
tabela = tabela.drop(columns="CustomerID")
print(tabela)

# ============================================
# PASSO 3: CORRIGIR OS DADOS
# ============================================
print(tabela.info())
tabela = tabela.dropna()
print(tabela.info())

# ============================================
# PASSO 4: ANÁLISE DOS CANCELAMENTOS
# ============================================
print(tabela["cancelou"].value_counts())
print(tabela["cancelou"].value_counts(normalize=True))

# ============================================
# PASSO 5: ANÁLISE DAS CAUSAS DOS CANCELAMENTOS
# ============================================
for coluna in tabela.columns:
    grafico = px.histogram(tabela, x=coluna, color="cancelou")
    grafico.show()