import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Conectar ao banco de dados (ou criar um novo)
conn = sqlite3.connect('Incendios_Brasil.db')

# Criar a tabela "incendios" (se ela não existir)
conn.execute('''
    CREATE TABLE IF NOT EXISTS TB_INCENDIOS (
        id INTEGER PRIMARY KEY,
        DB_ANO INTEGER,
        DB_ESTADO TEXT,
        DB_MES TEXT,
        DB_NUMERO REAL,
        DB_DATA TEXT
    )
''')

# Carregar os dados do arquivo CSV do GitHub
url = "https://raw.githubusercontent.com/gbyteinfo/Aulas-Big-Data-Unimetrocamp/develop/dados_incendios_brasil.csv"
df_incendios = pd.read_csv(url)

# Preparar os dados para inserção (exemplo simplificado)
df_incendios['id'] = df_incendios.index

# Alterar o nome das colunas para salvar em base
df_incendios.columns = ['Ano', 'Estado', 'Mes', 'Numero', 'Data', 'Id']

# Inserir os dados na tabela "incendios"
df_incendios.to_sql('TB_INCENDIOS', conn, if_exists='replace', index=False)

# Consultar os registros inseridos para verificar se foram adicionados corretamente
query = "SELECT * FROM TB_INCENDIOS"
df_consulta = pd.read_sql_query(query, conn)

print("\n********Análise Exploratória Básica********")
print(df_consulta.head(50))
print("*******************************************\n")

# Fechar a conexão com o banco de dados
conn.close()


################### Dados Esploratórios #####################


print("\n********Exibir os primeiros registros do DataFrame********")
print(df_consulta.head())
print("*******************************************\n")

print("\n*****informações básicas sobre o DataFrame:*****")
print(df_consulta.info())
print("*******************************************\n")

print("\n*****Algumas Estatísticas Descritivas:*****")
print(df_consulta.describe())
print("*******************************************\n")

# Visualização dos Dados
# Gráfico de barras: Total de Incêndios por Estado
total_incendios_por_estado = df_consulta.groupby('Estado')['Numero'].sum().sort_values(ascending=False)
plt.figure(figsize=(12, 6))
total_incendios_por_estado.plot(kind='bar', color='firebrick')
plt.title('Total de Incêndios por Estado')
plt.xlabel('Estado')
plt.ylabel('Total de Incêndios')
plt.xticks(rotation=90)
#plt.show()
caminho_grafico = '/root/figure_insendios_florestais_estado_aula7.png'
plt.savefig(caminho_grafico)


# Box Plot: Distribuição de Incêndios por Estado
plt.figure(figsize=(12, 6))
sns.boxplot(x='Estado', y='Numero', data=df_consulta)
plt.title('Distribuição de Incêndios por Estado')
plt.xlabel('Estado')
plt.ylabel('Número de Incêndios')
plt.xticks(rotation=90)
#plt.show()
caminho_grafico = '/root/boxplot_insendios_florestais_aula7.png'
plt.savefig(caminho_grafico)

# Gráfico de linha: Incêndios ao longo dos anos
incendios_por_ano = df_consulta.groupby('Ano')['Numero'].sum()
plt.figure(figsize=(12, 6))
incendios_por_ano.plot(kind='line', color='orange')
plt.title('Incêndios ao Longo dos Anos')
plt.xlabel('Ano')
plt.ylabel('Total de Incêndios')
#plt.show()
caminho_grafico = '/root/figure_insendios_florestais_aula7_anos.png'
plt.savefig(caminho_grafico)
