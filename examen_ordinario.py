import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#1. CARGA Y SEGMENTACION DE LA INFORMACIÓN
#carga de datasets
#insurance
df1= pd.read_csv("C:/Users/Valeria/Desktop/insurance.csv")
df2=pd.read_csv("C:/Users/Valeria/Desktop/heart_disease_uci.csv")
df_valeria= pd.concat([df1,df2], axis=1)

#Limpieza de valores nulos y duplicados

df_valeria.dropna(inplace=True)
df_valeria.drop_duplicates(inplace=True)
print(df_valeria)


#2. ANALISIS EXPLORATORIO DE DATOS
def modelo_camacho(df_valeria1, df_valeria2):
    pass
