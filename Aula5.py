import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados do arquivo CSV corrigido do GitHub = 245 KB (250.934 bytes) de dados
url = "https://raw.githubusercontent.com/gbyteinfo/Aulas-Big-Data-Unimetrocamp/develop/dados_incendios_brasil.csv"
dados_incendios = pd.read_csv(url)

print("\n********Análise Exploratória Básica********")
print(dados_incendios.info())
print("*******************************************\n")

print("\n*****Algumas Estatísticas Descritivas:*****")
print(dados_incendios.describe())
print("*******************************************\n")

print("\n*****Total de incêndios por estado:*****")
# Exemplo: Total de incêndios por estado
total_incendios_por_estado = dados_incendios.groupby('state')['number'].sum().sort_values(ascending=False)
print("\nTotal de Incêndios por Estado:")
print(total_incendios_por_estado)
print("*******************************************\n")


##########################Grafico#########################

# Visualização: Gráfico de Barras do Total de Incêndios por Estado
plt.figure(figsize=(12, 6))
sns.barplot(x=total_incendios_por_estado.index, y=total_incendios_por_estado.values)
plt.xticks(rotation=90)
plt.xlabel('Estado')
plt.ylabel('Total de Incêndios')
plt.title('Total de Incêndios por Estado no Brasil')

# Salvando o gráfico na pasta especificada
caminho_grafico = '/root/faculdade/total_incendios_por_estado.png'
plt.savefig(caminho_grafico)

# Exibindo o gráfico
plt.show()
