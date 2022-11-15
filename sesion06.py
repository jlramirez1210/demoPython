import pandas as pd
import xml.etree.ElementTree as et
import glob
from datetime import datetime
import sqlalchemy
#import mysql.connector

def extraer_de_csv(archivo_procesar):
    df = pd.read_csv(archivo_procesar)
    return df

def extraer_de_json(archivo_procesar):
    df = pd.read_json(archivo_procesar, lines = True)
    return df

def extraer_de_xml(archivo_procesar):
    xtree = et.parse(archivo_procesar)
    xroot = xtree.getroot()
    car_model_list = []
    year_of_manufacture_list = []
    price_list = []
    fuel_list = []
    for persona in xroot:
        car_model_list.append(persona.find('car_model').text)
        year_of_manufacture_list.append(persona.find('year_of_manufacture').text)
        price_list.append(float(persona.find('price').text))
        fuel_list.append(persona.find('fuel').text)
    df = pd.DataFrame({'car_model': car_model_list, 'year_of_manufacture': year_of_manufacture_list, 'price': price_list, 'fuel':fuel_list })
    return df

def extraer():
    df_list = []
    for a_csv in glob.glob('./Archives/used_car_prices/*.csv'):
        print(a_csv)
        df_list.append(extraer_de_csv(a_csv))

    for a_json in glob.glob('./Archives/used_car_prices/*.json'):
        print(a_json)
        df_list.append(extraer_de_json(a_json))

    for a_xml in glob.glob('./Archives/used_car_prices/*.xml'):
        print(a_xml)
        df_list.append(extraer_de_xml(a_xml))

    final_df = pd.concat(df_list)
    return final_df

def transform1(data):
    #data.year_of_manufacture = data.year_of_manufacture.astype(int)
    #data.sort_values(by=['year_of_manufacture'])
    data.query('fuel != "Diesel"', inplace=True) #excluir los que usan diesel
    data['price'] = round(data['price'], 2) #redondear el precio a dos
    return data

def transform2(data):
    return data.groupby(['car_model'])['price'].mean() #agruoa por car_model y promedia el campo price

def load1(df):
    username = 'root'
    hostname = 'localhost'
    database = 'used_car_prices'
    port = '3306'
    password = 'root'
    con = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                                   format(username, password,
                                          hostname, database))
    df.to_sql(con=con, name='precio_autos', if_exists='append')

def load2(df):
    username = 'root'
    hostname = 'localhost'
    database = 'used_car_prices'
    port = '3306'
    password = 'root'
    con = sqlalchemy.create_engine('mysql+mysqlconnector://{0}:{1}@{2}/{3}'.
                                   format(username, password,
                                          hostname, database))
    df.to_sql(con=con, name='precio_modelo', if_exists='append')

now = datetime.now()
print('Proceso Comienza',now)
extracted_data = extraer()
transformed_data1 = transform1(extracted_data)
transformed_data2 = transform2(transformed_data1)
load1(transformed_data1) #carga a la tabla precio_autos
load2(transformed_data2) #carga a la tabla precio_modelo
now = datetime.now()
print('Proceso Finaliza',now)