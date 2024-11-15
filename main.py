import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import io
import base64
import matplotlib
matplotlib.use('agg')

#primeiro passo: leitura do arquivo csv em um dataframe
df = pd.read_csv('ecommerce_estatistica.csv')

# Garantindo que as colunas sejam numéricas
df['N_Avaliações'] = pd.to_numeric(df['N_Avaliações'], errors='coerce')
df['Qtd_Vendidos'] = pd.to_numeric(df['Qtd_Vendidos'], errors='coerce')

#Selecionando Colunas Para Mapa De Calor
dados_corr = df[['Nota','N_Avaliações','Desconto','Preço','Qtd_Vendidos']].select_dtypes(include='number').dropna()

#inicializar a aplicação dash
app = dash.Dash(__name__)

#layout da aplicação
app.layout = html.Div([
    html.H1("Visualização De Dados E-commerce"),

    #Dropdown para selecionar o tipo de Gráfico
    dcc.Dropdown(
        id='dropdown-grafico',
        options=[
            {'label': 'Histograma de Preço', 'value': 'histograma'},
            {'label': 'Gráfico de Dispersão (Nota x N_Avaliações)', 'value': 'dispersão'},
            {'label': 'Mapa de Calor', 'value': 'mapa_calor'},
            {'label': 'Gráfico de Barra (Produto Por Marca)', 'value': 'barra'},
            {'label': 'Gráfico de Pizza (Distribuição de Materiais)', 'value': 'pizza'},
            {'label': 'Gráfico de Densidade (Preço)', 'value': 'densidade'},
            {'label': 'Gráfico de Regressão (N_Avaliações x Qtd_Vendidos)', 'value': 'regressão'}
        ],
        value='histograma'
    ),

    #componente para exibir o gráfico
    html.Img(id='grafico-img')
])

#função para converter o gráfico matplotlib para base64
def fig_to_base64():
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    return base64.b64encode(buf.read()).decode('utf-8')

#Callback para atualizar o gráfico com base na seleção do usuário
@app.callback(
    Output('grafico-img', 'src'),
    [Input('dropdown-grafico', 'value')]
)
def atualizar_grafico(tipo_grafico):
    # Limpar o gráfico anterior
    plt.clf()

    # Gráfico De Histograma Com a Coluna Preços
    if tipo_grafico == 'histograma':
        plt.hist(df['Preço'],bins=20, color='blue', edgecolor='black')
        plt.title('Distribuição dos Preços dos Produtos')
        plt.xlabel('Preço')
        plt.ylabel('Frequência')

    #Gráfico De Dispersão Entre 'Nota' e 'N_Avaliações'
    elif tipo_grafico == 'dispersão':
        plt.scatter(df['Nota'],df['N_Avaliações'], alpha=0.5, color='purple')
        plt.title('Relação Entre Nota e Números de Avaliação')
        plt.xlabel('Nota')
        plt.ylabel('Número De Avaliações')

    #Mapa de Calor
    elif tipo_grafico == 'mapa_calor':
        plt.figure(figsize=(10,6))
        sns.heatmap(dados_corr.corr(), annot=True, cmap='coolwarm', center=0)
        plt.title('Mapa De Calor Das Correlações entre Variáveis')

    #Gráfico De Barra
    elif tipo_grafico == 'barra':
        df['Marca'].value_counts().plot(kind='bar', color='salmon')
        plt.title('Número De Produtos Por Marca')
        plt.xlabel('Marca')
        plt.ylabel('Quantidade de Produtos')

    #Gráfico de Pizza para a distribuição de materiais
    elif tipo_grafico == 'pizza':
        df['Material'].value_counts().plot(kind='pie', autopct='%1.1f%%', startangle=90)
        plt.title('Distribuição Dos Materiais Dos Produtos')
        plt.ylabel('')

    #Gráfico De Densidade para coluna Preço
    elif tipo_grafico == 'densidade':
        sns.kdeplot(df['Preço'], fill=True, color='green')
        plt.title('Densidade De Preço Dos Produtos')
        plt.xlabel('Preço')

    #Gráfico De Regressão Entre N_Avalições e Qtd Vendidos, Removendo valores NaN nas colunas 'N_Avaliações' e 'Qtd_Vendidos'
    elif tipo_grafico == 'regressão':
        df_clean = df[['N_Avaliações', 'Qtd_Vendidos']].dropna()
        sns.regplot(x='N_Avaliações', y='Qtd_Vendidos', data=df_clean, scatter_kws={'alpha':0.5}, line_kws={'color':'red'})
        plt.title('Relação Entre Número De Avaliações e Quantidade De Vendidos')
        plt.xlabel('Número De Avaliações')
        plt.ylabel('Quantidade De Vendidos')

    # converter o gráfico para base64
    img_base64 = fig_to_base64()
    return f'data:image/png;base64,{img_base64}'

#executar o servidor
if __name__ == '__main__':
    app.run_server(debug=True)