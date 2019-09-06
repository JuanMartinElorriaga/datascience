#CONSOLIDADOR DE ARCHIVOS EXCEL. Total de filas y columnas --- > estáticas
#Colocar este archivo dentro de 

import pandas as pd
from glob import glob
from os import getcwd

cwd = getcwd()
excel_names = glob('H:\\Digital\\HUB\\Fronts\\Media_Planes\\2019\\Junio\\*.xls*') #Busca archivos Excel en la ruta especificada
 
excels = [file for file in directorio if file.endswith(".xlsm") or file.endswith(".xlsx")]

df = pd.DataFrame()
contador = 0

for e in excel_names:
	x = pd.read_excel(e, sheet_name='MEDIA PLAN')
	#maximo = 10 + (x['Unnamed: 1'].count() - 6) + (x['Unnamed: 1'].isnull().sum() - 4) #HAY UN ERROR EN LA CUENTA DE LOS NULL!!!!!
	#print(maximo)
	#print(x['Unnamed: 1'].isnull().sum())
	#print(x['Unnamed: 1'].count())
	x = x.loc[10:60,'Unnamed: 1':'Unnamed: 56']
	df = df.append(x)
	contador += 1
	print(f"Copia de MP {contador} finalizada!")

#print(df)
#From DF to Excel:
writer = pd.ExcelWriter('C:\\Users\\Juan.Elorriaga\\Desktop\\vieja pc\\Proyectos Py\\Bases_consolidadas\\EXCEL_UNIFICADO_JUNIO.xlsx')
df.to_excel(writer)
writer.save()
