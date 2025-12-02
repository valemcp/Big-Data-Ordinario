import pandas as pd
import numpy as np

#carga de datasets
#insurance
df_valeria1 = pd.read_csv("C:/Users/Valeria/Desktop/insurance.csv")
print(df_valeria1.head())
#heart disease
df_valeria2=pd.read_csv("C:/Users/Valeria/Desktop/heart_disease_uci.csv")
print(df_valeria2.head())


#Limpieza de valores nulos y duplicados

#dataser insurance
df_valeria1.dropna(inplace=True)
df_valeria2.drop_duplicates(inplace=True)
print(df_valeria1)

#dataset heart disease
df_valeria2.dropna(inplace=True)
df_valeria2.drop_duplicates(inplace=True)
print(df_valeria2)

