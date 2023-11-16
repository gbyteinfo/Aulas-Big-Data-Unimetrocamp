#Imports
import pandas as pd


# Carregar os dados do arquivo CSV do GitHub
print("\n********Manipulando CSV para memoria o Volume de Dados********")
dados = "https://raw.githubusercontent.com/Professor-Leonardo/DADOS/main/C%C3%B3pia%20de%20Discrep%C3%A2ncias_MAPGEO2015%20(Dados%20tabelados).csv"
df_csv = pd.read_csv(dados, sep=';', encoding='ISO-8859-1')
print("*******************************************\n")

print("\n********Análise Exploratória Básica********")
print(df_csv.head())
print("*******************************************\n")

print("\n*****informações básicas sobre o DataFrame:*****")
print(df_csv.info())
print("*******************************************\n")

print("\n*****Algumas Estatísticas Descritivas:*****")
print(df_csv.describe())
print("*******************************************\n")


# Carregar os dados do arquivo XLSX do GitHub
print("\n********Manipulando XLSX para memoria o Volume de Dados********")
url_excel = "https://raw.githubusercontent.com/Professor-Leonardo/DADOS/main/C%C3%B3pia%20de%20Discrep%C3%A2ncias_MAPGEO2015%20(Dados%20tabelados).xlsx"
df_excel = pd.read_excel(url_excel)
print("*******************************************\n")

print("\n********Análise Exploratória Básica********")
print(df_excel.head())
print("*******************************************\n")

print("\n*****informações básicas sobre o DataFrame:*****")
print(df_excel.info())
print("*******************************************\n")

print("\n*****Algumas Estatísticas Descritivas:*****")
print(df_excel.describe())
print("*******************************************\n")



