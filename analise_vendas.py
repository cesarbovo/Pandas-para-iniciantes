"""
PROGRAMA DE ANÁLISE DE VENDAS COM PANDAS
=========================================
Demonstra os conceitos principais do pandas de forma didática
Autor: César Bovo
"""

import pandas as pd
import numpy as np

# ============================================================================
# 1. CRIAR DADOS - Simulando um dataset de vendas de uma loja
# ============================================================================
print("=" * 70)
print("1. CRIANDO DADOS - DataFrame com informações de vendas")
print("=" * 70)

# Criando dados com dicionário (forma mais intuitiva)
dados_vendas = {
    'Produto': ['Notebook', 'Mouse', 'Teclado', 'Monitor', 'Webcam', 'Fone', 'Notebook', 'Mouse'],
    'Categoria': ['Eletrônico', 'Periférico', 'Periférico', 'Eletrônico', 'Periférico', 'Periférico', 'Eletrônico', 'Periférico'],
    'Preço': [3500, 80, 250, 1200, 350, 150, 3500, 80],
    'Quantidade': [2, 10, 8, 3, 5, 4, 1, 20],
    'Vendedor': ['Ana', 'Carlos', 'Ana', 'Bruno', 'Carlos', 'Bruno', 'Ana', 'Carlos']
}

# Criar o DataFrame
df = pd.DataFrame(dados_vendas)

print("\n📊 DataFrame criado com sucesso!")
print(df)
print(f"\nDimensões: {df.shape[0]} linhas, {df.shape[1]} colunas")


# ============================================================================
# 2. EXPLORAR DADOS - Conhecer a estrutura
# ============================================================================
print("\n" + "=" * 70)
print("2. EXPLORANDO OS DADOS - Estrutura e tipos")
print("=" * 70)

print("\n📋 Informações do DataFrame:")
print(df.info())

print("\n📊 Estatísticas descritivas (colunas numéricas):")
print(df.describe())

print("\n🔍 Primeiras 3 linhas:")
print(df.head(3))


# ============================================================================
# 3. CRIAR COLUNA NOVA - Calcular receita (Preço × Quantidade)
# ============================================================================
print("\n" + "=" * 70)
print("3. CRIANDO NOVA COLUNA - Calcular receita por linha")
print("=" * 70)

df['Receita'] = df['Preço'] * df['Quantidade']

print("\n✅ Coluna 'Receita' criada!")
print(df[['Produto', 'Preço', 'Quantidade', 'Receita']])


# ============================================================================
# 4. FILTRAR DADOS - Encontrar vendas acima de R$ 1000
# ============================================================================
print("\n" + "=" * 70)
print("4. FILTRANDO DADOS - Vendas com receita > R$ 1000")
print("=" * 70)

vendas_altas = df[df['Receita'] > 1000]

print(f"\n🎯 Encontrados {len(vendas_altas)} registros:")
print(vendas_altas[['Produto', 'Quantidade', 'Receita']])


# ============================================================================
# 5. AGRUPAR DADOS - Receita por vendedor e categoria
# ============================================================================
print("\n" + "=" * 70)
print("5. AGRUPANDO DADOS - Receita total por vendedor")
print("=" * 70)

receita_vendedor = df.groupby('Vendedor')['Receita'].sum().sort_values(ascending=False)

print("\n💰 Receita por vendedor (em ordem decrescente):")
print(receita_vendedor)

print("\n💰 Receita por categoria:")
receita_categoria = df.groupby('Categoria')['Receita'].sum()
print(receita_categoria)


# ============================================================================
# 6. ANÁLISES ESTATÍSTICAS
# ============================================================================
print("\n" + "=" * 70)
print("6. ANÁLISES ESTATÍSTICAS")
print("=" * 70)

print(f"\n💵 Receita total: R$ {df['Receita'].sum():,.2f}")
print(f"📈 Receita média por venda: R$ {df['Receita'].mean():,.2f}")
print(f"🔝 Maior receita: R$ {df['Receita'].max():,.2f}")
print(f"🔻 Menor receita: R$ {df['Receita'].min():,.2f}")
print(f"📊 Quantidade total de produtos vendidos: {df['Quantidade'].sum()}")


# ============================================================================
# 7. ORDENAR DADOS - Produtos mais vendidos
# ============================================================================
print("\n" + "=" * 70)
print("7. ORDENANDO DADOS - Produtos por quantidade (maior → menor)")
print("=" * 70)

top_produtos = df.sort_values('Quantidade', ascending=False)[['Produto', 'Quantidade', 'Receita']]
print(top_produtos)


# ============================================================================
# 8. CONTAR VALORES ÚNICOS - Diversidade de dados
# ============================================================================
print("\n" + "=" * 70)
print("8. ANÁLISE DE DIVERSIDADE")
print("=" * 70)

print(f"\n📦 Quantidade de produtos diferentes: {df['Produto'].nunique()}")
print(f"👥 Quantidade de vendedores: {df['Vendedor'].nunique()}")
print(f"🏷️ Quantidade de categorias: {df['Categoria'].nunique()}")

print("\n📋 Vendedores e quantos produtos cada um vendeu:")
print(df['Vendedor'].value_counts())


# ============================================================================
# 9. SALVAR RESULTADO - Exportar para CSV
# ============================================================================
print("\n" + "=" * 70)
print("9. SALVANDO DADOS - Exportar para arquivo CSV")
print("=" * 70)

df.to_csv('vendas_analise.csv', index=False, encoding='utf-8')
print("✅ Dados salvos em 'vendas_analise.csv'")


# ============================================================================
# 10. RESUMO FINAL
# ============================================================================
print("\n" + "=" * 70)
print("📌 RESUMO DAS OPERAÇÕES PANDAS DEMONSTRADAS")
print("=" * 70)

resumo = """
✓ Criar DataFrame a partir de dicionário
✓ Explorar dados (shape, info, describe)
✓ Acessar primeiras linhas (head)
✓ Criar novas colunas com operações
✓ Filtrar dados com condições
✓ Agrupar dados (groupby)
✓ Ordenar dados (sort_values)
✓ Cálculos estatísticos (sum, mean, max, min)
✓ Contar valores únicos (nunique, value_counts)
✓ Exportar para arquivo (to_csv)
"""
print(resumo)

print("=" * 70)
print("✨ Análise completa!")
print("=" * 70)
