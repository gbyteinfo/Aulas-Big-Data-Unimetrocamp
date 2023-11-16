import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Função para criar a tabela de incêndios florestais
def criar_tabela():
    # Conectar ao banco de dados (ou criar um novo)
    conn = sqlite3.connect('Incendios_Brasil.db')
    cursor = conn.cursor()
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
    df_incendios['id'] = df_incendios.index
    df_incendios.columns = ['DB_ANO', 'DB_ESTADO', 'DB_MES', 'DB_NUMERO', 'DB_DATA', 'Id']
    df_incendios.to_sql('TB_INCENDIOS', conn, if_exists='replace', index=False)

    conn.commit()
    conn.close()

# Função para inserir um novo registro na tabela de incêndios florestais
def inserir_dados(Ano, Estado, Mes, Numero, Data):
    conn = sqlite3.connect("Incendios_Brasil.db")
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO TB_INCENDIOS (DB_ANO, DB_ESTADO, DB_MES, DB_NUMERO, DB_DATA)
    VALUES (?, ?, ?, ?, ?)
    ''', (Ano, Estado, Mes, Numero, Data))
    conn.commit()
    conn.close()
    print(f"\nDados Inseridos: Ano:{Ano} - Estado:{Estado} - Mes:{Mes} - Numero:{Numero} - Data{Data}")

# Função para excluir um registro da tabela de incêndios florestais por ID
def excluir_dados(id):
    conn = sqlite3.connect("Incendios_Brasil.db")
    cursor = conn.cursor()
    cursor.execute('DELETE FROM TB_INCENDIOS WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    print(f"\nDados excluidos id: {id}")
    
# Função para listar todos os registros
def listar_dados():
    conn = sqlite3.connect("Incendios_Brasil.db")
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM TB_INCENDIOS')
    registros = cursor.fetchall()
    for registro in registros:
        print(f"registro:{registro}")
    conn.close()

# Cria a tabela se ela não existir
criar_tabela()

# Exemplo de inserção de um registro
inserir_dados(2023, "São PauloHortolandia", "Janeiro", 150, "01-01-2023")

# Exclusão do registro
excluir_dados(1)

# Listar dados para verificar
listar_dados()
