import numpy as np
import pandas as pd
import folium

# x_min, x_mas = 5, 15
# x= np.linspace(start=x_min, stop=x_mas, num=6)
# print(f'x: {x}')
# print(f'shape: {x.shape}')
# print(x[-1])  # para acessar o ultimo elemento de um array de uma linha
# print(x[-2:])  # Dois elementos de tras para frente!
#
# # Criação de matriz indentidade
#
# n = 4
# x =np.eye(n)
# print(f'x:\n {x}')
# print(f'Shape: {x.shape}')

# https://archive.ics.uci.edu/autos/imports-85.data
# url = "https://raw.githubusercontent.com/wcota/covid19br/master/cases-brazil-total.csv"
# df = pd.read_csv(url, header=None)  # Comando header=Nome serve para ignorar o cabeçalho
# print(df.dtypes)
# print(df.describe(include="all"))
# print(df.header(1))
# print(df.tail(5))
# path = "C:/Users/JotaCarlos/Desktop/Pynton/teste.csv"
# df.to_csv(path)

# x = np.ones((2, 2))
# y = np.eye(2)
# print(f'X:\n{x}')
# print(f'Y: \n{y}')
# print(f'SOma de dois arrays:\n{x+y}')
# print(f'Multiplicação matricial \n{np.dot(x, y)}')
# print(f'Multiplicação matricial \n{x @ y}')
# print(f'Multiplicação matricial \n{x.dot(y)}')
# a = np.array([1, 2, 3])
# b = np.array([2, 0, 3])
# s = 3
# print(a == b)
# print(a == s)
# cond = a <= 0
# d = a[cond]  # Copia os valores em que as condição de verificação se aplica
# print(f'Condição: {cond}')
# print(f'D: {d}')

# indexação booleana
x = np.array([[1, 3, 7],
             [4, 11, 21],
             [42, 8, 9]])
# Retorna o número de elementos maiores que K
k = 10
cond = x > k
print(f'Condição: \n {cond}')
print(f'Elementos maiores que {k}, {x[cond]}')
print(f'números de elementos maiores que {k}, {len(x[cond])}')

# Indexação booleana: extração dos números pares
cond = x % 2 == 0  # Números pares
print(f'condição: \n, {cond}')
print(f'números pares: {x[cond]}')

# reshape transforma a matriz em um vetor coluna
# (3, 3) vira (9, 1) ou (1, 9) para colocar em linha
print(f'Transformação de um vetor em coluna {x.reshape(9, 1)}')
print(f'Transformação em vetor linha: {x.reshape(1, 9)}')

# Transposição da matriz transforma linha em coluna
print(f'X Transposta: \n{x.T}')

# soma de uma dado eixo axis {0 = Linha, 1 = cpluna}
print(f'soma de todos os elementos: {np.sum(x)}')
print(f'soma de ao longo das linhas: {np.sum(x, axis=0)}')
print(f'soma ao longo da colunas: {np.sum(x, axis=1)}')

# media em um dado eixo, axis = {0=Linha, 1=coluna}
print(f'média de todos os elementos: {np.mean(x)}')
print(f'média de x ao longo das linha: {np.mean(x, axis=0)}')
print(f'média de x ao longo das colunas: {np.mean(x, axis=1)}')

# Visualização de dados
import matplotlib.pyplot as plt

x = [-1., -0.77777778, -0.555555556, -0.33333333, -0.11111111, 0.11111111, 0.33333333, 0.55555556, 0.77777776, 1.]
y = [-1.13956201, -0.57177999, -0.21697033, 0.5425699, 0.49406657, 1.14972239, 1.64228553, 2.1749824, 2.64773614, 2.95684202]

# plot dos dados
# plt.figure(figsize=(10, 5))
# plt.plot(x, y, 'o', label='dados originais')
# plt.legend()
# plt.xlabel('x')
# plt.ylabel('y')
# plt.grid()
# plt.show()

# não função reshape podemos determinar o -1 quando não saber a quantidade de denominador
x, y = np.array(x).reshape(-1, 1), np.array(y).reshape(-1, 1)

# adicionando baias: para estimar o termo base
x = np.hstack((x, np.ones(x.shape)))

# Estimando A e B
# beta = np.linalg.pinv(x).dot(y)
# print(f'A estimado: {beta[0][0]}')
# print(f'B estimado: {beta[1][0]}')

# df = pd.read_csv("https://pycourse.s3.amazonaws.com/temperature.csv")
# print(df)

# Para arquivos Excel com mais de uma ABA
excel_file = pd.ExcelFile("https://pycourse.s3.amazonaws.com/temperature.xlsx")
df2 = pd.read_excel(excel_file, sheet_name='Sheet1')
print(df2)

df3 = pd.read_excel(excel_file, sheet_name='Sheet2')
print(df3)


# Mostrando as primeiras linhas do DataFrame
n = 3
print(df2.head(n))

# mostrando as ultimas linhas do DataFrame
print(df2.tail(n))

# Para verificar os itens que são constituidos as colunas
print(df2.dtypes)

#Estatisticas basicas dos dados numericos delicinha!
print(df2.describe())

# Panorama geral do DataFrame
print(df2.info())

# Verificar o nome das colunas
print(df2.columns)

# E possivel renomear as colunas!
df2.columns = ['Col1', 'Col2', 'Col3']
print(df2.columns)

# Retornar apenas uma coluna especifica
# para retornar apenas uma coluna print(df['nome da coluna'] mais de uma coluna tem que ser [['nome das col']]
print(df2[['Col1', 'Col2', 'Col3']])

# Indexação usando o número da coluna
print(df2.iloc[:, 0])

# Indexação usando o nome da coluna
# para pegar mais de uma coluna usa o seguinte metodo df2.loc[:, ['Col1', 'col2']]
print(df2.loc[:, 'Col1'])

# para acessa de uma determinada coluna para frente
print(df2.loc[:, 'Col2':])

# força o parametro para coluna
# df2['Col1'] = pd.to_datetime(df2['Col1'])

# seta a indexação preferencial
print(df2)
df2 = df2.set_index('Col1')
print(df2)

# indexação booleana
print(df2[df2['Col2'] >= 25])

# uma vez convertito a coluna data em index para fazer busca nela usa o seguinte parametro
print(df2[df2.index <= '2020-03-01'])

# dá para fazer busca usando a condição de uma coluna e retornado o valor de outra
print(df2.loc[df2.index <= '2020-03-01', ['Col2']])

# dá para pegar apenas a ultima coluna usando o iloc
print(df2.iloc[df2.index <= '2020-03-01', [-1]])

# para ordenar colunas usamos o metodo sort
# para ordenar um unica coluna df2.sort_values(by='Col2')
# passando o ascending=False ele classificará do maior para o menor!
print(df2.sort_values(by=['Col3', 'Col2'], ascending=False))

# para ordenar pelo index
print(df2.sort_index())
print(df2.sort_index(ascending=False))

# para plotar dados com o panda
print(df2.plot(style='-o', figsize=(10, 5), grid=True))  # Mostra uma linha com uma bola
# print(df2.plot(style='--', figsize=(10, 5), grid=True)) para mostar a linha tracejada
# print(df2.plot(style='-.', figsize=(10, 5), grid=True)) Mostra uma linha

# Para aumenta a espessura da linha
print(df2.plot(style='-o', figsize=(10, 5), linewidth=2.5, grid=True))

# Pode-se adicionar cor, inclusive hex
print(df2.plot(style='-o', figsize=(10, 5), color='#822fb5', linewidth='2.5', grid=True))

# Plot de barras
print(df2['Col3'].value_counts())
teste = df2['Col3'].value_counts().plot.bar(figsize=(10, 5), rot=0)

# Grafico de setores = Pizza
print(df2['Col3'].value_counts().plot.pie(autopct='%1.1f%%', shadow=True, figsize=(10, 7)))


# Agrupar colunas
df2.groupby(by='Col3')
print(df2.groupby(by='Col3').mean())  # depois de agrupar tenho que passar uma função no caso parametro mean
print(df2.groupby(by='Col3').sum())  # ou aqui o parametro sum

# para ignorar uma linha ou coluna usar o metodo drop
df2.drop('Col3', axis=1)

# usando o metodo implace=True faremos uma operação que sobrecreverá o obejeto

