import pyspark
import matplotlib.pyplot as plt

spark = pyspark.sql.SparkSession.builder.getOrCreate()

# Carregar o DataFrame com Dados de Incêndios Florestais
df_incendios = spark.read.csv('dados_incendios_brasil.csv', inferSchema=True, header=True)

# Selecionar colunas específicas
df_incendios.select("year", "state", "number").show()

# Filtrar por número de incêndios maior que um limiar
df_incendios.filter(df_incendios.number > 100).show()

# Agrupar por estado e calcular a média de incêndios
df_incendios.groupBy("state").avg("number").show()

# Converter o resultado para Pandas DataFrame
df_estado_media = df_incendios.groupBy("state").avg("number").toPandas()

# Criar um gráfico de barras
plt.figure(figsize=(12, 6))
plt.bar(df_estado_media["state"], df_estado_media["avg(number)"])
plt.xlabel("Estado")
plt.ylabel("Média de Incêndios")
plt.title("Média de Incêndios Florestais por Estado no Brasil")
plt.xticks(rotation=90)
plt.show()