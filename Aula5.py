import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Carregar os dados corrigidos do arquivo CSV
file_path = 'caminho_para_o_arquivo_corrigido.csv'
dados_incendios = pd.read_csv(file_path)

# Análise Exploratória Básica
print("Informações Básicas do DataFrame:")
print(dados_incendios.info())

print("\nAlgumas Estatísticas Descritivas:")
print(dados_incendios.describe())

# Análise de dados específicos
# Exemplo: Total de incêndios por estado
total_incendios_por_estado = dados_incendios.groupby('state')['number'].sum().sort_values(ascending=False)
print("\nTotal de Incêndios por Estado:")
print(total_incendios_por_estado)

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