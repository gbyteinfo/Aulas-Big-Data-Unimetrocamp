import pandas as pd
#Padrao para desenvolvimento
print("\n********Análise Exploratória Básica********")
print("*******************************************\n")

# Carregar os dados do arquivo CSV corrigido do GitHub

print("\n********Análise Exploratória Básica********")
dados = "https://raw.githubusercontent.com/Professor-Leonardo/DADOS/main/C%C3%B3pia%20de%20Discrep%C3%A2ncias_MAPGEO2015%20(Dados%20tabelados).csv"
df_ibge = pd.read_csv(dados, sep=';', encoding='ISO-8859-1')
df_ibge.head()
print("*******************************************\n")
# Salvando o gráfico na pasta especificada


