import pandas as pd
import xml.etree.ElementTree as et
import glob

def extraer_de_csv(archivo_procesar):
    df = pd.read_csv(archivo_procesar)
    df['origen'] = archivo_procesar
    df['tipo'] = 'csv'
    return df

def extraer_de_json(archivo_procesar):
    df = pd.read_json(archivo_procesar, lines = True)
    df['origen'] = archivo_procesar
    df['tipo'] = 'json'
    return df

def extraer_de_xml(archivo_procesar):
    xtree = et.parse(archivo_procesar)
    xroot = xtree.getroot()
    nombre_list = []
    ventas1_list = []
    ventas_list = []
    for persona in xroot:
        nombre_list.append(persona.find('nombre').text)
        ventas1_list.append(float(persona.find('ventas1').text))
        ventas_list.append(float(persona.find('ventas').text))

    df = pd.DataFrame({'nombre': nombre_list, 'ventas1': ventas1_list, 'ventas': ventas_list, 'origen':archivo_procesar, 'tipo': 'xml' })
    return df

def extraer():
    df_list = []
    for a_csv in glob.glob('./Archives/ventas/*.csv'):
        print(a_csv)
        df_list.append(extraer_de_csv(a_csv))

    for a_json in glob.glob('./Archives/ventas/*.json'):
        print(a_json)
        df_list.append(extraer_de_json(a_json))

    for a_xml in glob.glob('./Archives/ventas/*.xml'):
        print(a_xml)
        df_list.append(extraer_de_xml(a_xml))

    final_df = pd.concat(df_list)
    return final_df

print(extraer())