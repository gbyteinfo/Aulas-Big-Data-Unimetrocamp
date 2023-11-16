import pandas as pd
from IPython.display import display

#AGORA COM DISPLAY O QUE DA UMA MELHOR FORMATAÇÃO MAS NO COLAB O TERMINAL DO VS CONDE É MUITO RUIM PARA AS FORMATAÇÕES

print("\n*********** Catalogo dados abertos *************")
# 1. Carregar um catálogo de dados abertos no Brasil
url_dados_brasil = "https://raw.githubusercontent.com/dadosgovbr/catalogos-dados-brasil/master/dados/catalogos.csv"
dados_brasil = pd.read_csv(url_dados_brasil)
dados_brasil.columns = ['Tituloo', 'Urll', 'Municípioo', 'Uff', 'Esferaa', 'Poderr', 'Soluçãoo'] # alterando colunas
#print("Catálogo de Dados Abertos no Brasil:\n", dados_brasil.head(10))
display(dados_brasil.head(10))
display(dados_brasil.describe())
print("*******************************************\n")

print("\n*********** Aplicativos que usam dados governamentais *************")
# 2. Carregar dados sobre aplicativos que usam dados abertos governamentais no Brasil
url_outros_dados = "https://raw.githubusercontent.com/dadosgovbr/aplicativos-dados-brasil/master/dados/aplicativos.csv"
outros_brasil = pd.read_csv(url_outros_dados)
#print("\nAplicativos que Usam Dados Abertos Governamentais:\n", outros_brasil.head(10))
display(outros_brasil.head(10))
print("\n")
display(outros_brasil.describe())
print("*******************************************\n")

print("\n*********** Dados do covid19 no Brasil *************")
# 3. Carregar dados de COVID-19 no Brasil
url_covid_brasil = "https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-states.csv"
dados_covid = pd.read_csv(url_covid_brasil)
#print("\nDados de COVID-19 no Brasil:\n", dados_covid.head())
display(dados_covid.head(10))
display(dados_covid.describe())
print("*******************************************\n")

print("\n*********** Exemplo de uso do try para casos de incerteza da disponibilidade dos dados  *************")
# 4. Carregar dados de desmatamento na Amazônia (exemplo hipotético, link pode estar incorreto)
url_desmatamento_amazonia = "https://raw.githubusercontent.com/riscoprodutivo/desmatamento/master/amazonia_desmatamento.csv"
try:
    dados_desmatamento = pd.read_csv(url_desmatamento_amazonia, sep=';', encoding='latin1')
    print("\nDados de Desmatamento na Amazônia:\n", dados_desmatamento.head())
except Exception as e:
    print("\nErro ao carregar dados de desmatamento na Amazônia:", e)
print("*******************************************\n")

