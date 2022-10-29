import pandas as pd

titanic = pd.read_csv('./Archives/titanic.csv', usecols = ['PassengerId', 'Survived', 'Pclass', 'Sex', 'Age'])

def menor(x):
    if x < 18:
        menor = 'SI'
    else:
        menor = "NO"
    return menor

#Crear una nueva columna que indique si eran menor de edad (usar: si y no)
titanic['menorEdad'] = titanic['Age'].transform(menor)
print(titanic)