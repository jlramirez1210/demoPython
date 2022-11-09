import pandas as pd

titanic = pd.read_csv('./Archives/titanic/titanic.csv')
#Filtrar los sobrevivientes que sean hombres,que hayan estado en 3ra clase y que sean mayores de  20 años
titanic.query('Survived == 1 and Sex == "male" and Pclass == 3 and Age>20', inplace = True)
print(titanic)