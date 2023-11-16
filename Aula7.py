# Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates

#USANDO DADOS FICTICIOS
# Criando um conjunto de dados de exemplo
dados = np.array([85, 92, 78, 94, 89, 110, 45, 75, 82, 99])

# Cálculo da Amplitude
amplitude = np.max(dados) - np.min(dados)
print("Amplitude dos Dados:", amplitude)

# Cálculo da Média
media = np.mean(dados)

# Cálculo da Variância
variancia = np.mean((dados - media) ** 2)
print("Variância dos Dados:", variancia)

# Cálculo do Desvio Padrão
desvio_padrao = np.sqrt(variancia)
print("Desvio Padrão dos Dados:", desvio_padrao)

# Cálculo do IQR
q1 = np.percentile(dados, 25)  # Primeiro quartil (25%)
q3 = np.percentile(dados, 75)  # Terceiro quartil (75%)
iqr = q3 - q1
print("Intervalo Interquartil (IQR):", iqr)



########################################################


#USANDO DADOS TEMPERATURA E MAIS COMPLETO
# Carregar os dados do arquivo CSV do GitHub
print("\n********Manipulando CSV para memoria o Volume de Dados********")
dados_temperatura = pd.read_csv("https://raw.githubusercontent.com/gbyteinfo/Aulas-Big-Data-Unimetrocamp/develop/DataCidadeEstadoTemperatura.csv")
print("*******************************************\n")

print("\n********Análise Exploratória Básica********")
print("### Primeiras linhas do conjunto de dados ###")
print(dados_temperatura.head(10))
print("*******************************************\n")

print("\n*****informações básicas sobre o DataFrame:*****")
print("\n### Informações gerais sobre o conjunto de dados ###")
print(dados_temperatura.info())
print("*******************************************\n")

print("\n*****Algumas Estatísticas Descritivas:*****")
print("\n### Resumo estatístico das variáveis numéricas ###")
print(dados_temperatura.describe())
print("*******************************************\n")


#1° manipulação exploratoria Análise Exploratória de Dados: Grafico Boxplot das temperaturas por estado
plt.figure(figsize=(10, 6))
sns.boxplot(data=dados_temperatura, x='Estado', y='Temperatura')
plt.title('Box Plot das Temperaturas por Estado')
plt.xlabel('Estado')
plt.ylabel('Temperatura (°C)')
#plt.show()
caminho_grafico = '/root/boxplot_temperatura_por_estado.png'
plt.savefig(caminho_grafico)


#2° manipulação exploratoria Gráfico de linha da temperatura ao longo do tempo
# Converter a coluna de Data para o tipo datetime
dados_temperatura['Data'] = pd.to_datetime(dados_temperatura['Data'])
# Configurar o formato dos rótulos do eixo x para exibir apenas o mês/ano
plt.figure(figsize=(12, 6))
sns.lineplot(data=dados_temperatura, x='Data', y='Temperatura', hue='Cidade')
plt.title('Temperatura Diária em Diferentes Cidades')
plt.xlabel('Data de Observação')
plt.ylabel('Temperatura (°C)')
plt.xticks(rotation=45)
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m/%Y')) # Formato de mês/ano
#plt.show()
caminho_grafico = '/root/lines_temperatura_por_mes_ano.png'
plt.savefig(caminho_grafico)


#3° Cálculo de Estatísticas das Temperaturas
media_temperatura = dados_temperatura['Temperatura'].mean()
mediana_temperatura = dados_temperatura['Temperatura'].median()
variancia_temperatura = dados_temperatura['Temperatura'].var()
desvio_padrao_temperatura = dados_temperatura['Temperatura'].std()
Q1 = dados_temperatura['Temperatura'].quantile(0.25)
Q3 = dados_temperatura['Temperatura'].quantile(0.75)
IQR_temperatura = Q3 - Q1

print("\n### Estatísticas das Temperaturas ###")
print("Média:", media_temperatura)
print("Mediana:", mediana_temperatura)
print("Variância:", variancia_temperatura)
print("Desvio Padrão:", desvio_padrao_temperatura)
print("Intervalo Interquartil (IQR):", IQR_temperatura)
