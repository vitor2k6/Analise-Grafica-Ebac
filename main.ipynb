import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

#primeiro passo: leitura do arquivo csv em um dataframe
df = pd.read_csv('ecommerce_estatistica.csv')

#Gráfico De Histograma Com a Coluna Preços
plt.hist(df['Preço'],bins=20, color='blue', edgecolor='black')
plt.title('Distribuição dos Preços dos Produtos')
plt.xlabel('Preço')
plt.ylabel('Frequência')
plt.show()

#Gráfico De Dispersão Entre 'Nota' e 'N_Avaliações'
plt.scatter(df['Nota'],df['N_Avaliações'], alpha=0.5, color='purple')
plt.title('Relação Entre Nota e Números de Avaliação')
plt.xlabel('Nota')
plt.ylabel('Número De Avaliações')
plt.show()

#Selecionando Colunas Para Mapa De Calor
dados_corr = df[['Nota','N_Avaliações','Desconto','Preço','Qtd_Vendidos']].select_dtypes(include='number').dropna()

#Mapa de Calor
plt.figure(figsize=(10,6))
sns.heatmap(dados_corr.corr(), annot=True, cmap='coolwarm', center=0)
plt.title('Mapa De Calor Das Correlações entre Variáveis')
plt.show()

#Gráfico De Barra
df['Marca'].value_counts().plot(kind='bar', color='salmon')
plt.title('Número De Produtos Por Marca')
plt.xlabel('Marca')
plt.ylabel('Quantidade de Produtos')
plt.show()

#Gráfico de Pizza para a distribuição de materiais
df['Material'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90)
plt.title('Distribuição Dos Materiais Dos Produtos')
plt.ylabel('')
plt.show()

#Gráfico De Densidade para coluna Preço
sns.kdeplot(df['Preço'], fill=True, color='green')
plt.title('Densidade De Preço Dos Produtos')
plt.xlabel('Preço')
plt.show()

# Garantindo que as colunas sejam numéricas
df['N_Avaliações'] = pd.to_numeric(df['N_Avaliações'], errors='coerce')
df['Qtd_Vendidos'] = pd.to_numeric(df['Qtd_Vendidos'], errors='coerce')

# Removendo valores NaN nas colunas 'N_Avaliações' e 'Qtd_Vendidos'
df_clean = df[['N_Avaliações', 'Qtd_Vendidos']].dropna()

#Gráfico De Regressão Entre N_Avalições e Qtd Vendidos
sns.regplot(x='N_Avaliações', y='Qtd_Vendidos', data=df_clean, scatter_kws={'alpha':0.5}, line_kws={'color':'red'})
plt.title('Relação Entre Número De Avaliações e Quantidade De Vendidos')
plt.xlabel('Número De Avaliações')
plt.ylabel('Quantidade De Vendidos')
plt.show()