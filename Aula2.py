# dadosAula2.txt nomes, sexo, e data de nascimento
# Lendo o arquivo e imprimindo cada linha
dados_simulado = "/root/faculdade/dadosAula2.txt"
with open(dados_simulado, 'r') as arquivo:
    count = 1
    print("\n***********Linhas no arquivo*************")
    for linha in arquivo:
        print(f"Linha{count}...: " + linha.strip())
        count+=1
    count = 0
    print("*******************************************\n")
# Usando o Pandas para ler o arquivo e criar um DataFrame
import pandas as pd

# Lendo os dados do arquivo simulado para o DataFrame
df = pd.read_csv(dados_simulado)

# Exibindo o DataFrame
print("\n*********** Data Frame *************")
print(df)
print("*******************************************\n")

# Exemplos de manipulação de dados com Pandas
print("\n***********Linhas iniciais e padrao*************")
print(df.head())  # Exibe o padrao as linhas iniciais apenas
print(df.head(28))  # Exibe as primeiras linhas
print("*******************************************\n")
print("\n***********Estatisticas padrao*************")
print(df.describe())  # Estatísticas básicas 
print("*******************************************\n")

print("\n***********Ordenação pela coluna*************")
# Ordenando os dados pelo campo "Data de NAscimento"
df['Data de Nascimento']= pd.to_datetime(df['Data de Nascimento'].str.strip() , format='%d-%m-%Y')
df_nome_idx = df.sort_values(by='Data de Nascimento')
# Exibindo o DataFrame ordenado
print(df_nome_idx)
print("*******************************************\n")