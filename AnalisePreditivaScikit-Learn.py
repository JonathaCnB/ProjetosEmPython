import numpy as np
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
excel_file = pd.ExcelFile("https://pycourse.s3.amazonaws.com/temperature.xlsx")
df = pd.read_excel(excel_file, sheet_name='Sheet1')

x, y = df[['temperatura']].values, df[['classification']].values
print(f'X:\n{x}')
print(f'Y:\n{y}')

# Transforma o coluna que antes eram o status da temperatura em valores
# numerico para que sejam comparadas
# Pega um array e transforma em seleção numerica
le = LabelEncoder()
y = le.fit_transform(y.ravel())
print(f'Y:\n{y}')

# classificador
clf = LogisticRegression()
clf.fit(x, y)

# Gerando 100 valores de temperatura, linearmente espaçados entre 0 e 45
# predição em novos valores de temperatura
# Transformando em vetor coluna reshape(-1, 1)
x_test = np.linspace(start=0., stop=45., num=100).reshape(-1, 1)

# # predição desses valores
y_pred = clf.predict(x_test)

# conversão de y_pred para os valores originais
y_pred = le.inverse_transform(y_pred)

# OutPut
output = {'new_temp': x_test.ravel(), 'new_class': y_pred.ravel()}
output = pd.DataFrame(output)

# Estatisticas
output.info()
print(output.describe())

# contagem de valores gerados
output['new_class'].value_counts().plot.bar(figsize=(10, 5), rot=0, title="# de novos valores")

# distribuição do output produzido conseguimos inferir a classificação novas temperaturas

output.boxplot(by='new_class', figsize=(10, 5))

# sistema automatico para verificação da temperatura


def classify_temp():

    '''Classifica o input do usuário'''

    ask = True
    while ask:
        # input de temperatura
        temp = input('Insira a temperatura: ')

        # transforma para numpy array
        temp = np.array(float(temp)).reshape(-1, 1)

        # Realiza Classificação
        class_temp = clf.predict(temp)

        # Transformação inversa para retornar a string original
        class_temp = le.inverse_transform(class_temp)

        # classificação
        print(f'A classificação da temperatura {temp.ravel()[0]} é: {class_temp[0]}')

        # pergunta
        ask = input('Nova classificação (y/n): ') == 'y'

# rodando o programa

classify_temp()



