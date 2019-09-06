library(stats)
library(pastecs)
library(tidyverse)
options(scipen=100)
options(digits=2)
pastecs <- stat.desc(RRHH, basic=F)

#Remove columns (solo luego de haber creado los df)
pastecs$`Miembro_del_equipo` = NULL
pastecs$`Area` = NULL
pastecs$`Estudios` = NULL
pastecs$`Rubro profesional` = NULL
pastecs$`Fortalezas` = NULL
pastecs$`Motivación` = NULL
pastecs$`Comentarios` = NULL
pastecs$`Oportunidades` = NULL
pastecs$`Debilidades` = NULL
pastecs$`Amenazas` = NULL
pastecs$`Naturaleza` = NULL
pastecs$`Tácticas` = NULL
pastecs$`Energia` = NULL
pastecs$`intro_extro` = NULL
pastecs$`Categorizacion` = NULL
pastecs$`Fecha_ingreso` = NULL
pastecs$`Fecha_Actual` = NULL

#Variables categóricas
categorias <- count(RRHH,Categorizacion) #La variable estÃ¡ borrada del df RRHH
intros_extros <- count(RRHH,intro_extro)
Energia <- count(RRHH,Energia)
Naturaleza <- count(RRHH,Naturaleza)
Tácticas <- count(RRHH,Tácticas)
rubro_p <- count(RRHH, RRHH$`Rubro profesional`)
AREA <- count(RRHH,Area)

#Export
write.csv(categorias, "C:\\Users\\juan.elorriaga\\Desktop\\categorias.csv", sep="\t")

#Segmentación 
library(sqldf)
fronts <- sqldf("SELECT * FROM RRHH WHERE Area='Front'")
managers <- sqldf("SELECT * FROM RRHH WHERE Area='Manager'")
pasantes <- sqldf("SELECT * FROM RRHH WHERE Area='Pasante'")
optimizaciones <- sqldf("SELECT * FROM RRHH WHERE Area='Optimización'")
implentaciones <- sqldf("SELECT * FROM RRHH WHERE Area='Implementación'")
QAs <- sqldf("SELECT * FROM RRHH WHERE Area='QA'")
datas <- sqldf("SELECT * FROM RRHH WHERE Area='Data Science'")

#sqldf("SELECT * FROM RRHH WHERE Categorizacion='INTJ'")

#Pastecs por Area
options(scipen=100)
options(digits=2)
pastecs_imple <- stat.desc(implentaciones, basic=F)
pastecs_imple$`Miembro_del_equipo` = NULL
pastecs_imple$`Area` = NULL
pastecs_imple$`Estudios` = NULL
pastecs_imple$`Rubro profesional` = NULL
pastecs_imple$`Fortalezas` = NULL
pastecs_imple$`Motivación` = NULL
pastecs_imple$`Comentarios` = NULL
pastecs_imple$`Oportunidades` = NULL
pastecs_imple$`Debilidades` = NULL
pastecs_imple$`Amenazas` = NULL
pastecs_imple$`Naturaleza` = NULL
pastecs_imple$`TÃ¡cticas` = NULL
pastecs_imple$`Energia` = NULL
pastecs_imple$`intro_extro` = NULL
pastecs_imple$`Categorizacion` = NULL
pastecs_imple$`Fecha_ingreso` = NULL
pastecs_imple$`Fecha_Actual` = NULL
pastecs_imple$`MotivaciÃ³n` = NULL
pastecs_imple$`TIEMPO TOTAL (min)` = NULL


options(scipen=100)
options(digits=2)
pastecs_optim <- stat.desc(optimizaciones, basic=F)
pastecs_optim$`Miembro_del_equipo` = NULL
pastecs_optim$`Area` = NULL
pastecs_optim$`Estudios` = NULL
pastecs_optim$`Rubro profesional` = NULL
pastecs_optim$`Fortalezas` = NULL
pastecs_optim$`Motivación` = NULL
pastecs_optim$`Comentarios` = NULL
pastecs_optim$`Oportunidades` = NULL
pastecs_optim$`Debilidades` = NULL
pastecs_optim$`Amenazas` = NULL
pastecs_optim$`Naturaleza` = NULL
pastecs_optim$`TÃ¡cticas` = NULL
pastecs_optim$`Energia` = NULL
pastecs_optim$`intro_extro` = NULL
pastecs_optim$`Categorizacion` = NULL
pastecs_optim$`Fecha_ingreso` = NULL
pastecs_optim$`Fecha_Actual` = NULL
pastecs_optim$`MotivaciÃ³n` = NULL
pastecs_optim$`TIEMPO TOTAL (min)` = NULL


options(scipen=100)
options(digits=2)
pastecs_QA <- stat.desc(QAs, basic=F)
pastecs_QA$`Miembro_del_equipo` = NULL
pastecs_QA$`Area` = NULL
pastecs_QA$`Estudios` = NULL
pastecs_QA$`Rubro profesional` = NULL
pastecs_QA$`Fortalezas` = NULL
pastecs_QA$`Motivación` = NULL
pastecs_QA$`Comentarios` = NULL
pastecs_QA$`Oportunidades` = NULL
pastecs_QA$`Debilidades` = NULL
pastecs_QA$`Amenazas` = NULL
pastecs_QA$`Naturaleza` = NULL
pastecs_QA$`TÃ¡cticas` = NULL
pastecs_QA$`Energia` = NULL
pastecs_QA$`intro_extro` = NULL
pastecs_QA$`Categorizacion` = NULL
pastecs_QA$`Fecha_ingreso` = NULL
pastecs_QA$`Fecha_Actual` = NULL
pastecs_QA$`MotivaciÃ³n` = NULL
pastecs_QA$`TIEMPO TOTAL (min)` = NULL


options(scipen=100)
options(digits=2)
pastecs_Fronts <- stat.desc(fronts, basic=F)
pastecs_Fronts$`Miembro_del_equipo` = NULL
pastecs_Fronts$`Area` = NULL
pastecs_Fronts$`Estudios` = NULL
pastecs_Fronts$`Rubro profesional` = NULL
pastecs_Fronts$`Fortalezas` = NULL
pastecs_Fronts$`Motivación` = NULL
pastecs_Fronts$`Comentarios` = NULL
pastecs_Fronts$`Oportunidades` = NULL
pastecs_Fronts$`Debilidades` = NULL
pastecs_Fronts$`Amenazas` = NULL
pastecs_Fronts$`Naturaleza` = NULL
pastecs_Fronts$`TÃ¡cticas` = NULL
pastecs_Fronts$`Energia` = NULL
pastecs_Fronts$`intro_extro` = NULL
pastecs_Fronts$`Categorizacion` = NULL
pastecs_Fronts$`Fecha_ingreso` = NULL
pastecs_Fronts$`Fecha_Actual` = NULL
pastecs_Fronts$`MotivaciÃ³n` = NULL
pastecs_Fronts$`TIEMPO TOTAL (min)` = NULL


options(scipen=100)
options(digits=2)
pastecs_pasantes <- stat.desc(pasantes, basic=F)
pastecs_pasantes$`Miembro_del_equipo` = NULL
pastecs_pasantes$`Area` = NULL
pastecs_pasantes$`Estudios` = NULL
pastecs_pasantes$`Rubro profesional` = NULL
pastecs_pasantes$`Fortalezas` = NULL
pastecs_pasantes$`Motivación` = NULL
pastecs_pasantes$`Comentarios` = NULL
pastecs_pasantes$`Oportunidades` = NULL
pastecs_pasantes$`Debilidades` = NULL
pastecs_pasantes$`Amenazas` = NULL
pastecs_pasantes$`Naturaleza` = NULL
pastecs_pasantes$`TÃ¡cticas` = NULL
pastecs_pasantes$`Energia` = NULL
pastecs_pasantes$`intro_extro` = NULL
pastecs_pasantes$`Categorizacion` = NULL
pastecs_pasantes$`Fecha_ingreso` = NULL
pastecs_pasantes$`Fecha_Actual` = NULL
pastecs_pasantes$`MotivaciÃ³n` = NULL
pastecs_pasantes$`TIEMPO TOTAL (min)` = NULL


#Gráficos

#Edad
graf_edad_equipo <- ggplot(RRHH, aes(x=Edad)) + geom_histogram(aes(fill = ..count..))  +
  scale_x_continuous(name = "Edad", breaks = seq(15,50,1)) +
  scale_y_continuous(name = "Frecuencia") +
  ggtitle("Frecuencia de Edad: \nmPLATFORM") + theme(plot.title = element_text(hjust = 0.5)) +
  geom_density(aes(y=..count..), colour = "midnightblue", fill = "cadetblue2", alpha=0.25)
  
graf_edad_equipo


#Meses empresa
graf_meses_emp_equipo <- ggplot(RRHH, aes(x=RRHH$`Tiempo_Trabajo_en_empresa_(MESES)`)) + geom_histogram(aes(fill = ..count..))  +
  scale_x_continuous(name = "Meses en empresa", breaks = seq(0,96,3), limits = c(0,30)) +
  scale_y_continuous(name = "Frecuencia") +
  ggtitle("Frecuencia de Meses en empresa: \nmPLATFORM") + theme(plot.title = element_text(hjust = 0.5)) +
  geom_density(aes(y=..count..), colour = "midnightblue", fill = "cadetblue2", alpha=0.25)

graf_meses_emp_equipo


#Experiencia_Laboral_Total
graf_exp_total_grupo <- ggplot(RRHH, aes(x=RRHH$`Experiencia Laboral total (AÑOS)`)) + geom_histogram(aes(fill = ..count..))  +
  scale_x_continuous(name = "Años de Trabajo Total", breaks = seq(1,16,2)) +
  scale_y_continuous(name = "Frecuencia") +
  ggtitle("Frecuencia de Años Laborales Total: \nmPLATFORM") + theme(plot.title = element_text(hjust = 0.5)) +
  geom_density(aes(y=..count..), colour = "midnightblue", fill = "cadetblue2", alpha=0.25)

graf_exp_total_grupo


#Porcentajes globales
graf_rdos_globales_equipo <- ggplot() +
  geom_density(aes(implentaciones$`% GLOBAL`), colour = "dodgerblue1", fill = "dodgerblue1", alpha=0.15, size=1) +
  geom_density(aes(fronts$`% GLOBAL`), colour = "firebrick2", fill = "firebrick2", alpha=0.15, size=1) +
  geom_density(aes(QAs$`% GLOBAL`), colour = "lightsalmon4", fill = "lightsalmon4", alpha=0.15, size=1) +
  geom_density(aes(optimizaciones$`% GLOBAL`), colour = "darkgoldenrod2", fill = "darkgoldenrod2", alpha=0.15, size=1) +
  geom_density(aes(pasantes$`% GLOBAL`), colour = "darkseagreen", fill = "darkseagreen", alpha=0.15, size=1) +
  scale_x_continuous(name = "Procentajes globales test") +
  scale_y_continuous(name = "Densidad") +
  ggtitle("Funcion de densidad de % globales test: \nmPLATFORM") + theme(plot.title = element_text(hjust = 0.5))

graf_rdos_globales_equipo <- graf_rdos_globales_equipo + theme(plot.subtitle = element_text(vjust = 1), 
                                                               plot.caption = element_text(vjust = 1)) +labs(caption = "ROJO = Front; VERDE = Pasantes; AZUL = Implementación; AMARILLO = Optimización; MARRÓN = QA")

graf_rdos_globales_equipo

#Resultados CI Test
graf_rdos_CI_equipo <- ggplot() +
  geom_density(aes(implentaciones$`CI TEST`), colour = "dodgerblue1", fill = "dodgerblue1", alpha=0.15, size=1) +
  geom_density(aes(fronts$`CI TEST`), colour = "firebrick2", fill = "firebrick2", alpha=0.15, size=1) +
  geom_density(aes(QAs$`CI TEST`), colour = "lightsalmon4", fill = "lightsalmon4", alpha=0.15, size=1) +
  geom_density(aes(optimizaciones$`CI TEST`), colour = "darkgoldenrod2", fill = "darkgoldenrod2", alpha=0.15, size=1) +
  geom_density(aes(pasantes$`CI TEST`), colour = "darkseagreen", fill = "darkseagreen", alpha=0.15, size=1) +
  scale_x_continuous(name = "Resultados CI Test") +
  scale_y_continuous(name = "Densidad") +
  ggtitle("Funcion de densidad de resultados CI test: \nmPLATFORM") + theme(plot.title = element_text(hjust = 0.5)) + 
  labs(colour="Type")  +
  scale_colour_manual(values=c("dodgerblue1", "firebrick2","lightsalmon4","darkgoldenrod2","darkseagreen"))

graf_rdos_CI_equipo <- graf_rdos_CI_equipo + theme(plot.subtitle = element_text(vjust = 1), 
    plot.caption = element_text(vjust = 1)) +labs(caption = "ROJO = Front; VERDE = Pasantes; AZUL = Implementación; AMARILLO = Optimización; MARRÓN = QA")

graf_rdos_CI_equipo





