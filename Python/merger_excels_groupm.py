#CONSOLIDADOR DE ARCHIVOS EXCEL. Total de filas y columnas --- > estáticas
#Colocar este archivo dentro de la carpeta contenedora de los archivos a consolidar (*.xls*)

import pandas as pd
from glob import glob
from os import getcwd
#######################################################################################################

#cwd = getcwd()
excel_names = glob('H:\\Digital\\HUB\\Fronts\\Media_Planes\\2019\\Junio\\*.xls*') #Conjunto de archivos Excel en la ruta especificada
df = pd.DataFrame()
contador = 0

for e in excel_names:
	x = pd.read_excel(e, sheet_name = 'MEDIA PLAN')
	x = x.loc[10:60,'Unnamed: 1':'Unnamed: 56']
	df = df.append(x)
	contador += 1
	print(f"Copia de MP {contador} finalizada!")

print(f"Cantidad total de MP: {contador}")

#From df to Excel:
writer = pd.ExcelWriter('C:\\Users\\Juan.Elorriaga\\Desktop\\vieja pc\\Proyectos Py\\Bases_consolidadas\\EXCEL_UNIFICADO.xlsx')
df.to_excel(writer)
writer.save()
