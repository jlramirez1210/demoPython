import pandas as pd

titanic = pd.read_csv('./Archives/titanic/titanic.csv')
#Filtrando datos muestra data solamente con Cabin = NaN
bool_series = pd.isnull(titanic['Cabin'])
print(titanic[bool_series])