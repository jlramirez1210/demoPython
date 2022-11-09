import pandas as pd
import xml.etree.ElementTree as et
import glob

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

def transform(data):
    data.query('fuel != "Diesel"', inplace=True)
    data['price'] = round(data['price'], 2)
    return data

extracted_data = extraer()
transformed_data = transform(extracted_data)
print(transformed_data)