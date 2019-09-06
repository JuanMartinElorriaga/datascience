#import os
import pandas as pd
#import numpy as np
#import pandasql as psql
RRHH = pd.read_csv(r"C:/Users/Juan.Elorriaga/Desktop/csv/statusRRHH.csv", encoding="cp1252")
RRHH = pd.DataFrame(RRHH)

# =============================================================================
# # RRHH["Area"] = RRHH["Area"].astype("category")
# # RRHH["Area"].cat.set_categories(["Implementacion","Optimizacion","Manager","Pasante"],inplace=True)
# # RRHH.dtypes
# # print(RRHH['Tiempo_Trabajo_en_empresa_(MESES)'])
# # list(RRHH)
# =============================================================================

#TABLAS DE FRECUENCIAS POR EQUIPO ... linea 1: Frecuencias; linea 2: COLUMNA %; linea 3: append Total; linea 4: Cambiar nombre columnas
RRHH_f_area = pd.DataFrame(RRHH['Area'].value_counts())
RRHH_f_area['% respecto al total'] = ((RRHH_f_area.Area / RRHH_f_area.Area.sum())*100)
RRHH_f_area = RRHH_f_area.append(RRHH_f_area.sum().rename('Total')).round(1)
RRHH_f_area = RRHH_f_area.rename(index=str, columns={"Area": "Frecuencia de Area"})

RRHH_f_categoria = pd.DataFrame(RRHH['Categorizacion'].value_counts())
RRHH_f_categoria['% respecto al total'] = ((RRHH_f_categoria.Categorizacion / RRHH_f_categoria.Categorizacion.sum())*100)
RRHH_f_categoria = RRHH_f_categoria.append(RRHH_f_categoria.sum().rename('Total')).round(1)
RRHH_f_categoria = RRHH_f_categoria.rename(index=str, columns={"Categorizacion": "Frecuencia de Categorizacion"})

RRHH_f_intro_extro = pd.DataFrame(RRHH['intro_extro'].value_counts())
RRHH_f_intro_extro['% respecto al total'] = ((RRHH_f_intro_extro.intro_extro / RRHH_f_intro_extro.intro_extro.sum())*100)
RRHH_f_intro_extro = RRHH_f_intro_extro.append(RRHH_f_intro_extro.sum().rename('Total')).round(1)
RRHH_f_intro_extro = RRHH_f_intro_extro.rename(index=str, columns={"intro_extro": "Frecuencia de Introversión - Extroversión"})

RRHH_f_energia = pd.DataFrame(RRHH['Energia'].value_counts())
RRHH_f_energia['% respecto al total'] = ((RRHH_f_energia.Energia / RRHH_f_energia.Energia.sum())*100)
RRHH_f_energia = RRHH_f_energia.append(RRHH_f_energia.sum().rename('Total')).round(1)
RRHH_f_energia = RRHH_f_energia.rename(index=str, columns={"Energia": "Frecuencia de Tipo de Energia"})

RRHH_f_tacticas = pd.DataFrame(RRHH['Tacticas'].value_counts())
RRHH_f_tacticas['% respecto al total'] = ((RRHH_f_tacticas.Tacticas / RRHH_f_tacticas.Tacticas.sum())*100)
RRHH_f_tacticas = RRHH_f_tacticas.append(RRHH_f_tacticas.sum().rename('Total')).round(1)
RRHH_f_tacticas = RRHH_f_tacticas.rename(index=str, columns={"Tacticas": "Frecuencia de Tipo de Tacticas"})

RRHH_f_naturaleza = pd.DataFrame(RRHH['Naturaleza'].value_counts())
RRHH_f_naturaleza['% respecto al total'] = ((RRHH_f_naturaleza.Naturaleza / RRHH_f_naturaleza.Naturaleza.sum())*100)
RRHH_f_naturaleza = RRHH_f_naturaleza.append(RRHH_f_naturaleza.sum().rename('Total')).round(1)
RRHH_f_naturaleza = RRHH_f_naturaleza.rename(index=str, columns={"Naturaleza": "Frecuencia de Tipo de Naturaleza"})

RRHH_f_Rubro_Profesional = pd.DataFrame(RRHH['Rubro_Profesional'].value_counts())
RRHH_f_Rubro_Profesional['% respecto al total'] = ((RRHH_f_Rubro_Profesional.Rubro_Profesional / RRHH_f_Rubro_Profesional.Rubro_Profesional.sum())*100)
RRHH_f_Rubro_Profesional = RRHH_f_Rubro_Profesional.append(RRHH_f_Rubro_Profesional.sum().rename('Total')).round(1)
RRHH_f_Rubro_Profesional = RRHH_f_Rubro_Profesional.rename(index=str, columns={"Rubro_Profesional": "Frecuencia de Rubro Profesional"})


#TABLAS PIVOT por categorizacion
RRHH_pt_CI_x_Categ = pd.DataFrame(RRHH.pivot_table(index='Categorizacion', values='CI_TEST')).round(1).sort_values(by=['CI_TEST'], ascending = False)
RRHH_pt_CI_x_Categ = RRHH_pt_CI_x_Categ.append(RRHH_pt_CI_x_Categ.mean().rename('Media Total')).round(1)
RRHH_pt_CI_x_Categ = RRHH_pt_CI_x_Categ.rename(index=str, columns={"CI_TEST": "Media de test CI por Categorización"})

RRHH_pt_ACIERTOS_x_Categ = pd.DataFrame(RRHH.pivot_table(index='Categorizacion', values='ACIERTOS')).round(1).sort_values(by=['ACIERTOS'], ascending = False)
RRHH_pt_ACIERTOS_x_Categ = RRHH_pt_ACIERTOS_x_Categ.append(RRHH_pt_ACIERTOS_x_Categ.mean().rename('Media Total')).round(1)
RRHH_pt_ACIERTOS_x_Categ = RRHH_pt_ACIERTOS_x_Categ.rename(index=str, columns={"ACIERTOS": "Media de aciertos por Categorización"})

RRHH_pt_GLOBAL_x_Categ = pd.DataFrame(RRHH.pivot_table(index='Categorizacion', values='%_GLOBAL')).round(1).sort_values(by=['%_GLOBAL'], ascending = False)
RRHH_pt_GLOBAL_x_Categ = RRHH_pt_GLOBAL_x_Categ.append(RRHH_pt_GLOBAL_x_Categ.mean().rename('Media Total')).round(1)
RRHH_pt_GLOBAL_x_Categ = RRHH_pt_GLOBAL_x_Categ.rename(index=str, columns={"%_GLOBAL": "Media de % global por Categorización"})

RRHH_pt_PREGS_x_Categ = pd.DataFrame(RRHH.pivot_table(index='Categorizacion', values='TOTAL_PREGUNTAS')).round(1).sort_values(by=['TOTAL_PREGUNTAS'], ascending = False)
RRHH_pt_PREGS_x_Categ = RRHH_pt_PREGS_x_Categ.append(RRHH_pt_PREGS_x_Categ.mean().rename('Media Total')).round(1)
RRHH_pt_PREGS_x_Categ = RRHH_pt_PREGS_x_Categ.rename(index=str, columns={"TOTAL_PREGUNTAS": "Media de Total de Preguntas por Categorización"})

#SUMMARY
RRHH_describe = RRHH.describe().round(2)
#RRHH_describe = RRHH_describe.round(2)
#SUMMARY POR GRUPO
RRHH_Fronts = RRHH[RRHH.Area == 'Front'].describe().round(2)
RRHH_Implementadores = RRHH[RRHH.Area == 'Implementacion'].describe().round(2)
RRHH_Optimizadores = RRHH[RRHH.Area == 'Optimizacion'].describe().round(2)
RRHH_MANAGERS = RRHH[RRHH.Area == 'QA'].describe().round(2)
RRHH_Pasantes = RRHH[RRHH.Area == 'Pasante'].describe().round(2)
RRHH_Managers = RRHH[RRHH.Area == 'Manager'].describe().round(2)



#TABLAS CONDICIONALES A NIVEL AGREGADO
#Tabla de meses en la empresa 
rrhh_ptc_meses1 = RRHH['Tiempo_Trabajo_en_empresa_(MESES)']<=3
rrhh_ptc_meses1 = pd.DataFrame(rrhh_ptc_meses1.value_counts())
rrhh_ptc_meses1 = rrhh_ptc_meses1.drop(False)
rrhh_ptc_meses1.index = ["3 meses o menos"]
rrhh_ptc_meses2 = RRHH['Tiempo_Trabajo_en_empresa_(MESES)']<=6
rrhh_ptc_meses2 = pd.DataFrame(rrhh_ptc_meses2.value_counts())
rrhh_ptc_meses2 = rrhh_ptc_meses2.drop(False)
rrhh_ptc_meses2.index = ["6 meses o menos"]
rrhh_ptc_meses3 = RRHH['Tiempo_Trabajo_en_empresa_(MESES)']>=12
rrhh_ptc_meses3 = pd.DataFrame(rrhh_ptc_meses3.value_counts())
rrhh_ptc_meses3 = rrhh_ptc_meses3.drop(False)
rrhh_ptc_meses3.index = ["12 meses o más"]
rrhh_ptc_meses = rrhh_ptc_meses1.append([rrhh_ptc_meses2, rrhh_ptc_meses3])
rrhh_ptc_meses['% respecto al total'] = ((rrhh_ptc_meses['Tiempo_Trabajo_en_empresa_(MESES)'] / rrhh_ptc_meses['Tiempo_Trabajo_en_empresa_(MESES)'].sum())*100)
rrhh_ptc_meses = rrhh_ptc_meses.rename(index=str, columns={"Tiempo_Trabajo_en_empresa_(MESES)": "Tiempo de trabajo en la empresa (MESES)"}).round(1)
del(rrhh_ptc_meses1,rrhh_ptc_meses2,rrhh_ptc_meses3)

#Tabla de años en rubro
rrhh_ptc_rubro1 = RRHH['Años_laborales_rubro_(MARKETING DIGITAL)']<=3
rrhh_ptc_rubro1 = pd.DataFrame(rrhh_ptc_rubro1.value_counts())
rrhh_ptc_rubro1 = rrhh_ptc_rubro1.drop(False)
rrhh_ptc_rubro1.index = ["3 meses o menos"]
rrhh_ptc_rubro2 = RRHH['Años_laborales_rubro_(MARKETING DIGITAL)']<=6
rrhh_ptc_rubro2 = pd.DataFrame(rrhh_ptc_rubro2.value_counts())
rrhh_ptc_rubro2 = rrhh_ptc_rubro2.drop(False)
rrhh_ptc_rubro2.index = ["6 meses o menos"]
rrhh_ptc_rubro3 = RRHH['Años_laborales_rubro_(MARKETING DIGITAL)']>6
rrhh_ptc_rubro3 = pd.DataFrame(rrhh_ptc_rubro3.value_counts())
rrhh_ptc_rubro3 = rrhh_ptc_rubro3.drop(False)
rrhh_ptc_rubro3.index = ["Más de 6 meses"]
rrhh_ptc_rubro = rrhh_ptc_rubro1.append([rrhh_ptc_rubro2, rrhh_ptc_rubro3])
rrhh_ptc_rubro['% respecto al total'] = ((rrhh_ptc_rubro['Años_laborales_rubro_(MARKETING DIGITAL)'] / rrhh_ptc_rubro['Años_laborales_rubro_(MARKETING DIGITAL)'].sum())*100)
rrhh_ptc_rubro = rrhh_ptc_rubro.rename(index=str, columns={'Años_laborales_rubro_(MARKETING DIGITAL)': 'Años laborales en el rubro (MARKETING DIGITAL)'}).round(1)
del(rrhh_ptc_rubro1,rrhh_ptc_rubro2,rrhh_ptc_rubro3)

#Tabla de edad
rrhh_ptc_edad1 = RRHH['Edad']<=21
rrhh_ptc_edad1 = pd.DataFrame(rrhh_ptc_edad1.value_counts())
rrhh_ptc_edad1 = rrhh_ptc_edad1.drop(False)
rrhh_ptc_edad1.index = ["21 años o menos"]
rrhh_ptc_edad2 = RRHH['Edad']<=25
rrhh_ptc_edad2 = pd.DataFrame(rrhh_ptc_edad2.value_counts())
rrhh_ptc_edad2 = rrhh_ptc_edad2.drop(False)
rrhh_ptc_edad2.index = ["25 años o menos"]
rrhh_ptc_edad3 = RRHH['Edad']>30
rrhh_ptc_edad3 = pd.DataFrame(rrhh_ptc_edad3.value_counts())
rrhh_ptc_edad3 = rrhh_ptc_edad3.drop(False)
rrhh_ptc_edad3.index = ["30 años o más"]
rrhh_ptc_edad = rrhh_ptc_edad1.append([rrhh_ptc_edad2, rrhh_ptc_edad3])
rrhh_ptc_edad['% respecto al total'] = ((rrhh_ptc_edad['Edad'] / rrhh_ptc_edad['Edad'].sum())*100).round(1)
del(rrhh_ptc_edad1,rrhh_ptc_edad2,rrhh_ptc_edad3)

#Tabla de experiencia total
rrhh_ptc_expTot1 = RRHH['Experiencia_Laboral_Total_(AÑOS)']<=3
rrhh_ptc_expTot1 = pd.DataFrame(rrhh_ptc_expTot1.value_counts())
rrhh_ptc_expTot1 = rrhh_ptc_expTot1.drop(False)
rrhh_ptc_expTot1.index = ["3 años o menos"]
rrhh_ptc_expTot2 = RRHH['Experiencia_Laboral_Total_(AÑOS)']<=6
rrhh_ptc_expTot2 = pd.DataFrame(rrhh_ptc_expTot2.value_counts())
rrhh_ptc_expTot2 = rrhh_ptc_expTot2.drop(False)
rrhh_ptc_expTot2.index = ["6 años o menos"]
rrhh_ptc_expTot3 = RRHH['Experiencia_Laboral_Total_(AÑOS)']>6
rrhh_ptc_expTot3 = pd.DataFrame(rrhh_ptc_expTot3.value_counts())
rrhh_ptc_expTot3 = rrhh_ptc_expTot3.drop(False)
rrhh_ptc_expTot3.index = ["Más de 6 meses"]

rrhh_ptc_expTot = rrhh_ptc_expTot1.append([rrhh_ptc_expTot2, rrhh_ptc_expTot3])
rrhh_ptc_expTot['% respecto al total'] = ((rrhh_ptc_expTot['Experiencia_Laboral_Total_(AÑOS)'] / rrhh_ptc_expTot['Experiencia_Laboral_Total_(AÑOS)'].sum())*100)
rrhh_ptc_expTot = rrhh_ptc_expTot.rename(index=str, columns={'Experiencia_Laboral_Total_(AÑOS)': 'Experiencia laboral total (AÑOS)'}).round(1)
del(rrhh_ptc_expTot1,rrhh_ptc_expTot2,rrhh_ptc_expTot3)



#TABLAS CONDICIONALES POR EQUIPO
rrhh_fronts = RRHH[RRHH.Area == 'Front']
rrhh_optimizadores = RRHH[RRHH.Area == 'Optimizacion']
rrhh_implementadores = RRHH[RRHH.Area == 'Implementacion']
rrhh_pasantes = RRHH[RRHH.Area == 'Pasante']
rrhh_QAs = RRHH[RRHH.Area == 'QA']
RRHH_managers = RRHH[RRHH.Area == 'Manager']
#Tabla de meses en la empresa 

#FRONTS
rrhh_ptc_meses1 = rrhh_fronts['Tiempo_Trabajo_en_empresa_(MESES)']<=3
rrhh_ptc_meses1 = pd.DataFrame(rrhh_ptc_meses1.value_counts())
rrhh_ptc_meses1 = rrhh_ptc_meses1.drop(False)
rrhh_ptc_meses1.index = ["3 meses o menos"]
rrhh_ptc_meses2 = rrhh_fronts['Tiempo_Trabajo_en_empresa_(MESES)']<=6
rrhh_ptc_meses2 = pd.DataFrame(rrhh_ptc_meses2.value_counts())
rrhh_ptc_meses2 = rrhh_ptc_meses2.drop(False)
rrhh_ptc_meses2.index = ["6 meses o menos"]
rrhh_ptc_meses3 = rrhh_fronts['Tiempo_Trabajo_en_empresa_(MESES)']>=12
rrhh_ptc_meses3 = pd.DataFrame(rrhh_ptc_meses3.value_counts())
rrhh_ptc_meses3 = rrhh_ptc_meses3.drop(False)
rrhh_ptc_meses3.index = ["12 meses o más"]
rrhh_ptc_meses_FRONTS = rrhh_ptc_meses1.append([rrhh_ptc_meses2, rrhh_ptc_meses3])
rrhh_ptc_meses_FRONTS['% respecto al total'] = ((rrhh_ptc_meses_FRONTS['Tiempo_Trabajo_en_empresa_(MESES)'] / rrhh_ptc_meses_FRONTS['Tiempo_Trabajo_en_empresa_(MESES)'].sum())*100)
rrhh_ptc_meses_FRONTS = rrhh_ptc_meses_FRONTS.rename(index=str, columns={"Tiempo_Trabajo_en_empresa_(MESES)": "Tiempo de trabajo en la empresa (MESES) - FRONT"}).round(1)
del(rrhh_ptc_meses1,rrhh_ptc_meses2,rrhh_ptc_meses3)

#Tabla de años en rubro
rrhh_ptc_rubro1 = rrhh_fronts['Años_laborales_rubro_(MARKETING DIGITAL)']<=3
rrhh_ptc_rubro1 = pd.DataFrame(rrhh_ptc_rubro1.value_counts())
rrhh_ptc_rubro1 = rrhh_ptc_rubro1.drop(False)
rrhh_ptc_rubro1.index = ["3 meses o menos"]
rrhh_ptc_rubro2 = rrhh_fronts['Años_laborales_rubro_(MARKETING DIGITAL)']<=6
rrhh_ptc_rubro2 = pd.DataFrame(rrhh_ptc_rubro2.value_counts())
rrhh_ptc_rubro2 = rrhh_ptc_rubro2.drop(False)
rrhh_ptc_rubro2.index = ["6 meses o menos"]
rrhh_ptc_rubro3 = rrhh_fronts['Años_laborales_rubro_(MARKETING DIGITAL)']>6
rrhh_ptc_rubro3 = pd.DataFrame(rrhh_ptc_rubro3.value_counts())
rrhh_ptc_rubro3 = rrhh_ptc_rubro3.drop(False)
rrhh_ptc_rubro3.index = ["Más de 6 meses"]
rrhh_ptc_rubro_FRONTS = rrhh_ptc_rubro1.append([rrhh_ptc_rubro2, rrhh_ptc_rubro3])
rrhh_ptc_rubro_FRONTS['% respecto al total'] = ((rrhh_ptc_rubro_FRONTS['Años_laborales_rubro_(MARKETING DIGITAL)'] / rrhh_ptc_rubro_FRONTS['Años_laborales_rubro_(MARKETING DIGITAL)'].sum())*100)
rrhh_ptc_rubro_FRONTS = rrhh_ptc_rubro_FRONTS.rename(index=str, columns={'Años_laborales_rubro_(MARKETING DIGITAL)': 'Años laborales en el rubro (MARKETING DIGITAL)'}).round(1)
del(rrhh_ptc_rubro1,rrhh_ptc_rubro2,rrhh_ptc_rubro3)

#Tabla de edad
rrhh_ptc_edad1 = rrhh_fronts['Edad']<=21
rrhh_ptc_edad1 = pd.DataFrame(rrhh_ptc_edad1.value_counts())
rrhh_ptc_edad1 = rrhh_ptc_edad1.drop(False)
rrhh_ptc_edad1.index = ["21 años o menos"]
rrhh_ptc_edad2 = rrhh_fronts['Edad']<=25
rrhh_ptc_edad2 = pd.DataFrame(rrhh_ptc_edad2.value_counts())
rrhh_ptc_edad2 = rrhh_ptc_edad2.drop(False)
rrhh_ptc_edad2.index = ["25 años o menos"]
rrhh_ptc_edad3 = rrhh_fronts['Edad']>30
rrhh_ptc_edad3 = pd.DataFrame(rrhh_ptc_edad3.value_counts())
rrhh_ptc_edad3 = rrhh_ptc_edad3.drop(False)
rrhh_ptc_edad3.index = ["30 años o más"]
rrhh_ptc_edad_FRONTS = rrhh_ptc_edad1.append([rrhh_ptc_edad2, rrhh_ptc_edad3])
rrhh_ptc_edad_FRONTS['% respecto al total'] = ((rrhh_ptc_edad_FRONTS['Edad'] / rrhh_ptc_edad_FRONTS['Edad'].sum())*100).round(1)
del(rrhh_ptc_edad1,rrhh_ptc_edad2,rrhh_ptc_edad3)

#Tabla de experiencia total
rrhh_ptc_expTot1 = rrhh_fronts['Experiencia_Laboral_Total_(AÑOS)']<=3
rrhh_ptc_expTot1 = pd.DataFrame(rrhh_ptc_expTot1.value_counts())
rrhh_ptc_expTot1 = rrhh_ptc_expTot1.drop(False)
rrhh_ptc_expTot1.index = ["3 años o menos"]
rrhh_ptc_expTot2 = rrhh_fronts['Experiencia_Laboral_Total_(AÑOS)']<=6
rrhh_ptc_expTot2 = pd.DataFrame(rrhh_ptc_expTot2.value_counts())
rrhh_ptc_expTot2 = rrhh_ptc_expTot2.drop(False)
rrhh_ptc_expTot2.index = ["6 años o menos"]
rrhh_ptc_expTot3 = rrhh_fronts['Experiencia_Laboral_Total_(AÑOS)']>6
rrhh_ptc_expTot3 = pd.DataFrame(rrhh_ptc_expTot3.value_counts())
rrhh_ptc_expTot3 = rrhh_ptc_expTot3.drop(False)
rrhh_ptc_expTot3.index = ["Más de 6 meses"]

rrhh_ptc_expTot_FRONTS = rrhh_ptc_expTot1.append([rrhh_ptc_expTot2, rrhh_ptc_expTot3])
rrhh_ptc_expTot_FRONTS['% respecto al total'] = ((rrhh_ptc_expTot_FRONTS['Experiencia_Laboral_Total_(AÑOS)'] / rrhh_ptc_expTot_FRONTS['Experiencia_Laboral_Total_(AÑOS)'].sum())*100)
rrhh_ptc_expTot_FRONTS = rrhh_ptc_expTot.rename(index=str, columns={'Experiencia_Laboral_Total_(AÑOS)': 'Experiencia laboral total (AÑOS)'}).round(1)
del(rrhh_ptc_expTot1,rrhh_ptc_expTot2,rrhh_ptc_expTot3)


#OPTIMIZACION
rrhh_ptc_meses1 = rrhh_optimizadores['Tiempo_Trabajo_en_empresa_(MESES)']<=3
rrhh_ptc_meses1 = pd.DataFrame(rrhh_ptc_meses1.value_counts())
rrhh_ptc_meses1 = rrhh_ptc_meses1.drop(False)
rrhh_ptc_meses1.index = ["3 meses o menos"]
rrhh_ptc_meses2 = rrhh_optimizadores['Tiempo_Trabajo_en_empresa_(MESES)']<=6
rrhh_ptc_meses2 = pd.DataFrame(rrhh_ptc_meses2.value_counts())
rrhh_ptc_meses2 = rrhh_ptc_meses2.drop(False)
rrhh_ptc_meses2.index = ["6 meses o menos"]
rrhh_ptc_meses3 = rrhh_optimizadores['Tiempo_Trabajo_en_empresa_(MESES)']>=12
rrhh_ptc_meses3 = pd.DataFrame(rrhh_ptc_meses3.value_counts())
rrhh_ptc_meses3 = rrhh_ptc_meses3.drop(False)
rrhh_ptc_meses3.index = ["12 meses o más"]
rrhh_ptc_meses_OPTIMIZ = rrhh_ptc_meses1.append([rrhh_ptc_meses2, rrhh_ptc_meses3])
rrhh_ptc_meses_OPTIMIZ['% respecto al total'] = ((rrhh_ptc_meses_OPTIMIZ['Tiempo_Trabajo_en_empresa_(MESES)'] / rrhh_ptc_meses_OPTIMIZ['Tiempo_Trabajo_en_empresa_(MESES)'].sum())*100)
rrhh_ptc_meses_OPTIMIZ = rrhh_ptc_meses_OPTIMIZ.rename(index=str, columns={"Tiempo_Trabajo_en_empresa_(MESES)": "Tiempo de trabajo en la empresa (MESES) - FRONT"}).round(1)
del(rrhh_ptc_meses1,rrhh_ptc_meses2,rrhh_ptc_meses3)

#Tabla de años en rubro
rrhh_ptc_rubro1 = rrhh_optimizadores['Años_laborales_rubro_(MARKETING DIGITAL)']<=3
rrhh_ptc_rubro1 = pd.DataFrame(rrhh_ptc_rubro1.value_counts())
rrhh_ptc_rubro1 = rrhh_ptc_rubro1.drop(False)
rrhh_ptc_rubro1.index = ["3 meses o menos"]
rrhh_ptc_rubro2 = rrhh_optimizadores['Años_laborales_rubro_(MARKETING DIGITAL)']<=6
rrhh_ptc_rubro2 = pd.DataFrame(rrhh_ptc_rubro2.value_counts())
rrhh_ptc_rubro2 = rrhh_ptc_rubro2.drop(False)
rrhh_ptc_rubro2.index = ["6 meses o menos"]
rrhh_ptc_rubro3 = rrhh_optimizadores['Años_laborales_rubro_(MARKETING DIGITAL)']>6
rrhh_ptc_rubro3 = pd.DataFrame(rrhh_ptc_rubro3.value_counts())
rrhh_ptc_rubro3 = rrhh_ptc_rubro3.drop(False)
rrhh_ptc_rubro3.index = ["Más de 6 meses"]
rrhh_ptc_rubro_OPTIMIZ = rrhh_ptc_rubro1.append([rrhh_ptc_rubro2, rrhh_ptc_rubro3])
rrhh_ptc_rubro_OPTIMIZ['% respecto al total'] = ((rrhh_ptc_rubro_OPTIMIZ['Años_laborales_rubro_(MARKETING DIGITAL)'] / rrhh_ptc_rubro_OPTIMIZ['Años_laborales_rubro_(MARKETING DIGITAL)'].sum())*100)
rrhh_ptc_rubro_OPTIMIZ = rrhh_ptc_rubro_OPTIMIZ.rename(index=str, columns={'Años_laborales_rubro_(MARKETING DIGITAL)': 'Años laborales en el rubro (MARKETING DIGITAL)'}).round(1)
del(rrhh_ptc_rubro1,rrhh_ptc_rubro2,rrhh_ptc_rubro3)

#Tabla de edad
rrhh_ptc_edad1 = rrhh_optimizadores['Edad']<=21
rrhh_ptc_edad1 = pd.DataFrame(rrhh_ptc_edad1.value_counts())
rrhh_ptc_edad1 = rrhh_ptc_edad1.drop(False)
rrhh_ptc_edad1.index = ["21 años o menos"]
rrhh_ptc_edad2 = rrhh_optimizadores['Edad']<=25
rrhh_ptc_edad2 = pd.DataFrame(rrhh_ptc_edad2.value_counts())
rrhh_ptc_edad2 = rrhh_ptc_edad2.drop(False)
rrhh_ptc_edad2.index = ["25 años o menos"]
rrhh_ptc_edad3 = rrhh_optimizadores['Edad']>30
rrhh_ptc_edad3 = pd.DataFrame(rrhh_ptc_edad3.value_counts())
rrhh_ptc_edad3 = rrhh_ptc_edad3.drop(False)
rrhh_ptc_edad3.index = ["30 años o más"]
rrhh_ptc_edad_OPTIMIZ = rrhh_ptc_edad1.append([rrhh_ptc_edad2, rrhh_ptc_edad3])
rrhh_ptc_edad_OPTIMIZ['% respecto al total'] = ((rrhh_ptc_edad_OPTIMIZ['Edad'] / rrhh_ptc_edad_OPTIMIZ['Edad'].sum())*100).round(1)
del(rrhh_ptc_edad1,rrhh_ptc_edad2,rrhh_ptc_edad3)

#Tabla de experiencia total
rrhh_ptc_expTot1 = rrhh_optimizadores['Experiencia_Laboral_Total_(AÑOS)']<=3
rrhh_ptc_expTot1 = pd.DataFrame(rrhh_ptc_expTot1.value_counts())
rrhh_ptc_expTot1 = rrhh_ptc_expTot1.drop(False)
rrhh_ptc_expTot1.index = ["3 años o menos"]
rrhh_ptc_expTot2 = rrhh_optimizadores['Experiencia_Laboral_Total_(AÑOS)']<=6
rrhh_ptc_expTot2 = pd.DataFrame(rrhh_ptc_expTot2.value_counts())
rrhh_ptc_expTot2 = rrhh_ptc_expTot2.drop(False)
rrhh_ptc_expTot2.index = ["6 años o menos"]
rrhh_ptc_expTot3 = rrhh_optimizadores['Experiencia_Laboral_Total_(AÑOS)']>6
rrhh_ptc_expTot3 = pd.DataFrame(rrhh_ptc_expTot3.value_counts())
rrhh_ptc_expTot3 = rrhh_ptc_expTot3.drop(False)
rrhh_ptc_expTot3.index = ["Más de 6 meses"]

rrhh_ptc_expTot_OPTIMIZ = rrhh_ptc_expTot1.append([rrhh_ptc_expTot2, rrhh_ptc_expTot3])
rrhh_ptc_expTot_OPTIMIZ['% respecto al total'] = ((rrhh_ptc_expTot_OPTIMIZ['Experiencia_Laboral_Total_(AÑOS)'] / rrhh_ptc_expTot_OPTIMIZ['Experiencia_Laboral_Total_(AÑOS)'].sum())*100)
rrhh_ptc_expTot_OPTIMIZ = rrhh_ptc_expTot.rename(index=str, columns={'Experiencia_Laboral_Total_(AÑOS)': 'Experiencia laboral total (AÑOS)'}).round(1)
del(rrhh_ptc_expTot1,rrhh_ptc_expTot2,rrhh_ptc_expTot3)


#IMPEMENTACION
rrhh_ptc_meses1 = rrhh_implementadores['Tiempo_Trabajo_en_empresa_(MESES)']<=3
rrhh_ptc_meses1 = pd.DataFrame(rrhh_ptc_meses1.value_counts())
rrhh_ptc_meses1 = rrhh_ptc_meses1.drop(False)
rrhh_ptc_meses1.index = ["3 meses o menos"]
rrhh_ptc_meses2 = rrhh_implementadores['Tiempo_Trabajo_en_empresa_(MESES)']<=6
rrhh_ptc_meses2 = pd.DataFrame(rrhh_ptc_meses2.value_counts())
rrhh_ptc_meses2 = rrhh_ptc_meses2.drop(False)
rrhh_ptc_meses2.index = ["6 meses o menos"]
rrhh_ptc_meses3 = rrhh_implementadores['Tiempo_Trabajo_en_empresa_(MESES)']>=12
rrhh_ptc_meses3 = pd.DataFrame(rrhh_ptc_meses3.value_counts())
rrhh_ptc_meses3 = rrhh_ptc_meses3.drop(False)
rrhh_ptc_meses3.index = ["12 meses o más"]
rrhh_ptc_meses_IMPLEMENT = rrhh_ptc_meses1.append([rrhh_ptc_meses2, rrhh_ptc_meses3])
rrhh_ptc_meses_IMPLEMENT['% respecto al total'] = ((rrhh_ptc_meses_IMPLEMENT['Tiempo_Trabajo_en_empresa_(MESES)'] / rrhh_ptc_meses_IMPLEMENT['Tiempo_Trabajo_en_empresa_(MESES)'].sum())*100)
rrhh_ptc_meses_IMPLEMENT = rrhh_ptc_meses_IMPLEMENT.rename(index=str, columns={"Tiempo_Trabajo_en_empresa_(MESES)": "Tiempo de trabajo en la empresa (MESES) - FRONT"}).round(1)
del(rrhh_ptc_meses1,rrhh_ptc_meses2,rrhh_ptc_meses3)

#Tabla de años en rubro
rrhh_ptc_rubro1 = rrhh_implementadores['Años_laborales_rubro_(MARKETING DIGITAL)']<=3
rrhh_ptc_rubro1 = pd.DataFrame(rrhh_ptc_rubro1.value_counts())
rrhh_ptc_rubro1 = rrhh_ptc_rubro1.drop(False)
rrhh_ptc_rubro1.index = ["3 meses o menos"]
rrhh_ptc_rubro2 = rrhh_implementadores['Años_laborales_rubro_(MARKETING DIGITAL)']<=6
rrhh_ptc_rubro2 = pd.DataFrame(rrhh_ptc_rubro2.value_counts())
rrhh_ptc_rubro2 = rrhh_ptc_rubro2.drop(False)
rrhh_ptc_rubro2.index = ["6 meses o menos"]
rrhh_ptc_rubro3 = rrhh_implementadores['Años_laborales_rubro_(MARKETING DIGITAL)']>6
rrhh_ptc_rubro3 = pd.DataFrame(rrhh_ptc_rubro3.value_counts())
rrhh_ptc_rubro3 = rrhh_ptc_rubro3.drop(False)
rrhh_ptc_rubro3.index = ["Más de 6 meses"]
rrhh_ptc_rubro_IMPLEMENT = rrhh_ptc_rubro1.append([rrhh_ptc_rubro2, rrhh_ptc_rubro3])
rrhh_ptc_rubro_IMPLEMENT['% respecto al total'] = ((rrhh_ptc_rubro_IMPLEMENT['Años_laborales_rubro_(MARKETING DIGITAL)'] / rrhh_ptc_rubro_IMPLEMENT['Años_laborales_rubro_(MARKETING DIGITAL)'].sum())*100)
rrhh_ptc_rubro_IMPLEMENT = rrhh_ptc_rubro_IMPLEMENT.rename(index=str, columns={'Años_laborales_rubro_(MARKETING DIGITAL)': 'Años laborales en el rubro (MARKETING DIGITAL)'}).round(1)
del(rrhh_ptc_rubro1,rrhh_ptc_rubro2,rrhh_ptc_rubro3)

#Tabla de edad
rrhh_ptc_edad1 = rrhh_implementadores['Edad']<=21
rrhh_ptc_edad1 = pd.DataFrame(rrhh_ptc_edad1.value_counts())
rrhh_ptc_edad1 = rrhh_ptc_edad1.drop(False)
rrhh_ptc_edad1.index = ["21 años o menos"]
rrhh_ptc_edad2 = rrhh_implementadores['Edad']<=25
rrhh_ptc_edad2 = pd.DataFrame(rrhh_ptc_edad2.value_counts())
rrhh_ptc_edad2 = rrhh_ptc_edad2.drop(False)
rrhh_ptc_edad2.index = ["25 años o menos"]
rrhh_ptc_edad3 = rrhh_implementadores['Edad']>30
rrhh_ptc_edad3 = pd.DataFrame(rrhh_ptc_edad3.value_counts())
rrhh_ptc_edad3 = rrhh_ptc_edad3.drop(False)
rrhh_ptc_edad3.index = ["30 años o más"]
rrhh_ptc_edad_IMPLEMENT = rrhh_ptc_edad1.append([rrhh_ptc_edad2, rrhh_ptc_edad3])
rrhh_ptc_edad_IMPLEMENT['% respecto al total'] = ((rrhh_ptc_edad_IMPLEMENT['Edad'] / rrhh_ptc_edad_IMPLEMENT['Edad'].sum())*100).round(1)
del(rrhh_ptc_edad1,rrhh_ptc_edad2,rrhh_ptc_edad3)

#Tabla de experiencia total
rrhh_ptc_expTot1 = rrhh_implementadores['Experiencia_Laboral_Total_(AÑOS)']<=3
rrhh_ptc_expTot1 = pd.DataFrame(rrhh_ptc_expTot1.value_counts())
rrhh_ptc_expTot1 = rrhh_ptc_expTot1.drop(False)
rrhh_ptc_expTot1.index = ["3 años o menos"]
rrhh_ptc_expTot2 = rrhh_implementadores['Experiencia_Laboral_Total_(AÑOS)']<=6
rrhh_ptc_expTot2 = pd.DataFrame(rrhh_ptc_expTot2.value_counts())
rrhh_ptc_expTot2 = rrhh_ptc_expTot2.drop(False)
rrhh_ptc_expTot2.index = ["6 años o menos"]
rrhh_ptc_expTot3 = rrhh_implementadores['Experiencia_Laboral_Total_(AÑOS)']>6
rrhh_ptc_expTot3 = pd.DataFrame(rrhh_ptc_expTot3.value_counts())
rrhh_ptc_expTot3 = rrhh_ptc_expTot3.drop(False)
rrhh_ptc_expTot3.index = ["Más de 6 meses"]

rrhh_ptc_expTot_IMPLEMENT = rrhh_ptc_expTot1.append([rrhh_ptc_expTot2, rrhh_ptc_expTot3])
rrhh_ptc_expTot_IMPLEMENT['% respecto al total'] = ((rrhh_ptc_expTot_IMPLEMENT['Experiencia_Laboral_Total_(AÑOS)'] / rrhh_ptc_expTot_IMPLEMENT['Experiencia_Laboral_Total_(AÑOS)'].sum())*100)
rrhh_ptc_expTot_IMPLEMENT = rrhh_ptc_expTot.rename(index=str, columns={'Experiencia_Laboral_Total_(AÑOS)': 'Experiencia laboral total (AÑOS)'}).round(1)
del(rrhh_ptc_expTot1,rrhh_ptc_expTot2,rrhh_ptc_expTot3)



#PASANTES
rrhh_ptc_meses1 = rrhh_pasantes['Tiempo_Trabajo_en_empresa_(MESES)']<=3
rrhh_ptc_meses1 = pd.DataFrame(rrhh_ptc_meses1.value_counts())
rrhh_ptc_meses1 = rrhh_ptc_meses1.drop(False)
rrhh_ptc_meses1.index = ["3 meses o menos"]
rrhh_ptc_meses2 = rrhh_pasantes['Tiempo_Trabajo_en_empresa_(MESES)']<=6
rrhh_ptc_meses2 = pd.DataFrame(rrhh_ptc_meses2.value_counts())
rrhh_ptc_meses2 = rrhh_ptc_meses2.drop(False)
rrhh_ptc_meses2.index = ["6 meses o menos"]
rrhh_ptc_meses3 = rrhh_pasantes['Tiempo_Trabajo_en_empresa_(MESES)']>=12
rrhh_ptc_meses3 = pd.DataFrame(rrhh_ptc_meses3.value_counts())
rrhh_ptc_meses3 = rrhh_ptc_meses3.drop(False)
rrhh_ptc_meses3.index = ["12 meses o más"]
rrhh_ptc_meses_PASANTES = rrhh_ptc_meses1.append([rrhh_ptc_meses2, rrhh_ptc_meses3])
rrhh_ptc_meses_PASANTES['% respecto al total'] = ((rrhh_ptc_meses_PASANTES['Tiempo_Trabajo_en_empresa_(MESES)'] / rrhh_ptc_meses_PASANTES['Tiempo_Trabajo_en_empresa_(MESES)'].sum())*100)
rrhh_ptc_meses_PASANTES = rrhh_ptc_meses_PASANTES.rename(index=str, columns={"Tiempo_Trabajo_en_empresa_(MESES)": "Tiempo de trabajo en la empresa (MESES) - FRONT"}).round(1)
del(rrhh_ptc_meses1,rrhh_ptc_meses2,rrhh_ptc_meses3)

#Tabla de años en rubro
rrhh_ptc_rubro1 = rrhh_pasantes['Años_laborales_rubro_(MARKETING DIGITAL)']<=3
rrhh_ptc_rubro1 = pd.DataFrame(rrhh_ptc_rubro1.value_counts())
rrhh_ptc_rubro1 = rrhh_ptc_rubro1.drop(False)
rrhh_ptc_rubro1.index = ["3 meses o menos"]
rrhh_ptc_rubro2 = rrhh_pasantes['Años_laborales_rubro_(MARKETING DIGITAL)']<=6
rrhh_ptc_rubro2 = pd.DataFrame(rrhh_ptc_rubro2.value_counts())
rrhh_ptc_rubro2 = rrhh_ptc_rubro2.drop(False)
rrhh_ptc_rubro2.index = ["6 meses o menos"]
rrhh_ptc_rubro3 = rrhh_pasantes['Años_laborales_rubro_(MARKETING DIGITAL)']>6
rrhh_ptc_rubro3 = pd.DataFrame(rrhh_ptc_rubro3.value_counts())
rrhh_ptc_rubro3 = rrhh_ptc_rubro3.drop(False)
rrhh_ptc_rubro3.index = ["Más de 6 meses"]
rrhh_ptc_rubro_PASANTES = rrhh_ptc_rubro1.append([rrhh_ptc_rubro2, rrhh_ptc_rubro3])
rrhh_ptc_rubro_PASANTES['% respecto al total'] = ((rrhh_ptc_rubro_PASANTES['Años_laborales_rubro_(MARKETING DIGITAL)'] / rrhh_ptc_rubro_PASANTES['Años_laborales_rubro_(MARKETING DIGITAL)'].sum())*100)
rrhh_ptc_rubro_PASANTES = rrhh_ptc_rubro_PASANTES.rename(index=str, columns={'Años_laborales_rubro_(MARKETING DIGITAL)': 'Años laborales en el rubro (MARKETING DIGITAL)'}).round(1)
del(rrhh_ptc_rubro1,rrhh_ptc_rubro2,rrhh_ptc_rubro3)

#Tabla de edad
rrhh_ptc_edad1 = rrhh_pasantes['Edad']<=21
rrhh_ptc_edad1 = pd.DataFrame(rrhh_ptc_edad1.value_counts())
rrhh_ptc_edad1 = rrhh_ptc_edad1.drop(False)
rrhh_ptc_edad1.index = ["21 años o menos"]
rrhh_ptc_edad2 = rrhh_pasantes['Edad']<=25
rrhh_ptc_edad2 = pd.DataFrame(rrhh_ptc_edad2.value_counts())
rrhh_ptc_edad2 = rrhh_ptc_edad2.drop(False)
rrhh_ptc_edad2.index = ["25 años o menos"]
rrhh_ptc_edad3 = rrhh_pasantes['Edad']>30
rrhh_ptc_edad3 = pd.DataFrame(rrhh_ptc_edad3.value_counts())
rrhh_ptc_edad3 = rrhh_ptc_edad3.drop(False)
rrhh_ptc_edad3.index = ["30 años o más"]
rrhh_ptc_edad_PASANTES = rrhh_ptc_edad1.append([rrhh_ptc_edad2, rrhh_ptc_edad3])
rrhh_ptc_edad_PASANTES['% respecto al total'] = ((rrhh_ptc_edad_PASANTES['Edad'] / rrhh_ptc_edad_PASANTES['Edad'].sum())*100).round(1)
del(rrhh_ptc_edad1,rrhh_ptc_edad2,rrhh_ptc_edad3)

#Tabla de experiencia total
rrhh_ptc_expTot1 = rrhh_pasantes['Experiencia_Laboral_Total_(AÑOS)']<=3
rrhh_ptc_expTot1 = pd.DataFrame(rrhh_ptc_expTot1.value_counts())
rrhh_ptc_expTot1 = rrhh_ptc_expTot1.drop(False)
rrhh_ptc_expTot1.index = ["3 años o menos"]
rrhh_ptc_expTot2 = rrhh_pasantes['Experiencia_Laboral_Total_(AÑOS)']<=6
rrhh_ptc_expTot2 = pd.DataFrame(rrhh_ptc_expTot2.value_counts())
rrhh_ptc_expTot2 = rrhh_ptc_expTot2.drop(False)
rrhh_ptc_expTot2.index = ["6 años o menos"]
rrhh_ptc_expTot3 = rrhh_pasantes['Experiencia_Laboral_Total_(AÑOS)']>6
rrhh_ptc_expTot3 = pd.DataFrame(rrhh_ptc_expTot3.value_counts())
rrhh_ptc_expTot3 = rrhh_ptc_expTot3.drop(False)
rrhh_ptc_expTot3.index = ["Más de 6 meses"]

rrhh_ptc_expTot_PASANTES = rrhh_ptc_expTot1.append([rrhh_ptc_expTot2, rrhh_ptc_expTot3])
rrhh_ptc_expTot_PASANTES['% respecto al total'] = ((rrhh_ptc_expTot_PASANTES['Experiencia_Laboral_Total_(AÑOS)'] / rrhh_ptc_expTot_PASANTES['Experiencia_Laboral_Total_(AÑOS)'].sum())*100)
rrhh_ptc_expTot_PASANTES = rrhh_ptc_expTot.rename(index=str, columns={'Experiencia_Laboral_Total_(AÑOS)': 'Experiencia laboral total (AÑOS)'}).round(1)
del(rrhh_ptc_expTot1,rrhh_ptc_expTot2,rrhh_ptc_expTot3)



#QAs
rrhh_ptc_meses1 = rrhh_QAs['Tiempo_Trabajo_en_empresa_(MESES)']<=3
rrhh_ptc_meses1 = pd.DataFrame(rrhh_ptc_meses1.value_counts())
rrhh_ptc_meses1 = rrhh_ptc_meses1.drop(False)
rrhh_ptc_meses1.index = ["3 meses o menos"]
rrhh_ptc_meses2 = rrhh_QAs['Tiempo_Trabajo_en_empresa_(MESES)']<=6
rrhh_ptc_meses2 = pd.DataFrame(rrhh_ptc_meses2.value_counts())
rrhh_ptc_meses2 = rrhh_ptc_meses2.drop(False)
rrhh_ptc_meses2.index = ["6 meses o menos"]
rrhh_ptc_meses3 = rrhh_QAs['Tiempo_Trabajo_en_empresa_(MESES)']>=12
rrhh_ptc_meses3 = pd.DataFrame(rrhh_ptc_meses3.value_counts())
rrhh_ptc_meses3 = rrhh_ptc_meses3.drop(False)
rrhh_ptc_meses3.index = ["12 meses o más"]
rrhh_ptc_meses_QAs = rrhh_ptc_meses1.append([rrhh_ptc_meses2, rrhh_ptc_meses3])
rrhh_ptc_meses_QAs['% respecto al total'] = ((rrhh_ptc_meses_QAs['Tiempo_Trabajo_en_empresa_(MESES)'] / rrhh_ptc_meses_QAs['Tiempo_Trabajo_en_empresa_(MESES)'].sum())*100)
rrhh_ptc_meses_QAs = rrhh_ptc_meses_QAs.rename(index=str, columns={"Tiempo_Trabajo_en_empresa_(MESES)": "Tiempo de trabajo en la empresa (MESES) - FRONT"}).round(1)
del(rrhh_ptc_meses1,rrhh_ptc_meses2,rrhh_ptc_meses3)

#Tabla de años en rubro
rrhh_ptc_rubro1 = rrhh_QAs['Años_laborales_rubro_(MARKETING DIGITAL)']<=3
rrhh_ptc_rubro1 = pd.DataFrame(rrhh_ptc_rubro1.value_counts())
rrhh_ptc_rubro1 = rrhh_ptc_rubro1.drop(False)
rrhh_ptc_rubro1.index = ["3 meses o menos"]
rrhh_ptc_rubro2 = rrhh_QAs['Años_laborales_rubro_(MARKETING DIGITAL)']<=6
rrhh_ptc_rubro2 = pd.DataFrame(rrhh_ptc_rubro2.value_counts())
rrhh_ptc_rubro2 = rrhh_ptc_rubro2.drop(False)
rrhh_ptc_rubro2.index = ["6 meses o menos"]
rrhh_ptc_rubro3 = rrhh_QAs['Años_laborales_rubro_(MARKETING DIGITAL)']>6
rrhh_ptc_rubro3 = pd.DataFrame(rrhh_ptc_rubro3.value_counts())
rrhh_ptc_rubro3 = rrhh_ptc_rubro3.drop(False)
rrhh_ptc_rubro3.index = ["Más de 6 meses"]
rrhh_ptc_rubro_QAs = rrhh_ptc_rubro1.append([rrhh_ptc_rubro2, rrhh_ptc_rubro3])
rrhh_ptc_rubro_QAs['% respecto al total'] = ((rrhh_ptc_rubro_QAs['Años_laborales_rubro_(MARKETING DIGITAL)'] / rrhh_ptc_rubro_QAs['Años_laborales_rubro_(MARKETING DIGITAL)'].sum())*100)
rrhh_ptc_rubro_QAs = rrhh_ptc_rubro_QAs.rename(index=str, columns={'Años_laborales_rubro_(MARKETING DIGITAL)': 'Años laborales en el rubro (MARKETING DIGITAL)'}).round(1)
del(rrhh_ptc_rubro1,rrhh_ptc_rubro2,rrhh_ptc_rubro3)

#Tabla de edad
rrhh_ptc_edad1 = rrhh_QAs['Edad']<=21
rrhh_ptc_edad1 = pd.DataFrame(rrhh_ptc_edad1.value_counts())
rrhh_ptc_edad1 = rrhh_ptc_edad1.drop(False)
rrhh_ptc_edad1.index = ["21 años o menos"]
rrhh_ptc_edad2 = rrhh_QAs['Edad']<=25
rrhh_ptc_edad2 = pd.DataFrame(rrhh_ptc_edad2.value_counts())
rrhh_ptc_edad2 = rrhh_ptc_edad2.drop(False)
rrhh_ptc_edad2.index = ["25 años o menos"]
rrhh_ptc_edad3 = rrhh_QAs['Edad']>30
rrhh_ptc_edad3 = pd.DataFrame(rrhh_ptc_edad3.value_counts())
rrhh_ptc_edad3 = rrhh_ptc_edad3.drop(False)
rrhh_ptc_edad3.index = ["30 años o más"]
rrhh_ptc_edad_QAs = rrhh_ptc_edad1.append([rrhh_ptc_edad2, rrhh_ptc_edad3])
rrhh_ptc_edad_QAs['% respecto al total'] = ((rrhh_ptc_edad_QAs['Edad'] / rrhh_ptc_edad_QAs['Edad'].sum())*100).round(1)
del(rrhh_ptc_edad1,rrhh_ptc_edad2,rrhh_ptc_edad3)

#Tabla de experiencia total
rrhh_ptc_expTot1 = rrhh_QAs['Experiencia_Laboral_Total_(AÑOS)']<=3
rrhh_ptc_expTot1 = pd.DataFrame(rrhh_ptc_expTot1.value_counts())
rrhh_ptc_expTot1 = rrhh_ptc_expTot1.drop(False)
rrhh_ptc_expTot1.index = ["3 años o menos"]
rrhh_ptc_expTot2 = rrhh_QAs['Experiencia_Laboral_Total_(AÑOS)']<=6
rrhh_ptc_expTot2 = pd.DataFrame(rrhh_ptc_expTot2.value_counts())
rrhh_ptc_expTot2 = rrhh_ptc_expTot2.drop(False)
rrhh_ptc_expTot2.index = ["6 años o menos"]
rrhh_ptc_expTot3 = rrhh_QAs['Experiencia_Laboral_Total_(AÑOS)']>6
rrhh_ptc_expTot3 = pd.DataFrame(rrhh_ptc_expTot3.value_counts())
rrhh_ptc_expTot3 = rrhh_ptc_expTot3.drop(False)
rrhh_ptc_expTot3.index = ["Más de 6 meses"]

rrhh_ptc_expTot_QAs = rrhh_ptc_expTot1.append([rrhh_ptc_expTot2, rrhh_ptc_expTot3])
rrhh_ptc_expTot_QAs['% respecto al total'] = ((rrhh_ptc_expTot_QAs['Experiencia_Laboral_Total_(AÑOS)'] / rrhh_ptc_expTot_QAs['Experiencia_Laboral_Total_(AÑOS)'].sum())*100)
rrhh_ptc_expTot_QAs = rrhh_ptc_expTot.rename(index=str, columns={'Experiencia_Laboral_Total_(AÑOS)': 'Experiencia laboral total (AÑOS)'}).round(1)
del(rrhh_ptc_expTot1,rrhh_ptc_expTot2,rrhh_ptc_expTot3)



#MANAGERS
rrhh_ptc_meses1 = RRHH_managers['Tiempo_Trabajo_en_empresa_(MESES)']<=3
rrhh_ptc_meses1 = pd.DataFrame(rrhh_ptc_meses1.value_counts())
rrhh_ptc_meses1 = rrhh_ptc_meses1.drop(False)
rrhh_ptc_meses1.index = ["3 meses o menos"]
rrhh_ptc_meses2 = RRHH_managers['Tiempo_Trabajo_en_empresa_(MESES)']<=6
rrhh_ptc_meses2 = pd.DataFrame(rrhh_ptc_meses2.value_counts())
rrhh_ptc_meses2 = rrhh_ptc_meses2.drop(False)
rrhh_ptc_meses2.index = ["6 meses o menos"]
rrhh_ptc_meses3 = RRHH_managers['Tiempo_Trabajo_en_empresa_(MESES)']>=12
rrhh_ptc_meses3 = pd.DataFrame(rrhh_ptc_meses3.value_counts())
rrhh_ptc_meses3 = rrhh_ptc_meses3.drop(False)
rrhh_ptc_meses3.index = ["12 meses o más"]
rrhh_ptc_meses_MANAGERS = rrhh_ptc_meses1.append([rrhh_ptc_meses2, rrhh_ptc_meses3])
rrhh_ptc_meses_MANAGERS['% respecto al total'] = ((rrhh_ptc_meses_MANAGERS['Tiempo_Trabajo_en_empresa_(MESES)'] / rrhh_ptc_meses_MANAGERS['Tiempo_Trabajo_en_empresa_(MESES)'].sum())*100)
rrhh_ptc_meses_MANAGERS = rrhh_ptc_meses_MANAGERS.rename(index=str, columns={"Tiempo_Trabajo_en_empresa_(MESES)": "Tiempo de trabajo en la empresa (MESES) - FRONT"}).round(1)
del(rrhh_ptc_meses1,rrhh_ptc_meses2,rrhh_ptc_meses3)

#Tabla de años en rubro
rrhh_ptc_rubro1 = RRHH_managers['Años_laborales_rubro_(MARKETING DIGITAL)']<=3
rrhh_ptc_rubro1 = pd.DataFrame(rrhh_ptc_rubro1.value_counts())
rrhh_ptc_rubro1 = rrhh_ptc_rubro1.drop(False)
rrhh_ptc_rubro1.index = ["3 meses o menos"]
rrhh_ptc_rubro2 = RRHH_managers['Años_laborales_rubro_(MARKETING DIGITAL)']<=6
rrhh_ptc_rubro2 = pd.DataFrame(rrhh_ptc_rubro2.value_counts())
rrhh_ptc_rubro2 = rrhh_ptc_rubro2.drop(False)
rrhh_ptc_rubro2.index = ["6 meses o menos"]
rrhh_ptc_rubro3 = RRHH_managers['Años_laborales_rubro_(MARKETING DIGITAL)']>6
rrhh_ptc_rubro3 = pd.DataFrame(rrhh_ptc_rubro3.value_counts())
rrhh_ptc_rubro3 = rrhh_ptc_rubro3.drop(False)
rrhh_ptc_rubro3.index = ["Más de 6 meses"]
rrhh_ptc_rubro_MANAGERS = rrhh_ptc_rubro1.append([rrhh_ptc_rubro2, rrhh_ptc_rubro3])
rrhh_ptc_rubro_MANAGERS['% respecto al total'] = ((rrhh_ptc_rubro_MANAGERS['Años_laborales_rubro_(MARKETING DIGITAL)'] / rrhh_ptc_rubro_MANAGERS['Años_laborales_rubro_(MARKETING DIGITAL)'].sum())*100)
rrhh_ptc_rubro_MANAGERS = rrhh_ptc_rubro_MANAGERS.rename(index=str, columns={'Años_laborales_rubro_(MARKETING DIGITAL)': 'Años laborales en el rubro (MARKETING DIGITAL)'}).round(1)
del(rrhh_ptc_rubro1,rrhh_ptc_rubro2,rrhh_ptc_rubro3)

#Tabla de edad
rrhh_ptc_edad1 = RRHH_managers['Edad']<=21
rrhh_ptc_edad1 = pd.DataFrame(rrhh_ptc_edad1.value_counts())
rrhh_ptc_edad1 = rrhh_ptc_edad1.drop(False)
rrhh_ptc_edad1.index = ["21 años o menos"]
rrhh_ptc_edad2 = RRHH_managers['Edad']<=25
rrhh_ptc_edad2 = pd.DataFrame(rrhh_ptc_edad2.value_counts())
rrhh_ptc_edad2 = rrhh_ptc_edad2.drop(False)
rrhh_ptc_edad2.index = ["25 años o menos"]
rrhh_ptc_edad3 = RRHH_managers['Edad']>30
rrhh_ptc_edad3 = pd.DataFrame(rrhh_ptc_edad3.value_counts())
rrhh_ptc_edad3 = rrhh_ptc_edad3.drop(False)
rrhh_ptc_edad3.index = ["30 años o más"]
rrhh_ptc_edad_MANAGERS = rrhh_ptc_edad1.append([rrhh_ptc_edad2, rrhh_ptc_edad3])
rrhh_ptc_edad_MANAGERS['% respecto al total'] = ((rrhh_ptc_edad_MANAGERS['Edad'] / rrhh_ptc_edad_MANAGERS['Edad'].sum())*100).round(1)
del(rrhh_ptc_edad1,rrhh_ptc_edad2,rrhh_ptc_edad3)

#Tabla de experiencia total
rrhh_ptc_expTot1 = RRHH_managers['Experiencia_Laboral_Total_(AÑOS)']<=3
rrhh_ptc_expTot1 = pd.DataFrame(rrhh_ptc_expTot1.value_counts())
rrhh_ptc_expTot1 = rrhh_ptc_expTot1.drop(False)
rrhh_ptc_expTot1.index = ["3 años o menos"]
rrhh_ptc_expTot2 = RRHH_managers['Experiencia_Laboral_Total_(AÑOS)']<=6
rrhh_ptc_expTot2 = pd.DataFrame(rrhh_ptc_expTot2.value_counts())
rrhh_ptc_expTot2 = rrhh_ptc_expTot2.drop(False)
rrhh_ptc_expTot2.index = ["6 años o menos"]
rrhh_ptc_expTot3 = RRHH_managers['Experiencia_Laboral_Total_(AÑOS)']>6
rrhh_ptc_expTot3 = pd.DataFrame(rrhh_ptc_expTot3.value_counts())
rrhh_ptc_expTot3 = rrhh_ptc_expTot3.drop(False)
rrhh_ptc_expTot3.index = ["Más de 6 meses"]

rrhh_ptc_expTot_MANAGERS = rrhh_ptc_expTot1.append([rrhh_ptc_expTot2, rrhh_ptc_expTot3])
rrhh_ptc_expTot_MANAGERS['% respecto al total'] = ((rrhh_ptc_expTot_MANAGERS['Experiencia_Laboral_Total_(AÑOS)'] / rrhh_ptc_expTot_MANAGERS['Experiencia_Laboral_Total_(AÑOS)'].sum())*100)
rrhh_ptc_expTot_QAs = rrhh_ptc_expTot.rename(index=str, columns={'Experiencia_Laboral_Total_(AÑOS)': 'Experiencia laboral total (AÑOS)'}).round(1)
del(rrhh_ptc_expTot1,rrhh_ptc_expTot2,rrhh_ptc_expTot3)




# =============================================================================
# 
# Automatizacion de reporte
# 
# =============================================================================

import xlrd

Excelsheet1 = 

Book1 = xlrd.open_workbook(Excelsheet1)










