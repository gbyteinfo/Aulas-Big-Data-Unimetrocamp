import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
from bokeh.plotting import figure, show, output_notebook
import altair as alt

# Carregar dados de incêndios florestais
url = "https://raw.githubusercontent.com/gbyteinfo/Aulas-Big-Data-Unimetrocamp/develop/dados_incendios_brasil.csv"
df_incendios = pd.read_csv(url)

# Gráfico de Linha (Matplotlib): Total de Incêndios por Ano
incendios_por_ano = df_incendios.groupby('year')['number'].sum()
plt.figure(figsize=(10, 6))
plt.plot(incendios_por_ano.index, incendios_por_ano.values, marker='o', color='r')
plt.xlabel('Ano')
plt.ylabel('Total de Incêndios')
plt.title('Total de Incêndios Florestais por Ano no Brasil')
plt.grid(True)
plt.show()

# Gráfico de Barras (Seaborn): Total de Incêndios por Estado
total_incendios_por_estado = df_incendios.groupby('state')['number'].sum().sort_values(ascending=False)
plt.figure(figsize=(12, 8))
sns.barplot(x=total_incendios_por_estado.values, y=total_incendios_por_estado.index, palette='viridis')
plt.xlabel('Total de Incêndios')
plt.ylabel('Estado')
plt.title('Total de Incêndios Florestais por Estado no Brasil')
plt.show()

# Gráfico 3D (Plotly): Incêndios por Estado e Ano
fig = px.scatter_3d(df_incendios, x='year', y='state', z='number',
                    color='number', size='number',
                    title='Incêndios Florestais por Estado e Ano no Brasil')
fig.show()

# Gráfico de Linha Interativo (Bokeh): Incêndios por Ano
output_notebook()
p = figure(title="Incêndios Florestais por Ano no Brasil", x_axis_label='Ano', y_axis_label='Total de Incêndios', x_axis_type='datetime')
p.line(incendios_por_ano.index, incendios_por_ano.values, legend_label='Total de Incêndios', line_width=2)
show(p)

# Gráfico de Dispersão (Altair): Incêndios por Estado e Ano
alt.Chart(df_incendios).mark_circle(size=60).encode(
    x='year:O',
    y='state',
    size='number',
    color='number',
    tooltip=['year', 'state', 'number']
).properties(
    title='Incêndios Florestais por Estado e Ano no Brasil'
).interactive()

# Histograma (Pandas Plotting): Distribuição de Incêndios
df_incendios['number'].plot(kind='hist', bins=30, title='Distribuição de Incêndios Florestais no Brasil')
plt.xlabel('Número de Incêndios')
plt.show()
