#Algoritmo para aplicar las recomendaciones de Maronna
library(readr)
library(dplyr)

#FINAL 14 POZOS 100% CON RECORTE VARIABLE AT90
DATA           <- read_csv("C:/Users/SE31886/Documents/Prediccion_MN/PROP_ORGANICO/1MODELO_FINAL_FULL/predicciones/MN_Predecir_14pozos/AAFINALpred_df_TODO_filtroAT90_100porCiento.csv")

#Prediccion TODO
DATA_100_POZOS <- read_csv("C:/Users/SE31886/Documents/Prediccion_MN/PROP_ORGANICO/1MODELO_FINAL_FULL/predicciones/MN_Predecir_Todos_100pozos/AAFINAL_pred_df_100porCiento_recorteAT90_MNPredecirTodos.csv")
                 #col_types = cols(COCINA = col_factor(levels = c("0","1"))))

#prueba de calidad para los 100 pozos
#DATA_100_POZOS <- read_csv("C:/Users/SE31886/Documents/Prediccion_MN/PROP_ORGANICO/1MODELO_FINAL_FULL/predicciones/MN_Predecir_14pozos/AAFINALpred_df_TODO_filtroAT90_100porCiento.csv")
#DATA_100_POZOS <- read_csv("C:/Users/SE31886/Documents/Prediccion_MN/PROP_ORGANICO/AAFINAL_pred_df_100_recorteAT90_MNPredecirTodos.csv")

#DATA_100_POZOS <- DATA_100_POZOS %>% filter(AT90<=200)


#quito el DELTA segun metro y agrego un delta segun N de filas
DATA <- DATA[ , !(names(DATA) %in% c("DELTA"))]
DATA_100_POZOS <- DATA[ , !(names(DATA) %in% c("DELTA"))]

#library(dplyr)
DATA <- DATA %>% group_by(WELL) %>% mutate(DELTA = row_number())
DATA_100_POZOS <- DATA_100_POZOS %>% group_by(WELL) %>% mutate(DELTA = row_number())


#DATA           <- DATA            %>% group_by(WELL) %>% mutate(DELTA = DEPTH_MTS - min(DEPTH_MTS)) 
#DATA_100_POZOS <- DATA_100_POZOS  %>% group_by(WELL) %>% mutate(DELTA = DEPTH_MTS - min(DEPTH_MTS)) 



library(ggplot2)
library(GGally)
library(MASS)
library(Metrics)
library(sqldf)

#CORRELACIONES
suppressWarnings(ggcorr(DATA,size=3,label = TRUE,  label_size = 4, label_round = 2, label_alpha = TRUE, hjust = 0.6, size = 3) + ggtitle ("Correlaciones"))

suppressWarnings(ggcorr(DATA_100_POZOS,size=3,label = TRUE,  label_size = 4, label_round = 2, label_alpha = TRUE, hjust = 0.6, size = 3) + ggtitle ("Correlaciones"))



#Pozos en el set DATA
unique(DATA$WELL)

#Pozos en el set DATA_100_POZOS
unique(DATA_100_POZOS$WELL)

#Cantidad de observaciones por pozo en el set
sqldf("SELECT WELL, COUNT(1) Q_Observaciones FROM DATA GROUP BY WELL")

#Cantidad de observaciones por pozo en el set
sqldf("SELECT WELL, COUNT(1) Q_Observaciones FROM DATA_100_POZOS GROUP BY WELL")

resultados<-data.frame(WELL="",ISUP=0,IINF=0,n_raya_0=0)
resultados<-resultados[1==0,]

#CORRELACIONES POZO
#suppressWarnings(ggcorr(DATA_WELL,size=3,label = TRUE,  label_size = 4, label_round = 2, label_alpha = TRUE, hjust = 0.6, size = 3) + ggtitle ("Correlaciones"))

#F(X_i)=y_i
#X_i=(DEPTH_MTS; AT90; RO)
#y_i= MN_XO_AD predicho
#El objetivo del m茅todo de Maronna es dada una muestra y_1,.....,y_n todas con distribuci贸n F.
#encontrar un intervalo de confianza I=[a,b] tal que si y_0 (n observado) tiene distribuci贸n F 
#entonces Pr(a<= y_0 <=b)=1-alfa
#alfa= confianza

#Diferencia de los errores
#ri
#DATA_WELL$ri=DATA_WELL$MN_XO_AD-DATA_WELL$predict
#DATA_WELL$ri2=DATA_WELL$ri^2

#ri es el delta entre el verdadero MN y la predicci髇. ri2 es el cuadrado de ri
DATA$ri     = DATA$MN_XO_AD-DATA$predict
DATA$ri_est = (DATA$MN_XO_AD-DATA$predict)/sqrt(DATA$predict)
DATA$ri2    = DATA$ri^2

#Plot Error vs predicho / error vs real
#plot(DATA_WELL$predict, DATA_WELL$ri2)
#plot(DATA_WELL$MN_XO_AD, DATA_WELL$ri2)



residuales     <- plot(DATA$predict,DATA$ri) #gr醘ico de residuos te髍ico-est醤dar
residuales_est <- plot(DATA$predict,DATA$ri_est) #gr醘ico de residuos estandarizados
residuales_est_lm <- lm(DATA$ri_est ~ DATA$predict)
plot(residuales_est_lm)

plot(DATA$predict,DATA$ri2)
hist(DATA$MN_XO_AD)
hist(log(DATA$MN_XO_AD)) #normaliza el histograma

plot(DATA$MN_XO_AD, DATA$ri)
plot(DATA$MN_XO_AD, DATA$ri2)

#------------------------------------------------------------------------------------------
#Buscar un ^g(n_i) (smoother) que capture la relacion entre los errores del PLOT
#Utilizo loess con span elegido a ojo, family="Symmetric" que es robusta 
#y degree=1 porque es razonable suponer que la varianza es una funcion monotona de la media
#------------------------------------------------------------------------------------------

#loess con distintas intensidades de smooth
loessMod100 <- loess(ri2 ~ predict, data=DATA, method="loess", family="symmetric", degree=1, span=1) # 100% smoothing span
loessMod15  <- loess(ri2 ~ predict, data=DATA, method="loess", family="symmetric", degree=1, span=0.15) # 15% smoothing span
loessMod20  <- loess(ri2 ~ predict, data=DATA, method="loess", family="symmetric", degree=1, span=0.20) # 20% smoothing span
loessMod40  <- loess(ri2 ~ predict, data=DATA, method="loess", family="symmetric", degree=1, span=0.40) # 40% smoothing span
loessMod60  <- loess(ri2 ~ predict, data=DATA, method="loess", family="symmetric", degree=1, span=0.60) # 60% smoothing span

#Modelo lineal
modelo_lineal <- lm(ri2 ~ predict, data=DATA) #mismo que las regresiones LOESS, pero lineal est醤dar
summary(modelo_lineal)


# obtener smoothed output
smoothed100 <- predict(loessMod100,DATA$predict) #predice con loess 
smoothed15  <- predict(loessMod15,DATA$predict) 
smoothed20  <- predict(loessMod20,DATA$predict) 
smoothed40  <- predict(loessMod40,DATA$predict) 
smoothed60  <- predict(loessMod60,DATA$predict) 
lineal      <- predict(modelo_lineal,data=DATA$predict) #predice con modelo_lineal


#Modelo lineal loess
modelo_lineal_Loess <- lm(smoothed15 ~ predict, data=DATA)
summary(modelo_lineal_Loess)

lineal_loess <- predict(modelo_lineal_Loess,data=DATA$predict) 

# Plot 
plot(DATA$ri2,x=DATA$predict, type="p", main="Loess Smoothing ERROR and Prediction", xlab="MN_est", ylab="Error")
points(smoothed100, x=DATA$predict, col="blue")
points(smoothed15, x=DATA$predict, col="brown")
points(smoothed20, x=DATA$predict, col="pink")
points(smoothed40, x=DATA$predict, col="green")
points(smoothed60, x=DATA$predict, col="red")
points(lineal, x=DATA$predict, col="purple")
points(lineal_loess, x=DATA$predict, col="purple")

max(lineal_loess)
min(lineal_loess)
max(smoothed15)
min(smoothed15)

modelo_elegido <- modelo_lineal_Loess
smooth_elegido <- lineal_loess


DATA$ri2_est   <- smooth_elegido
smooth_elegido[smooth_elegido<0] <- 0 #reemplaza los valores negativos por 0
DATA$sigma_est <- sqrt(smooth_elegido) #revisar el pmax si resto no funciona


#calculo los ti
DATA$ti = DATA$ri/DATA$sigma_est

#ti vs predict
plot(DATA$ti,DATA$predict)

#IC-90%
alfa=0.1 
#calculo ta y tb
qnov=quantile(DATA$ri2, .9)
ta=quantile(DATA$ti,alfa/2)  
tb=quantile(DATA$ti,1-alfa/2)

#plot densidad F
plot(density(DATA$ti))
abline(v=ta, col="blue")
abline(v=tb, col="red")


#QUITADO DEL LOOP DE DATA_100_POZOS PORQUE LO HACE SOLO PARA LOS 14 POZOS. TEST DE PERFORMANCE
# Para cada observacion calculo la distancia |d_i-d_j| y el producto t_i*t_j
# Donde t_i son los residuos normalizados con varianza 1.
# t_i=r_i/^sigma_i
#Loop sobre 14 pozos de prediccion. Dataset "DATA"
#Los resultados de los loops internos se almacenan en una lista y luego se concatenan con "bind_rows"
table_agg <- list()
for (well in unique(DATA$WELL)){
  print(paste("Process...: ",well,sep=""))
  #I calculate variable "large",based on max value of the existing variable "DELTA" (numeric)
  wells_df <- DATA[DATA$WELL==well,]
  large = max(wells_df$DELTA)
  #cicle from 1 max.distance (large-1)
  for (d in c(1:(large-1))){
    #cicle from position 1 to large-distance (look how this turns to be symmetric)
    for (pos in (1:(large-d))){
      #I did all of this to calculate variables ti and tj 
      ti = wells_df[wells_df$DELTA==pos,]$ti
      tj = wells_df[wells_df$DELTA==pos+d,]$ti
      #I append the results into the once empty df "TABLE", and calculate p based on ti*tj
      table_agg[[length(table_agg)+1]]<-data.frame(well=well,d=d,p=ti*tj)
    }
  }
}

TABLE <- dplyr::bind_rows(table_agg)
#save(TABLE, file = "TABLE_final100.RData")
#load("TABLE_sinC.RData")


#loop por cada pozo de los 100
for (WELL_PROCESS in unique(DATA_100_POZOS$WELL)) {
  #----------------------------------------------------------------------------------
  #Tomo solo 1 pozo para las pruebas
  print("POZO------------------------------------------------------------------------------")
  print(WELL_PROCESS)
  DATA_WELL <- DATA_100_POZOS[DATA_100_POZOS$WELL==WELL_PROCESS,] #agarra solo el pozo del dataset
  
  # IC Observaciones individuales
  # [n_0 + ^sigma_0 * t_a ; n_0 + ^sigma_0 * t_b]
  #Tengo los numeros y calculo el intervalo para una observacion
  
  #Mi pozo 0 es el LCAV-21 en DATA_WELL
  #Calculo la varianza estimada 0 y sigma 0
  #Utilizo para eso la G() entrenada anteriormente y guardada en modelo_elegido
  DATA_WELL$Var_est0 = predict(modelo_elegido,data.frame(predict=DATA_WELL$predict))
  #DATA_WELL$Var_est0[DATA_WELL$Var_est0 < 0] <- 0
  DATA_WELL$sigma    = sqrt(DATA_WELL$Var_est0)
  
  DATA_WELL$linf <- DATA_WELL$predict+DATA_WELL$sigma*ta
  DATA_WELL$lsup <- DATA_WELL$predict+DATA_WELL$sigma*tb
  
  #plot = ggplot(data=DATA_WELL,aes(y=predict, x=DELTA)) + geom_point(aes(colour="predict")) 
  #plot = plot + geom_line(data=DATA_WELL,aes(y=lsup, x=DELTA), linetype=2)
  #plot = plot + geom_line(data=DATA_WELL,aes(y=linf, x=DELTA), linetype=2)
  #plot=plot + geom_point(data=DATA_WELL,aes(y=MN_XO_AD, x=DELTA,colour="real"), linetype=2)
  
  #plot
  
  #-----------------------------------------------------------------------------------------
  #GENERAL
  #--------------------------------------------------------------------------------
  #El IC quedar韆 por pozo:
  #[n_raya_0 + Za * raiz(v^_0) ; n_raya_0 + Zb * raiz(v^_0) 
  # Donde :
  # n_raya_0 = media de las predicciones
  #   Za y Zb son los cuantiles alfa/2 y 1 - alfa/2 de la normal estandar
  
  Za       <- qnorm(alfa/2)
  Zb       <- qnorm(1-alfa/2)
  n_raya_0 <- mean(DATA_WELL$predict)
  
  # v^_0 = 1/L^2 * (A + 2B)
  # A= Sum_i:1..L( sigma^2_0_i)
  #sigma^2_0_i = ^g(n_0_i) = smooth
  A = sum(DATA_WELL$Var_est0)
  
  
  #B= Sum_i:1..L-1(Sum_j:i+1..L(sigma_i * sigma_j * Ro_0_i_j)
  # Donde:
  #   sigma_i y sigma_j se obtienen con la smooth ^g
  
  # Ro_0_i_j es la correlaci贸n entre e_0_i y e_0_j
  # Asumimos que a mayor distancia la correlaci贸n disminuye
  # Ro_0_i_j = h(|d_i-d_j|)
  #donde h es una smooth creada con ti*tj=~h^(|di-dj|)
  # d_i y d_j es la profundidad desde el tope en metros
  
  #summary(lm(p~d,data=TABLA))
  # en estas condiciones B da cero
  
  #CALCULO INTERVALO
  # v^_0 = 1/L^2 * (A + 2B)
  v0 = (1/max(DATA_WELL$DELTA)^2) * A
  #El IC quedar铆a por pozo:
  #[n_raya_0 + Za * raiz(v^_0) ; n_raya_0 + Zb * raiz(v^_0) 
  ISUP=n_raya_0 + Zb * sqrt(v0)
  IINF=n_raya_0 + Za * sqrt(v0)
  
  print("ERROR RELATIVO PARA EL POZO")
  print((ISUP-IINF)/n_raya_0)
  
  #guardo en resultados
  resultados<-rbind(resultados,data.frame(WELL=WELL_PROCESS,ISUP=ISUP,IINF=IINF,n_raya_0=n_raya_0))
}

View(resultados)


#revision de duplicados. No deber韆 haber ninguno
sqldf("
SELECT WELL, COUNT(*)
FROM resultados
GROUP BY WELL
HAVING COUNT(*) > 1
      ")

#prueba con 1 pozo al azar
# sqldf("
# SELECT *
# FROM resultados
# WHERE WELL = \"YPF.NQ.LLL-101\"
#       ")

#Quito las filas que no tienen IC bien calculado
# resultados <- sqldf("
# SELECT DISTINCT WELL, MAX(ISUP), MIN(IINF), AVG(n_raya_0)
#       FROM resultados
#       GROUP BY WELL
#       ")

#save(resultados, file = "resultados_final_100.RData")
#load("resultados_sinC.RData")



#pdf("plot2_TODO_ENTERO98_FINAL.pdf")
#plot2<-ggplot(data=TABLE, aes(y=p,x=d)) + geom_point() + geom_smooth()
#plot2
#dev.off()
#summary(DATA_WELL$predict)

#library(EnvStats)
#qqPlot(x=DATA$ti,y=NULL,add.line=TRUE,qq.line.type = "robust")

write.csv(resultados,"C:/Users/SE31886/Documents/Prediccion_MN/PROP_ORGANICO/RESULTADOS_final_100.csv", row.names = FALSE)
