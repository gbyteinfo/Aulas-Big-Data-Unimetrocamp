#Imports
import pandas as pd


# Carregar os dados do arquivo CSV do GitHub
print("\n********Manipulando CSV para memoria o Volume de Dados********")
dados = "https://raw.githubusercontent.com/gbyteinfo/Aulas-Big-Data-Unimetrocamp/develop/DataCidadeEstadoTemperatura.csv"
df_csv = pd.read_csv(dados, sep=';', encoding='ISO-8859-1')
print("*******************************************\n")

print("\n********Análise Exploratória Básica********")
print(df_csv.head(10))
print("*******************************************\n")

print("\n*****informações básicas sobre o DataFrame:*****")
print(df_csv.info())
print("*******************************************\n")

print("\n*****Algumas Estatísticas Descritivas:*****")
print(df_csv.describe())
print("*******************************************\n")


# Carregar os dados do arquivo XLSX do GitHub
print("\n********Manipulando XLSX para memoria o Volume de Dados********")
url_excel = "https://github.com/gbyteinfo/Aulas-Big-Data-Unimetrocamp/raw/develop/DataCidadeEstadoTemperatura.xlsx"
df_excel = pd.read_excel(url_excel)
print("*******************************************\n")

print("\n********Análise Exploratória Básica********")
print(df_excel.head(10))
print("*******************************************\n")

print("\n*****informações básicas sobre o DataFrame:*****")
print(df_excel.info())
print("*******************************************\n")

print("\n*****Algumas Estatísticas Descritivas:*****")
print(df_excel.describe())
print("*******************************************\n")



