import pandas as pd
import numpy as np
#Exeplo em Aula proposto no exemplo

# Carregar os dados do Titanic
titanic_url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"
titanic_data = pd.read_csv(titanic_url)

# Explorar os dados
print(titanic_data.head())
print(titanic_data.info())

print("\n***********Estatisticas padrao*************")
print(titanic_data.describe())
print("*******************************************\n")

# Traduzir os nomes das colunas
titanic_data.columns = ['PassageiroId', 'Sobreviveu', 'Classe', 'Nome', 'Sexo', 'Idade', 'Id', 'Janela', 'Bilhete', 'Tarifa', 'Cabine', 'Embarcado']
# Exibir os dados traduzidos
print(titanic_data.head())

print("\n*********** Ordenação por sobrevivente *************")
total_passageiros_por_classe = titanic_data.groupby('Classe')['Sobreviveu'].count()
sobreviventes_por_classe = titanic_data.groupby('Classe')['Sobreviveu'].sum()
mortos_por_classe = total_passageiros_por_classe - sobreviventes_por_classe
print(f"Total por Classe por Classe: {total_passageiros_por_classe}")
print(f"Mortos por Classe: {sobreviventes_por_classe}")
print(f"Mortos por Classe: {mortos_por_classe}")
print("*******************************************\n")

print("\n*********** Soma o total does passageirso sobreviventes *************")
#Soma Total de passageiros em cada classe
sobreviventes_por_classe = titanic_data.groupby('Classe')['Sobreviveu'].sum()
print(sobreviventes_por_classe)
print("*******************************************\n")

print("\n*********** Soma o total does passageirso *************")
#Total de passageiro de cada classe
passageiros_por_classe = titanic_data.groupby('Classe')['Sobreviveu'].count()
print(passageiros_por_classe)
print("*******************************************\n")