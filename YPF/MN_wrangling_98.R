
#PROYECTO MN.
#Script de wrangling
#IMPORTACIONES Y WRANGLING

#librerias
librerias <- c("corrplot","PerformanceAnalytics","reshape","sqldf","GGally","ggplot2","factoextra",
               "psych","plotrix","REdaS","ppls","Metrics","grid","gridExtra","lmtest","nls2","e1071",
               "glmnet","rpart","rpart.plot","caret","ggpubr","dplyr", "funModeling")

invisible(lapply(librerias, library, character.only = TRUE))
#Carga del parser de archivos .las
source("C:\\Users\\SE31886\\Documents\\Prediccion_MN\\COCINA\\script\\Las_parser_98.R")



#Tomo los datos descartando los valores -999 (count =  119153)
#cuenta_nulls <- sqldf("SELECT COUNT(*) FROM DATA_df WHERE (MN_XO_AD == -999 OR AT90 == -999)") #Cuenta de los registros que se quitar por -999
#datos_POZOS_DET <- filter(DATA_df, DATA_df$MN_XO_AD!=-999)
datos_POZOS_DET <- filter(datos_POZOS_DET, datos_POZOS_DET$AT90!=-999)
#datos_POZOS_DET<-DATA_df[DATA_df$MN_XO_AD!=-999,]

#listado de pozos. Profundidades max y min de cada pozo
#pozos_list <- sqldf("SELECT DISTINCT WELL FROM datos_POZOS_DET")
#pozos_maxmin <- sqldf("SELECT WELL, MAX(DEPTH), MIN(DEPTH), (MAX(DEPTH)-MIN(DEPTH)) FROM datos_POZOS_DET GROUP BY WELL")

#Agregar topes de cocina y Passey a pozos_list
# topes_c <- c(2944.17,3018.739,2775.14,2807.97,2824.277,2758.58,3081.38,2921.356,2910.81,2959.405,3071.012,3144.317,3041.42,2964.88)
# topes_passey <- c(2786.53,2770,2454.13,2643,2651,2579.25,2729.18,2705,2605.24,2725,2862,2949,2685.83,2523.32)
# pozos_list <- cbind(pozos_list, topes_c, topes_passey)


#Limpieza recorte final. Los números representan las BASES de los pozos de cocina y los topes de Passey

# datos_POZOS_DET_temp<-datos_POZOS_DET[(datos_POZOS_DET$WELL=='LCAV-21') & (datos_POZOS_DET$DEPTH<=2975.0004) & (datos_POZOS_DET$DEPTH>=2786.53),]
# datos_POZOS_DET_temp<-rbind(datos_POZOS_DET_temp,datos_POZOS_DET[(datos_POZOS_DET$WELL=='LRI-6(H)') & (datos_POZOS_DET$DEPTH<=3050.1337) & (datos_POZOS_DET$DEPTH>=2770),])
# datos_POZOS_DET_temp<-rbind(datos_POZOS_DET_temp,datos_POZOS_DET[(datos_POZOS_DET$WELL=='YPF.ADLA-1001(H)ST') & (datos_POZOS_DET$DEPTH<=2783.2812) & (datos_POZOS_DET$DEPTH>=2454.13),])
# datos_POZOS_DET_temp<-rbind(datos_POZOS_DET_temp,datos_POZOS_DET[(datos_POZOS_DET$WELL=='YPF.NQ.EOR-31') & (datos_POZOS_DET$DEPTH<=2838.1448) & (datos_POZOS_DET$DEPTH>=2643),])
# datos_POZOS_DET_temp<-rbind(datos_POZOS_DET_temp,datos_POZOS_DET[(datos_POZOS_DET$WELL=='YPF.NQ.EOR-35D') & (datos_POZOS_DET$DEPTH<=2852.0136) & (datos_POZOS_DET$DEPTH>=2651),])
# datos_POZOS_DET_temp<-rbind(datos_POZOS_DET_temp,datos_POZOS_DET[(datos_POZOS_DET$WELL=='YPF.NQ.EOR-45') & (datos_POZOS_DET$DEPTH<=2790.1392) & (datos_POZOS_DET$DEPTH>=2579.25),])
# datos_POZOS_DET_temp<-rbind(datos_POZOS_DET_temp,datos_POZOS_DET[(datos_POZOS_DET$WELL=='YPF.NQ.LACH-14') & (datos_POZOS_DET$DEPTH<=3112.922) & (datos_POZOS_DET$DEPTH>=2729.18),])
# datos_POZOS_DET_temp<-rbind(datos_POZOS_DET_temp,datos_POZOS_DET[(datos_POZOS_DET$WELL=='YPF.NQ.LACH-16') & (datos_POZOS_DET$DEPTH<=2950.0068) & (datos_POZOS_DET$DEPTH>=2705),])
# datos_POZOS_DET_temp<-rbind(datos_POZOS_DET_temp,datos_POZOS_DET[(datos_POZOS_DET$WELL=='YPF.NQ.LACH-17') & (datos_POZOS_DET$DEPTH<=2941.0152) & (datos_POZOS_DET$DEPTH>=2605.24),])
# datos_POZOS_DET_temp<-rbind(datos_POZOS_DET_temp,datos_POZOS_DET[(datos_POZOS_DET$WELL=='YPF.NQ.LACH-24') & (datos_POZOS_DET$DEPTH<=2983.0268) & (datos_POZOS_DET$DEPTH>=2725),])
# datos_POZOS_DET_temp<-rbind(datos_POZOS_DET_temp,datos_POZOS_DET[(datos_POZOS_DET$WELL=='YPF.NQ.LCAV-24') & (datos_POZOS_DET$DEPTH<=3102.7116) & (datos_POZOS_DET$DEPTH>=2862),])
# datos_POZOS_DET_temp<-rbind(datos_POZOS_DET_temp,datos_POZOS_DET[(datos_POZOS_DET$WELL=='YPF.NQ.LLL-993') & (datos_POZOS_DET$DEPTH<=3178.15) & (datos_POZOS_DET$DEPTH>=2949),])
# datos_POZOS_DET_temp<-rbind(datos_POZOS_DET_temp,datos_POZOS_DET[(datos_POZOS_DET$WELL=='YPF.NQ.LLL-997') & (datos_POZOS_DET$DEPTH<=3075.432) & (datos_POZOS_DET$DEPTH>=2685.93),])
# datos_POZOS_DET_temp<-rbind(datos_POZOS_DET_temp,datos_POZOS_DET[(datos_POZOS_DET$WELL=='YPF.NQ.RDM-184H') & (datos_POZOS_DET$DEPTH<=3000.1464) & (datos_POZOS_DET$DEPTH>=2523.32),])
# 
# 
# #Agregar variable RO como constante, según los valores de cocina
# datos_POZOS_DET_temp <- datos_POZOS_DET_temp %>% mutate(RO=case_when(
#   WELL == "LCAV-21"            ~ (1.3),
#   WELL == "LRI-6(H)"           ~ (1.3),
#   WELL == "YPF.ADLA-1001(H)ST" ~ (1.55),
#   WELL == "YPF.NQ.EOR-31"      ~ (1.45),
#   WELL == "YPF.NQ.EOR-35D"     ~ (1.55),
#   WELL == "YPF.NQ.EOR-45"      ~ (1.6),
#   WELL == "YPF.NQ.LACH-14"     ~ (0.9),
#   WELL == "YPF.NQ.LACH-16"     ~ (1),
#   WELL == "YPF.NQ.LACH-17"     ~ (1),
#   WELL == "YPF.NQ.LACH-24"     ~ (1.1),
#   WELL == "YPF.NQ.LCAV-24"     ~ (1.22),
#   WELL == "YPF.NQ.LLL-993"     ~ (1.08),
#   WELL == "YPF.NQ.LLL-997"     ~ (1.2),
#   WELL == "YPF.NQ.RDM-184H"    ~ (1.78)
# ))

#Agregar función decreciente de RO en función de DEPTH
#Desde el tope de cocina y hacia arriba, el RO decrece -0.1 por cada 200 metros de DEPTH.

#1  --> LEFT JOIN entre datos_pozos_det_temp y topes_c
#2  --> que la formula considere la columna de topes_c
#3  --> borrar tope_c del df
# datos_POZOS_DET_temp <- sqldf("SELECT datos_POZOS_DET_temp.*, pozos_list.topes_c
#                               FROM datos_POZOS_DET_temp
#                               LEFT JOIN pozos_list
#                               ON datos_POZOS_DET_temp.WELL = pozos_list.WELL")
# datos_POZOS_DET_temp <- datos_POZOS_DET_temp %>% group_by(WELL) %>% mutate(RO = RO - (0.1 * floor((mean(topes_c) - DEPTH)/200))) 
# datos_POZOS_DET_temp <- subset(datos_POZOS_DET_temp, select = -c(topes_c))



#redondeo a 4 cifras significativas
datos_POZOS_DET_temp$RO<-signif(datos_POZOS_DET_temp$RO,4)
datos_POZOS_DET_temp$AT90<-signif(datos_POZOS_DET_temp$AT90,4)
#datos_POZOS_DET_temp$MN_XO_AD<-signif(datos_POZOS_DET_temp$MN_XO_AD,4)

datos_POZOS_DET <- datos_POZOS_DET_temp
#sqldf("SELECT WELL, MIN(DEPTH) Tope, MAX(DEPTH) Base from datos_POZOS_DET_temp group by WELL")
rm(datos_POZOS_DET_temp)

#Agregar booleana de "cocina". 1="cocina". 0="no cocina"
# datos_POZOS_DET <- datos_POZOS_DET %>% mutate(COCINA=case_when(
#   (WELL == "LCAV-21"            & DEPTH >= 2944.17)   ~ 1,
#   (WELL == "LRI-6(H)"           & DEPTH >= 3018.739)  ~ 1,
#   (WELL == "YPF.ADLA-1001(H)ST" & DEPTH >= 2775.14)   ~ 1,
#   (WELL == "YPF.NQ.EOR-31"      & DEPTH >= 2807.97)   ~ 1,
#   (WELL == "YPF.NQ.EOR-35D"     & DEPTH >= 2824.277)  ~ 1,
#   (WELL == "YPF.NQ.EOR-45"      & DEPTH >= 2758.58)   ~ 1,
#   (WELL == "YPF.NQ.LACH-14"     & DEPTH >= 3081.38)   ~ 1,
#   (WELL == "YPF.NQ.LACH-16"     & DEPTH >= 2921.356)  ~ 1,
#   (WELL == "YPF.NQ.LACH-17"     & DEPTH >= 2910.81)   ~ 1,
#   (WELL == "YPF.NQ.LACH-24"     & DEPTH >= 2959.405)  ~ 1,
#   (WELL == "YPF.NQ.LCAV-24"     & DEPTH >= 3071.012)  ~ 1,
#   (WELL == "YPF.NQ.LLL-993"     & DEPTH >= 3144.317)  ~ 1,
#   (WELL == "YPF.NQ.LLL-997"     & DEPTH >= 3041.42)   ~ 1,
#   (WELL == "YPF.NQ.RDM-184H"    & DEPTH >= 2964.88)   ~ 1
# ))
# datos_POZOS_DET$COCINA[is.na(datos_POZOS_DET$COCINA)] <- 0


#df de cocina
# datos_solo_cocina <- datos_POZOS_DET %>% filter(COCINA == 1)
# datos_solo_cocina <- subset(datos_solo_cocina, select = c(WELL, DEPTH, AT90, MN_XO_AD, RO)) #para quitar variable COCINA

#df de NO cocina
# datos_sin_cocina <- datos_POZOS_DET %>% filter(COCINA == 0)
# datos_sin_cocina <- subset(datos_sin_cocina, select = c(WELL, DEPTH, AT90, MN_XO_AD, RO)) #para quitar variable COCINA



#Agrupación por metro. df total, solo cocina y resto de niveles
datos_GRP_POZO_DEPTH_TODO<-sqldf("SELECT  WELL,  CAST(DEPTH AS INTEGER) DEPTH_MTS,  AVG(Ro) RO,	AVG(AT90) AT90,	AVG(MN_XO_AD) MN_XO_AD, COCINA FROM datos_POZOS_DET GROUP BY WELL, CAST(DEPTH AS INTEGER), COCINA")
# datos_GRP_POZO_DEPTH_sinC<-sqldf("SELECT  WELL,  CAST(DEPTH AS INTEGER) DEPTH_MTS,  AVG(Ro) RO,	AVG(AT90) AT90,	AVG(MN_XO_AD) MN_XO_AD FROM datos_sin_cocina GROUP BY WELL, CAST(DEPTH AS INTEGER)")
# datos_GRP_POZO_DEPTH_soloC<-sqldf("SELECT  WELL,  CAST(DEPTH AS INTEGER) DEPTH_MTS,  AVG(Ro) RO,	AVG(AT90) AT90,	AVG(MN_XO_AD) MN_XO_AD FROM datos_solo_cocina GROUP BY WELL, CAST(DEPTH AS INTEGER)")

#Redondeo 4 cifras signif y variable categórica
datos_GRP_POZO_DEPTH_TODO$RO         <- signif(datos_GRP_POZO_DEPTH_TODO$RO,4)
datos_GRP_POZO_DEPTH_TODO$AT90       <- signif(datos_GRP_POZO_DEPTH_TODO$AT90,4)
datos_GRP_POZO_DEPTH_TODO$MN_XO_AD   <- signif(datos_GRP_POZO_DEPTH_TODO$MN_XO_AD,4)
datos_GRP_POZO_DEPTH_TODO$WELL       <-  as.factor(datos_GRP_POZO_DEPTH_TODO$WELL)
datos_GRP_POZO_DEPTH_TODO$COCINA     <-  as.factor(datos_GRP_POZO_DEPTH_TODO$COCINA)

datos_GRP_POZO_DEPTH_sinC$RO         <- signif(datos_GRP_POZO_DEPTH_sinC$RO,4)
datos_GRP_POZO_DEPTH_sinC$AT90       <- signif(datos_GRP_POZO_DEPTH_sinC$AT90,4)
datos_GRP_POZO_DEPTH_sinC$MN_XO_AD   <- signif(datos_GRP_POZO_DEPTH_sinC$MN_XO_AD,4)
datos_GRP_POZO_DEPTH_sinC$WELL       <- as.factor(datos_GRP_POZO_DEPTH_sinC$WELL)

datos_GRP_POZO_DEPTH_soloC$RO         <- signif(datos_GRP_POZO_DEPTH_soloC$RO,4)
datos_GRP_POZO_DEPTH_soloC$AT90       <- signif(datos_GRP_POZO_DEPTH_soloC$AT90,4)
datos_GRP_POZO_DEPTH_soloC$MN_XO_AD   <- signif(datos_GRP_POZO_DEPTH_soloC$MN_XO_AD,4)
datos_GRP_POZO_DEPTH_soloC$WELL       <- as.factor(datos_GRP_POZO_DEPTH_soloC$WELL)

#lista de pozos. Variable categórica
POZOS=unique(as.character(datos_GRP_POZO_DEPTH_TODO$WELL))
#df con promedio de variables, agrupado por pozo
POCIFICADO<-sqldf("SELECT WELL, AVG(DEPTH_MTS) AVG_DEPTH, AVG(RO) AVG_RO, AVG(AT90) AVG_AT90, AVG(MN_XO_AD) AVG_MN_XO_AD FROM datos_GRP_POZO_DEPTH_TODO GROUP BY WELL")
#Tabla de valores MN agrupados por pozo
tabla_real <- sqldf("SELECT WELL, AVG(MN_XO_AD) AVG_REAL FROM datos_GRP_POZO_DEPTH_sinC GROUP BY WELL ORDER BY WELL")





