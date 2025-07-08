import pandas as pd
from sklearn.linear_model import LinearRegression
import pickle 

base_treino = pd.read_csv("data/train.csv")

eliminar = base_treino.columns[base_treino.isnull().sum()/base_treino.shape[0] > 0.1] 
base_treino = base_treino.drop(eliminar, axis=1)

colunas_texto_treino = base_treino.columns[base_treino.dtypes == 'object']
base_treino = base_treino.drop(colunas_texto_treino, axis=1)

base_treino = base_treino.fillna(-1)

X_treino = base_treino.drop('SalePrice', axis=1)
Y_treino = base_treino['SalePrice']

regressao_linear = LinearRegression().fit(X_treino, Y_treino)

print("Features que o modelo aprendeu:")
features = regressao_linear.feature_names_in_
print(list(features))


nome_arquivo_modelo = 'modelo.pkl'

with open(nome_arquivo_modelo, 'wb') as file:
    pickle.dump(regressao_linear, file)

def Previsao(teste):
    return regressao_linear.predict(teste)
