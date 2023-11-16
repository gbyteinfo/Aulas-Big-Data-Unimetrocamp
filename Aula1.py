
print("Olá, mundo!\n")


# 2. Variáveis
mensagem = "Olá, Python!"
print(mensagem + "\n")


# 3. Tipos de Dados Básicos
inteiro = 10
ponto_flutuante = 3.14
texto = "Isso é uma string\n"
booleano = True


# 4. Entrada do Usuário (removido para esta execução)
nome = input("Digite o seu nome: ")
idade = input("Agora digite sua idade: ")
print(f"Olá, {nome}, você tem {idade} anos de idade!\n")


# 5. Estruturas de Controle
if int(idade) >= 18:
    print(f"Você é maior de idade. Voce tem {idade}\n")
else:
    print(f"Você é menor de idade.Voce tem {idade}\n")

# Laços de repetição (for, while)
for i in range(int(idade)):
    print(f"Ano:{i}")
print("\n")

#Contador 
contador = 0
while contador < int(idade):
    print(contador)
    contador += 1
print("\n")

# 6. Listas
frutas = ["Jorge", "Guilherme", "Gabriel", "Marisa"]
print(frutas[0])  # Acessando o primeiro item
frutas.append("Beatriz")  # Adicionando um item

# 7. Funções
def tabuada_do_1_10():
    print("***************Tabuada do 1 ao 10***************")
    for multiplicando in range(1, 11):  # estiver entre 1 e 10
        print(f"***************Tabuada do {multiplicando}***************")
        for multiplicador in range(0, 11):
            produto = multiplicando * multiplicador
            print(f"{multiplicando} X {multiplicador} = {produto}")
        print(f"*************** Fim ***************")

tabuada_do_1_10() # Chama a função