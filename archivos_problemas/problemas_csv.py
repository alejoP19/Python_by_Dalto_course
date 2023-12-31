#cambiar el tipo de dato de una columna
import pandas as pd
df = pd.read_csv("archivos_problemas\\datos.csv")
# print(df)

#convertir a string los datos de una columna
df['edad'] = df['edad'].astype(str)

#mostrar el tipo de dato del primer elemento de la columna edad
# print(type(df['edad'][0]))

#remplazando los datos "dalto" por "Mario"
df['nombre'].replace("lucas","Alejandro",inplace=True)
print(df['nombre'])

#eliminando las filas con datos faltantes
# df = df.dropna()

#eliminando las filas repetidas
# df = df.drop_duplicates()

#creando un CSV con el dataframe resultante (limpio)
df.to_csv("archivos_problemas\\datos_limpios.csv")




